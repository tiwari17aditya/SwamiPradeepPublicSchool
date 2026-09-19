"""
Central Configuration & Path Management for Swami Pradeep Public School Pipeline.
Manages all directories, file paths, fallback models, hierarchical output folders, and configs.
"""

import os
import re
import json
from pathlib import Path
from typing import Dict, Any, List, Optional

def sanitize_json_text(raw_text: str) -> str:
    """Fixes unescaped Windows backslashes in JSON strings."""
    # Replace single backslashes that are not valid escape characters
    return re.sub(r'\\(?!["\\/bfnrtu])', r'\\\\', raw_text)

def get_exam_subfolder(exam_type: str) -> str:
    """
    Standardizes exam subfolder name into: Quarterly, Half-Yearly, Final, or General.
    """
    exam_lower = (exam_type or "").lower().replace("-", "_").replace(" ", "_")
    if "quarter" in exam_lower or "त्रैमासिक" in exam_lower:
        return "Quarterly"
    elif "half" in exam_lower or "mid" in exam_lower or "अर्धवार्षिक" in exam_lower:
        return "Half-Yearly"
    elif "final" in exam_lower or "annual" in exam_lower or "वार्षिक" in exam_lower:
        return "Final"
    elif "unit" in exam_lower:
        return "Unit_Test"
    elif "periodic" in exam_lower:
        return "Periodic_Test"
    elif exam_type and exam_type.strip():
        return exam_type.strip().replace(" ", "_")
    else:
        return "General"

def get_year_folder(metadata: Dict[str, Any], default_session: str = "2026-2027") -> str:
    """
    Extracts or formats academic session/year folder.
    """
    session = metadata.get("academic_session") or default_session
    clean = re.sub(r"[^\w\d\-]", "_", str(session)).strip("_")
    return clean or "2026-2027"

def get_class_subfolder(class_name: Optional[str]) -> str:
    """
    Standardizes class subfolder name for hierarchical storage:
    e.g. 'Class_1', 'Class_2', 'Class_KG1', 'Class_1to2'
    """
    if not class_name:
        return "Class_General"
    cls_str = str(class_name).strip()
    clean = re.sub(r"[^a-zA-Z0-9_]", "_", cls_str).strip("_")
    clean = re.sub(r"_+", "_", clean)
    if not clean.lower().startswith("class"):
        clean = f"Class_{clean}"
    return clean

def normalize_paper_key(exam_type: str = "", class_name: str = "", subject: str = "") -> str:
    """
    Computes a canonical deduplication key for an exam paper, e.g.:
    exam='Quarterly', class='Class_6' / 'Class_6TH', subject='Mathematics' / 'Maths' -> 'quarterly:class6:mathematics'
    """
    exam_clean = re.sub(r"[^a-z0-9]", "", str(exam_type or "").lower())
    cls_clean = str(class_name or "").lower().replace(" ", "").replace("_", "")
    cls_clean = re.sub(r"(st|nd|rd|th)$", "", cls_clean)
    sub_clean = str(subject or "").lower().replace(" ", "").replace("_", "")
    if "sst" in sub_clean or "social" in sub_clean:
        sub_clean = "socialscience"
    elif "evs" in sub_clean or "environ" in sub_clean or "पर्यावरण" in sub_clean:
        sub_clean = "evs"
    elif "math" in sub_clean or "गणित" in sub_clean:
        sub_clean = "mathematics"
    elif "sci" in sub_clean or "विज्ञान" in sub_clean:
        sub_clean = "science"
    elif "eng" in sub_clean or "अंग्रेजी" in sub_clean:
        sub_clean = "english"
    elif "hin" in sub_clean or "हिन्दी" in sub_clean or "हिंदी" in sub_clean:
        sub_clean = "hindi"
    elif "sans" in sub_clean or "संस्कृत" in sub_clean:
        sub_clean = "sanskrit"
    elif "comp" in sub_clean:
        sub_clean = "computer"
    elif "gk" in sub_clean:
        sub_clean = "gk"
    return f"{exam_clean}:{cls_clean}:{sub_clean}"

def parse_paper_key_from_filename(filename: str) -> str:
    """
    Extracts canonical paper key from a generated PDF filename like 'Quarterly_Class_6TH_Science.pdf'.
    """
    stem = Path(filename).stem
    parts = stem.split("_")
    if len(parts) >= 3:
        exam = parts[0]
        if parts[1].lower() == "class" and len(parts) >= 4:
            cls = f"Class_{parts[2]}"
            subj = "_".join(parts[3:])
        else:
            cls = parts[1]
            subj = "_".join(parts[2:])
        return normalize_paper_key(exam, cls, subj)
    return normalize_paper_key("", "", stem)


class ConfigManager:
    """
    Unified manager for all paths, file formats, hierarchical output trees, and API fallbacks.
    """
    def __init__(self, base_dir: Optional[str] = None):
        if base_dir:
            self.BASE_DIR = Path(base_dir).resolve()
        else:
            current_file = Path(__file__).resolve()
            if current_file.parent.name == "config":
                self.BASE_DIR = current_file.parent.parent
            else:
                self.BASE_DIR = current_file.parent

        # Core directories inside Digitalizing_Papers
        self.CONFIG_DIR = self.BASE_DIR / "config"
        self.CORE_DIR = self.BASE_DIR / "core"
        self.RAW_INPUTS_DIR = self.BASE_DIR / "raw_inputs"
        self.DIGITIZED_TEXTS_DIR = self.BASE_DIR / "digitized_texts"
        self.OUTPUT_PDFS_DIR = self.BASE_DIR / "output_pdfs"
        self.ARCHIVE_DIR = self.BASE_DIR / "archive"
        self.SAMPLE_DIR = self.BASE_DIR / "sample"
        self.FONTS_DIR = self.BASE_DIR / "fonts"

        # Config files
        self.FORMAT_CONFIG_PATH = self.CONFIG_DIR / "format_config.json"
        self.DRIVE_CONFIG_PATH = self.CONFIG_DIR / "drive_config.json"

        # Model Fallback Chain
        self.MODEL_FALLBACK_CHAIN: List[str] = [
            "gemini-2.5-flash",
            "gemini-2.5-pro",
            "gemini-2.0-flash",
            "gemini-1.5-flash",
            "gemini-1.5-pro"
        ]

        self.ensure_directories()
        self._format_config: Optional[Dict[str, Any]] = None
        self._drive_config: Optional[Dict[str, Any]] = None

    def ensure_directories(self):
        """Creates all required directories."""
        for d in [
            self.CONFIG_DIR,
            self.CORE_DIR,
            self.RAW_INPUTS_DIR,
            self.DIGITIZED_TEXTS_DIR,
            self.OUTPUT_PDFS_DIR,
            self.ARCHIVE_DIR,
            self.SAMPLE_DIR,
            self.FONTS_DIR
        ]:
            d.mkdir(parents=True, exist_ok=True)

    def get_format_config(self) -> Dict[str, Any]:
        """Loads and returns the paper formatting configuration."""
        if self._format_config is None:
            if self.FORMAT_CONFIG_PATH.exists():
                try:
                    with open(self.FORMAT_CONFIG_PATH, "r", encoding="utf-8") as f:
                        raw = f.read()
                        self._format_config = json.loads(sanitize_json_text(raw))
                except Exception as e:
                    print(f"[ConfigManager] Error reading format config: {e}")
                    self._format_config = self._default_format_config()
            else:
                self._format_config = self._default_format_config()
        return self._format_config

    def get_drive_config(self) -> Dict[str, Any]:
        """Loads and returns the Google Drive configuration."""
        if self._drive_config is None:
            if self.DRIVE_CONFIG_PATH.exists():
                try:
                    with open(self.DRIVE_CONFIG_PATH, "r", encoding="utf-8") as f:
                        raw = f.read()
                        self._drive_config = json.loads(sanitize_json_text(raw))
                except Exception as e:
                    print(f"[ConfigManager] Error reading drive config: {e}")
                    self._drive_config = {}
            else:
                self._drive_config = {}
        return self._drive_config

    def get_fallback_models(self) -> List[str]:
        """Returns ordered list of models to try if quota or rate-limits are encountered."""
        custom_chain = self.get_format_config().get("ai_models", {}).get("fallback_chain")
        if custom_chain and isinstance(custom_chain, list):
            return custom_chain
        return self.MODEL_FALLBACK_CHAIN

    def resolve_output_pdf_path(self, metadata: Dict[str, Any]) -> Path:
        """
        Computes the target output PDF path inside hierarchical folders:
        output_pdfs/<Year>/<ExamType>/<Class>/<filename>.pdf
        """
        year_folder = get_year_folder(metadata, self.get_format_config().get("school", {}).get("academic_session", "2026-2027"))
        exam_subfolder = get_exam_subfolder(metadata.get("exam_type", ""))
        class_subfolder = get_class_subfolder(metadata.get("class_name", ""))

        target_dir = self.OUTPUT_PDFS_DIR / year_folder / exam_subfolder / class_subfolder
        target_dir.mkdir(parents=True, exist_ok=True)

        exam = metadata.get("exam_type", "").strip().replace(" ", "_")
        cls = metadata.get("class_name", "Class").strip().replace(" ", "_")
        subj = metadata.get("subject", "Subject").strip().replace(" ", "_")

        if exam:
            filename = f"{exam}_{cls}_{subj}.pdf"
        else:
            filename = f"{cls}_{subj}.pdf"

        return target_dir / filename

    @staticmethod
    def _default_format_config() -> Dict[str, Any]:
        return {
            "school": {
                "name": "SWAMI PRADEEP PUBLIC SCHOOL, Deori, Sagar, M.P.",
                "academic_session": "2026-2027"
            },
            "watermark": {
                "enabled": True,
                "text": "Swami Pradeep Public School",
                "angle": -40.0,
                "font_size": 42,
                "opacity": 0.11
            }
        }

# Global shared instance
config_mgr = ConfigManager()
