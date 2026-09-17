"""
Metadata Parser Module for Swami Pradeep Public School.
Extracts Subject, Class, Exam Type, Time, Marks, and generates standardized filenames.

Exam Type Preference Hierarchy:
1. Explicit Override / Rewrite: (via CLI --exam-type or parameter)
2. First Preference: Detected in input PDF content (e.g. त्रैमासिक -> Quarterly, अर्धवार्षिक -> Half_Yearly, etc.)
3. Second Preference: Configured in format_config.json under 'exam_settings.config_exam_type'
4. Third Preference: If none given or set to '' / 'none', NO exam type is added.

Naming Formats:
- When exam type is present: <typeOfExam>_<class>_<subject>.pdf
- When no exam type is given: <class>_<subject>.pdf
"""

import re
import os
from typing import Dict, Any, Optional
from config.config_manager import config_mgr

class MetadataParser:
    def __init__(self, format_config: Optional[Dict[str, Any]] = None):
        self.config = format_config or config_mgr.get_format_config()
        naming = self.config.get("naming_format", {})
        self.pattern_with_exam = naming.get("pattern_with_exam", "{typeOfExam}_{class}_{subject}.pdf")
        self.pattern_without_exam = naming.get("pattern_without_exam", "{class}_{subject}.pdf")
        self.sanitize_spaces = naming.get("sanitize_spaces", "_")

    def parse(
        self,
        text: str = "",
        filename: str = "",
        default_meta: Optional[Dict[str, Any]] = None,
        config_override_exam: Optional[str] = None
    ) -> Dict[str, Any]:
        """
        Extracts metadata following the user preference hierarchy.
        """
        meta = {
            "school_name": self.config.get("school", {}).get("name", "Swami Pradeep Public School"),
            "exam_type": "",
            "class_name": "General",
            "subject": "General",
            "time_allowed": "2.5 Hours",
            "max_marks": "50",
            "date_line": "Date: ____________________",
            "academic_session": self.config.get("school", {}).get("academic_session", "2026-2027")
        }

        if default_meta:
            meta.update({k: v for k, v in default_meta.items() if v})

        combined_context = f"{filename}\n{text[:2500]}"

        # --- EXAM TYPE RESOLUTION (Hierarchy) ---
        if config_override_exam is not None:
            clean_override = str(config_override_exam).strip()
            if clean_override.lower() in ("none", "null", "no", "blank", "empty", '""', "''"):
                meta["exam_type"] = ""
            else:
                meta["exam_type"] = clean_override.replace(" ", "_")
        else:
            # 1st Preference: Found in input PDF
            detected_exam = self._detect_exam_type_from_text(combined_context)
            if detected_exam:
                meta["exam_type"] = detected_exam
            else:
                # 2nd Preference: Provided in configuration
                cfg_exam = self.config.get("exam_settings", {}).get("config_exam_type", "")
                if cfg_exam and str(cfg_exam).strip().lower() not in ("none", "null", "no", "blank", "empty", ""):
                    meta["exam_type"] = str(cfg_exam).strip().replace(" ", "_")
                else:
                    # 3rd Preference: None given -> do not add any exam type
                    meta["exam_type"] = ""

        # --- CLASS RESOLUTION ---
        class_patterns = [
            r"class\s*[-: ]*\s*([0-9]{1,2}(?:th|st|nd|rd)?|[IVXLCDM]+)",
            r"कक्षा\s*[-: ]*\s*([0-9]{1,2}(?:th|st|nd|rd)?|[IVXLCDM]+)",
            r"(?:std|standard)\s*[-: ]*\s*([0-9]{1,2}(?:th|st|nd|rd)?|[IVXLCDM]+)",
            r"\b(class[-_ ]*[0-9]{1,2})\b",
            r"\b(nursery|lkg|ukg|kg)\b"
        ]
        for pat in class_patterns:
            m = re.search(pat, combined_context, re.IGNORECASE)
            if m:
                val = m.group(1) if m.groups() else m.group(0)
                cleaned_class = re.sub(r"[^0-9a-zA-Z]", "", val)
                if not cleaned_class.lower().startswith("class") and cleaned_class.isdigit():
                    meta["class_name"] = f"Class_{cleaned_class}"
                elif cleaned_class.lower().startswith("class"):
                    meta["class_name"] = cleaned_class.replace("class", "Class_")
                else:
                    meta["class_name"] = f"Class_{cleaned_class.upper()}"
                break

        # --- SUBJECT RESOLUTION ---
        subjects = [
            "Mathematics", "Maths", "गणित",
            "Science", "विज्ञान",
            "Social Science", "Social Studies", "SST", "सामाजिक विज्ञान",
            "English", "अंग्रेजी",
            "Hindi", "हिन्दी", "हिंदी",
            "Sanskrit", "संस्कृत",
            "Computer Science", "Information Technology", "Computer",
            "Physics", "Chemistry", "Biology",
            "Accountancy", "Business Studies", "Economics",
            "History", "Geography", "Political Science"
        ]
        for sub in subjects:
            if re.search(rf"\b{re.escape(sub)}\b", combined_context, re.IGNORECASE):
                norm_map = {
                    "maths": "Mathematics",
                    "गणित": "Mathematics",
                    "विज्ञान": "Science",
                    "sst": "Social_Science",
                    "social studies": "Social_Science",
                    "social science": "Social_Science",
                    "सामाजिक विज्ञान": "Social_Science",
                    "english": "English",
                    "अंग्रेजी": "English",
                    "hindi": "Hindi",
                    "हिन्दी": "Hindi",
                    "हिंदी": "Hindi",
                    "sanskrit": "Sanskrit",
                    "संस्कृत": "Sanskrit",
                    "computer": "Computer_Science",
                    "computer science": "Computer_Science",
                    "it": "Information_Technology",
                    "information technology": "Information_Technology"
                }
                meta["subject"] = norm_map.get(sub.lower(), sub.replace(" ", "_"))
                break

        # --- MAXIMUM MARKS ---
        marks_match = re.search(r"(?:max(?:imum)?\s*marks|m\.?m\.?|पूर्णांक)\s*[:=-]?\s*(\d{2,3})", combined_context, re.IGNORECASE)
        if marks_match:
            meta["max_marks"] = marks_match.group(1)

        # --- TIME ALLOWED ---
        time_match = re.search(r"(?:time(?:\s*allowed)?|समय)\s*[:=-]?\s*([0-9\.]+\s*(?:hrs?|hours?|min|minutes?|घंटे))", combined_context, re.IGNORECASE)
        if time_match:
            meta["time_allowed"] = time_match.group(1).strip()

        meta["sanitized_filename"] = self.generate_filename(meta)
        return meta

    def _detect_exam_type_from_text(self, context: str) -> Optional[str]:
        """
        Detects examination type from handwritten or printed text.
        """
        exam_patterns = [
            (r"(त्रैमासिक\s*(?:परीक्षा)?|quarterly\s*(?:exam|examination)?)", "Quarterly"),
            (r"(अर्धवार्षिक\s*(?:परीक्षा)?|half\s*yearly|half-yearly|mid\s*term|midterm)", "Half_Yearly"),
            (r"(वार्षिक\s*(?:परीक्षा)?|annual\s*(?:exam|examination)?|final\s*(?:exam|examination)?)", "Final_Exam"),
            (r"(pre[- ]*board|preboard)", "Pre_Board"),
            (r"(periodic\s*test\s*[-_ ]*(\d+)|pt\s*[-_ ]*(\d+)|आवधिक\s*परीक्षा\s*[-_ ]*(\d+)?)", "Periodic_Test"),
            (r"(unit\s*test\s*[-_ ]*(\d+)|ut\s*[-_ ]*(\d+)|इकाई\s*परीक्षा\s*[-_ ]*(\d+)?)", "Unit_Test"),
            (r"(class\s*test|mock\s*test)", "Class_Test")
        ]

        for pat, standard_name in exam_patterns:
            m = re.search(pat, context, re.IGNORECASE)
            if m:
                digits = [g for g in m.groups() if g and g.isdigit()]
                if digits:
                    return f"{standard_name}_{digits[0]}"
                return standard_name

        return None

    def generate_filename(self, meta: Dict[str, Any]) -> str:
        """
        Formats filename according to:
        - If exam type given: <typeOfExam>_<class>_<subject>.pdf
        - If NO exam type given: <class>_<subject>.pdf
        """
        def clean(s: str) -> str:
            s = re.sub(r"[^\w\d]", "_", str(s))
            return re.sub(r"_+", "_", s).strip("_")

        exam = clean(meta.get("exam_type", ""))
        cls = clean(meta.get("class_name", "Class")) or "Class"
        subj = clean(meta.get("subject", "Subject")) or "Subject"

        if exam:
            return f"{exam}_{cls}_{subj}.pdf"
        else:
            return f"{cls}_{subj}.pdf"
