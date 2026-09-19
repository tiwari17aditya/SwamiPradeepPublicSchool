"""
Master Pipeline Orchestrator for Swami Pradeep Public School.
Digitalizes handwritten exam papers and generates standardized school PDFs.

Pipeline Flow:
1. Fetch/Sync raw PDFs (from Google Drive Input Folder or local raw_inputs/).
2. Digitalize questions via AI Vision (with fallback models / resilient offline fallback).
3. Save clean digitized text file (.txt) in original language.
4. Extract exam metadata (Subject, Class, Type of Exam) using 3-tier preference:
   - 1st Preference: Extracted from input PDF (e.g. त्रैमासिक / Quarterly)
   - 2nd Preference: Configured in format_config.json / CLI --exam-type
   - 3rd Preference: If none given, no exam type is added
5. Generate official PDF with School Header, Date blank line, and diagonal Top-Left to Bottom-Right watermark.
6. Save output PDF named:
   - With exam type: <typeOfExam>_<class>_<subject>.pdf
   - Without exam type: <class>_<subject>.pdf
7. Optionally upload finished PDF to Google Drive Output Folder.
"""

import os
import sys
import argparse
import logging
from pathlib import Path
from typing import Optional, List, Dict, Any

# Ensure project root is in sys.path
BASE_DIR = Path(__file__).resolve().parent
if str(BASE_DIR) not in sys.path:
    sys.path.insert(0, str(BASE_DIR))

from datetime import datetime
from config.config_manager import (
    config_mgr,
    get_exam_subfolder,
    get_year_folder,
    get_class_subfolder,
    normalize_paper_key,
    parse_paper_key_from_filename
)
from core.ocr_extractor import PaperDigitalizer
from core.metadata_parser import MetadataParser
from core.pdf_generator import ExamPaperPDFGenerator
from core.drive_syncer import DriveSyncer

logger = logging.getLogger("Pipeline")
logging.basicConfig(level=logging.INFO, format="%(asctime)s [%(levelname)s] %(message)s")


class ExamDigitalizationPipeline:
    def __init__(self):
        self.config_mgr = config_mgr
        self.digitalizer = PaperDigitalizer()
        self.metadata_parser = MetadataParser(self.config_mgr.get_format_config())
        self.pdf_generator = ExamPaperPDFGenerator(self.config_mgr.get_format_config())
        self.drive_syncer = DriveSyncer(base_dir=str(self.config_mgr.BASE_DIR))

    def process_file(self, pdf_path: str, exam_type_override: Optional[str] = None, upload_to_drive: bool = False) -> Dict[str, Any]:
        """
        Executes complete pipeline on a single PDF file.
        """
        input_pdf = Path(pdf_path).resolve()
        if not input_pdf.exists():
            raise FileNotFoundError(f"Input PDF not found: {input_pdf}")

        logger.info(f"============================================================")
        logger.info(f"[1/4] Processing Input Paper: {input_pdf.name}")
        logger.info(f"============================================================")

        # Step 1: Digitalize handwritten paper into text in original language
        logger.info(f"[2/4] Digitalizing questions & transcribing handwriting...")
        raw_text, structured_data, saved_text_path = self.digitalizer.digitalize(str(input_pdf))
        logger.info(f" -> Digitized text saved at: {saved_text_path}")

        # Step 2: Extract & standardize metadata (3-tier preference)
        logger.info(f"[3/4] Parsing exam metadata (Subject, Class, Exam Type)...")
        extracted_meta = structured_data.get("metadata", {})
        metadata = self.metadata_parser.parse(
            text=raw_text,
            filename=input_pdf.name,
            default_meta=extracted_meta,
            config_override_exam=exam_type_override
        )

        exam_display = metadata.get('exam_type') or "[NONE - Not added]"
        logger.info(f" -> Exam Type : {exam_display}")
        logger.info(f" -> Class     : {metadata.get('class_name')}")
        logger.info(f" -> Subject   : {metadata.get('subject')}")
        logger.info(f" -> Max Marks : {metadata.get('max_marks')}")
        logger.info(f" -> Time      : {metadata.get('time_allowed')}")

        # Step 3: Compute output filename: <typeOfExam>_<class>_<subject>.pdf or <class>_<subject>.pdf
        output_pdf_path = self.config_mgr.resolve_output_pdf_path(metadata)
        logger.info(f"[4/4] Generating formatted PDF with Watermark & School Header: {output_pdf_path.name}")

        # Deduplication: remove any existing stale variant of the same paper in the target directory
        current_key = normalize_paper_key(
            metadata.get("exam_type", ""),
            metadata.get("class_name", ""),
            metadata.get("subject", "")
        )
        for existing in output_pdf_path.parent.glob("*.pdf"):
            if existing.name != output_pdf_path.name:
                if parse_paper_key_from_filename(existing.name) == current_key:
                    existing.unlink(missing_ok=True)
                    logger.info(f"[Pipeline] Removed stale duplicate in local output: {existing.name}")

        sections = structured_data.get("sections", [])
        instructions = structured_data.get("general_instructions", [])

        generated_pdf = self.pdf_generator.generate_pdf(
            output_path=str(output_pdf_path),
            metadata=metadata,
            sections=sections,
            general_instructions=instructions
        )

        drive_link = None
        if upload_to_drive or self.config_mgr.get_drive_config().get("enabled", False):
            logger.info("Uploading generated exam PDF to Google Drive Output hierarchy...")
            drive_link = self.drive_syncer.upload_output(generated_pdf, metadata=metadata)

        logger.info(f"============================================================")
        logger.info(f" SUCCESS! Generated Exam Paper PDF: {generated_pdf}")
        if drive_link:
            logger.info(f" Google Drive Link: {drive_link}")
        logger.info(f"============================================================")

        # Automatically update tabular README ledgers in input, output, and text directories
        self._update_tabular_ledgers(input_pdf, generated_pdf, metadata, saved_text_path)

        return {
            "input_file": str(input_pdf),
            "digitized_text_file": saved_text_path,
            "output_pdf_file": generated_pdf,
            "metadata": metadata,
            "drive_link": drive_link
        }

    def _update_tabular_ledgers(self, input_pdf: Path, output_pdf: str, metadata: Dict[str, Any], saved_text_path: str):
        """
        Maintains tabular markdown ledgers with timestamps in raw_inputs, output_pdfs, and digitized_texts.
        Guarantees zero duplicate entries by updating existing records in-place.
        """
        now_str = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        # 1. Update raw_inputs/README.md
        raw_readme = self.config_mgr.RAW_INPUTS_DIR / "README.md"
        if raw_readme.exists():
            content = raw_readme.read_text(encoding="utf-8")
            header_lines = []
            data_rows = []
            for line in content.splitlines():
                if line.strip().startswith("| Sl") or not line.strip().startswith("|"):
                    header_lines.append(line)
                elif "---" in line:
                    header_lines.append(line)
                else:
                    cols = [c.strip() for c in line.strip().split("|")[1:-1]]
                    if len(cols) >= 4:
                        data_rows.append(cols)

            updated = False
            for r in data_rows:
                if r[1] == input_pdf.name:
                    r[3] = now_str
                    r[4] = "Processed"
                    updated = True
                    break
            if not updated:
                data_rows.append([str(len(data_rows) + 1), input_pdf.name, "Auto-Detected", now_str, "Processed"])

            new_lines = list(header_lines)
            for idx, r in enumerate(data_rows, 1):
                new_lines.append(f"| {idx} | {r[1]} | {r[2]} | {r[3]} | {r[4]} |")
            raw_readme.write_text("\n".join(new_lines) + "\n", encoding="utf-8")

        # 2. Update output_pdfs/README.md
        out_readme = self.config_mgr.OUTPUT_PDFS_DIR / "README.md"
        if out_readme.exists():
            content = out_readme.read_text(encoding="utf-8")
            header_lines = []
            data_rows = []
            for line in content.splitlines():
                if line.strip().startswith("| Sl") or not line.strip().startswith("|"):
                    header_lines.append(line)
                elif "---" in line:
                    header_lines.append(line)
                else:
                    cols = [c.strip() for c in line.strip().split("|")[1:-1]]
                    if len(cols) >= 7:
                        data_rows.append(cols)

            out_name = Path(output_pdf).name
            exam_sub = get_exam_subfolder(metadata.get("exam_type", ""))
            year_sub = get_year_folder(metadata, self.config_mgr.get_format_config().get("school", {}).get("academic_session", "2026-2027"))
            class_sub = get_class_subfolder(metadata.get("class_name", ""))
            drive_loc = f"`{year_sub}/{exam_sub}/{class_sub}/`"
            cls_name = metadata.get("class_name", "").replace("_", " ")
            subj = metadata.get("subject", "").replace("_", " ")
            exam_t = metadata.get("exam_type") or "General"
            current_key = normalize_paper_key(exam_t, cls_name, subj)

            updated = False
            for r in data_rows:
                row_key = parse_paper_key_from_filename(r[1])
                if row_key == current_key or r[1] == out_name:
                    r[1] = out_name
                    r[2] = exam_t
                    r[3] = cls_name
                    r[4] = subj
                    r[5] = year_sub
                    r[6] = now_str
                    r[7] = drive_loc
                    updated = True
                    break
            if not updated:
                data_rows.append([str(len(data_rows) + 1), out_name, exam_t, cls_name, subj, year_sub, now_str, drive_loc])

            new_lines = list(header_lines)
            for idx, r in enumerate(data_rows, 1):
                new_lines.append(f"| {idx} | {r[1]} | {r[2]} | {r[3]} | {r[4]} | {r[5]} | {r[6]} | {r[7]} |")
            out_readme.write_text("\n".join(new_lines) + "\n", encoding="utf-8")

        # 3. Update digitized_texts/README.md
        txt_readme = self.config_mgr.DIGITIZED_TEXTS_DIR / "README.md"
        if txt_readme.exists():
            content = txt_readme.read_text(encoding="utf-8")
            header_lines = []
            data_rows = []
            for line in content.splitlines():
                if line.strip().startswith("| Sl") or not line.strip().startswith("|"):
                    header_lines.append(line)
                elif "---" in line:
                    header_lines.append(line)
                else:
                    cols = [c.strip() for c in line.strip().split("|")[1:-1]]
                    if len(cols) >= 5:
                        data_rows.append(cols)

            txt_name = Path(saved_text_path).name
            updated = False
            for r in data_rows:
                if r[1] == input_pdf.name:
                    r[2] = txt_name
                    r[3] = "Bilingual"
                    r[4] = now_str
                    r[5] = "Completed"
                    updated = True
                    break
            if not updated:
                data_rows.append([str(len(data_rows) + 1), input_pdf.name, txt_name, "Bilingual", now_str, "Completed"])

            new_lines = list(header_lines)
            for idx, r in enumerate(data_rows, 1):
                new_lines.append(f"| {idx} | {r[1]} | {r[2]} | {r[3]} | {r[4]} | {r[5]} |")
            txt_readme.write_text("\n".join(new_lines) + "\n", encoding="utf-8")

    def run_all(
        self,
        sync_drive: bool = False,
        specific_input: Optional[str] = None,
        exam_type_override: Optional[str] = None
    ) -> List[Dict[str, Any]]:
        """
        Runs the pipeline on input file or synchronizes and processes all available raw inputs.
        """
        results = []

        if specific_input:
            res = self.process_file(specific_input, exam_type_override=exam_type_override, upload_to_drive=sync_drive)
            results.append(res)
            return results

        should_sync = sync_drive or self.config_mgr.get_drive_config().get("enabled", False)
        if should_sync:
            logger.info("Synchronizing files from Google Drive Input Folder...")
            new_files = self.drive_syncer.sync()
            logger.info(f"Synced {len(new_files)} files from Google Drive.")

        # Process all pending PDFs in raw_inputs
        raw_files = list(self.config_mgr.RAW_INPUTS_DIR.glob("*.pdf"))
        if not raw_files:
            sample_files = list(self.config_mgr.SAMPLE_DIR.glob("*.pdf"))
            if sample_files:
                logger.info("raw_inputs empty, running on available sample files...")
                raw_files = sample_files

        if not raw_files:
            logger.warning("No PDF papers found to process in raw_inputs or sample directory.")
            return results

        for pdf_file in raw_files:
            try:
                res = self.process_file(str(pdf_file), exam_type_override=exam_type_override, upload_to_drive=sync_drive)
                results.append(res)
            except Exception as e:
                logger.error(f"Failed to process {pdf_file.name}: {e}", exc_info=True)

        return results


def main():
    parser = argparse.ArgumentParser(
        description="Swami Pradeep Public School - Exam Paper Digitalization Pipeline"
    )
    parser.add_argument(
        "--input", "-i",
        type=str,
        help="Path to a specific input PDF paper (e.g. raw_inputs/Sample.pdf)"
    )
    parser.add_argument(
        "--exam-type", "-e",
        type=str,
        default=None,
        help="Override or specify exam type (e.g. 'Quarterly', 'Half_Yearly', 'Final_Exam', or '' for none)"
    )
    parser.add_argument(
        "--sync-drive", "-s",
        action="store_true",
        help="Synchronize with Google Drive (download from input folder, upload finished PDFs to output folder)"
    )
    parser.add_argument(
        "--watch", "-w",
        action="store_true",
        help="Run continuously in the background and watch for new papers"
    )
    parser.add_argument(
        "--interval",
        type=int,
        default=30,
        help="Seconds between checks in watch mode (default: 30s)"
    )

    args = parser.parse_args()
    pipeline = ExamDigitalizationPipeline()

    if args.watch:
        import time
        logger.info(f"Starting continuous watch mode (polling every {args.interval} seconds)...")
        logger.info("Press Ctrl+C to stop.")
        try:
            while True:
                pipeline.run_all(
                    sync_drive=args.sync_drive,
                    specific_input=args.input,
                    exam_type_override=args.exam_type
                )
                time.sleep(args.interval)
        except KeyboardInterrupt:
            logger.info("Watch mode stopped.")
            return

    results = pipeline.run_all(
        sync_drive=args.sync_drive,
        specific_input=args.input,
        exam_type_override=args.exam_type
    )

    print("\n" + "=" * 60)
    print("PIPELINE SUMMARY:")
    print("=" * 60)
    for r in results:
        print(f"Input:          {r['input_file']}")
        print(f"Digitized Text: {r['digitized_text_file']}")
        print(f"Final PDF:      {r['output_pdf_file']}")
        print(f"Format:         {Path(r['output_pdf_file']).name}")
        if r.get("drive_link"):
            print(f"Drive Link:     {r['drive_link']}")
        print("-" * 60)

if __name__ == "__main__":
    main()
