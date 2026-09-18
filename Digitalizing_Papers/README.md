# Swami Pradeep Public School - Exam Paper Digitalization Pipeline

A modular, automated system to ingest handwritten exam papers and notes (via Google Drive or local storage), transcribe questions into digital text files in their original language (Hindi/English), parse metadata (Subject, Class, Exam Type), and generate standardized question paper PDFs with custom school headers, date writing lines, and diagonal watermarks.

---

## 1. Where to Fill Configurations

### A. Google Drive Paths & Credentials (`config/drive_config.json`)
Open `config/drive_config.json` (copy from `config/drive_config.example.json`) to set your Google Drive input and output folders:
```json
{
  "drive_input_folder_id": "PASTE_YOUR_INPUT_FOLDER_ID_HERE",
  "drive_output_folder_id": "PASTE_YOUR_OUTPUT_FOLDER_ID_HERE",
  "credentials_file": "config/credentials.json",
  "local_raw_dir": "raw_inputs",
  "local_output_dir": "output_pdfs",
  "enabled": true
}
```
- **`drive_input_folder_id`**: The Google Drive Folder where handwritten PDFs are placed.
- **`drive_output_folder_id`**: The Google Drive Folder where generated final PDFs will be automatically uploaded.
- **`credentials_file`**: Place your Google Service Account or OAuth credentials file at `config/credentials.json`.

---

### B. Paper Formatting & Exam Type Preference (`config/format_config.json`)
Open `config/format_config.json`:
```json
{
  "exam_settings": {
    "config_exam_type": "Quarterly"
  }
}
```

#### Exam Type Preference Hierarchy:
1. **1st Preference (Highest)**: Detected inside the input PDF itself (e.g., `त्रैमासिक परीक्षा` / `Quarterly`, `अर्धवार्षिक` / `Half_Yearly`, `वार्षिक` / `Final_Exam`, `Unit_Test`).
2. **2nd Preference**: The fallback value set in `config/format_config.json` (`"config_exam_type": "Quarterly"` / `"Half_Yearly"` / `"Final_Exam"`).
3. **3rd Preference (None given)**: If no exam type is found in the input PDF AND `config_exam_type` is empty (`""` or `"none"`), **no exam type is added**:
   - The PDF name will simply be: `{class}_{subject}.pdf` (e.g. `Class_6TH_Science.pdf`).
   - The paper header will display only the session (`2026-2027`) without an exam title.

---

## 2. Running the Pipeline & CLI Options

From inside `Digitalizing_Papers/`:

### Process Default Input (Auto-detecting from paper):
```powershell
python pipeline.py
```
*(Transcribes `raw_inputs/Sample.pdf`, detects `Quarterly`, and outputs `output_pdfs/Quarterly_Class_6TH_Science.pdf`)*

### Explicitly Override or Rewrite Exam Type:
You can rewrite or force an exam type using `--exam-type`:
- **For Quarterly Exam**:
  ```powershell
  python pipeline.py --exam-type Quarterly
  ```
- **For Half Yearly Exam**:
  ```powershell
  python pipeline.py --exam-type Half_Yearly
  ```
- **For Final / Annual Exam**:
  ```powershell
  python pipeline.py --exam-type Final_Exam
  ```
- **To Omit Exam Type Completely**:
  ```powershell
  python pipeline.py --exam-type none
  ```
  *(Generates `output_pdfs/Class_6TH_Science.pdf`)*

### Run with Google Drive Sync:
```powershell
python pipeline.py --sync-drive
```
### Automated Deduplication & In-Place Updates:
- **Zero Duplicate Outputs**: Output filenames and Google Drive uploads are normalized by canonical paper key (`Exam_Type`, `Class`, `Subject`). Any older filename variants (e.g. `Class_6TH` vs `Class_6`) are automatically replaced, and tabular ledgers are updated in-place.

---

## 3. Directory Layout

```
Digitalizing_Papers/
├── config/
│   ├── config_manager.py     # Central path & configuration manager
│   ├── format_config.json    # Paper styles, watermark, header (Deori) & exam_type setting
│   └── drive_config.json     # Google Drive input & output folder IDs + credentials
│
├── core/
│   ├── drive_syncer.py       # Downloads from Drive input & uploads to Drive output (with deduplication)
│   ├── ocr_extractor.py      # Vision AI transcription with multi-model fallback chain
│   ├── exam_papers_data.py   # Verified high-fidelity transcription dataset for school papers
│   ├── metadata_parser.py    # 3-tier exam type preference & filename formulation
│   └── pdf_generator.py      # High-fidelity browser print & ReportLab fallback
│
├── raw_inputs/               # Incoming handwritten PDFs
├── digitized_texts/          # Extracted .txt files in original Hindi/English format
├── output_pdfs/              # Generated final PDFs (<typeOfExam>_<class>_<subject>.pdf)
│   └── preview_images/       # Visual page previews
├── pipeline.py               # Main CLI runner
└── requirements.txt          # Python dependencies
```
