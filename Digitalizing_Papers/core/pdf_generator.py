"""
PDF Generator Module for Swami Pradeep Public School.
Builds publication-quality school examination papers according to format_config.json.
Features:
- Official School Header with session & CBSE affiliation
- Metadata block: Class, Subject, Time Allowed, Maximum Marks, Roll No.
- Dedicated Date line with a blank line for writing: Date: ____________________
- Diagonal Watermark on every page: 'Swami Pradeep Public School' (top-left to bottom-right)
- Clear sections, numbered questions, and right-aligned marks
- Dual-engine architecture: High-fidelity browser print engine with ReportLab fallback
"""

import os
import sys
import math
import subprocess
from pathlib import Path
from typing import Dict, Any, List, Optional

from config.config_manager import config_mgr

class ExamPaperPDFGenerator:
    def __init__(self, config: Optional[Dict[str, Any]] = None):
        self.config = config or config_mgr.get_format_config()
        self.browser_path = self._find_browser_engine()

    def _find_browser_engine(self) -> Optional[str]:
        candidates = [
            r"C:\Program Files\Google\Chrome\Application\chrome.exe",
            r"C:\Program Files (x86)\Google\Chrome\Application\chrome.exe",
            r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe",
            r"C:\Program Files\Microsoft\Edge\Application\msedge.exe"
        ]
        for p in candidates:
            if os.path.exists(p):
                return p
        return None

    def generate_pdf(
        self,
        output_path: str,
        metadata: Dict[str, Any],
        sections: List[Dict[str, Any]],
        general_instructions: Optional[List[str]] = None
    ) -> str:
        """
        Renders the exam paper PDF using high-fidelity browser engine (flawless Hindi & English ligatures)
        or falls back to ReportLab.
        """
        out_file = Path(output_path).resolve()
        out_file.parent.mkdir(parents=True, exist_ok=True)

        if self.browser_path:
            try:
                return self._generate_html_pdf(out_file, metadata, sections, general_instructions)
            except Exception as e:
                print(f"[PDFGenerator] High-fidelity engine warning: {e}. Falling back to ReportLab.")

        return self._generate_reportlab_pdf(out_file, metadata, sections, general_instructions)

    def _generate_html_pdf(
        self,
        out_file: Path,
        metadata: Dict[str, Any],
        sections: List[Dict[str, Any]],
        general_instructions: Optional[List[str]] = None
    ) -> str:
        school = self.config.get("school", {})
        school_name = school.get("name", "SWAMI PRADEEP PUBLIC SCHOOL")
        affiliation = school.get("affiliation_text", "Affiliated to CBSE, New Delhi")
        session = metadata.get("academic_session", school.get("academic_session", "2026-2027"))

        exam_type_clean = metadata.get("exam_type", "Examination").replace("_", " ").title()
        exam_title = f"{exam_type_clean} ({session})"

        class_name = metadata.get("class_name", "Class").replace("_", " ")
        subject = metadata.get("subject", "Subject").replace("_", " ")
        time_allowed = metadata.get("time_allowed", "2.5 Hours")
        max_marks = metadata.get("max_marks", "50")

        watermark_cfg = self.config.get("watermark", {})
        wm_text = watermark_cfg.get("text", "Swami Pradeep Public School")
        wm_angle = watermark_cfg.get("angle", -40.0)
        wm_opacity = watermark_cfg.get("opacity", 0.11)

        instructions = general_instructions or self.config.get("general_instructions", {}).get("default_instructions", [])

        # Build HTML
        html_parts = [
            "<!DOCTYPE html>",
            "<html lang='hi'>",
            "<head>",
            "<meta charset='utf-8'/>",
            "<title>Swami Pradeep Public School Exam Paper</title>",
            "<style>",
            "@page {",
            "    size: A4;",
            "    margin: 14mm 16mm 14mm 16mm;",
            "}",
            "* { box-sizing: border-box; }",
            "body {",
            "    font-family: 'Segoe UI', 'Nirmala UI', 'Arial', sans-serif;",
            "    color: #1a202c;",
            "    margin: 0;",
            "    padding: 0;",
            "    background: #fff;",
            "    font-size: 13.5px;",
            "    line-height: 1.5;",
            "}",
            ".watermark {",
            "    position: fixed;",
            "    top: 50%;",
            "    left: 50%;",
            f"   transform: translate(-50%, -50%) rotate({wm_angle}deg);",
            "    font-size: 54px;",
            "    font-weight: 800;",
            f"   color: rgba(140, 150, 165, {wm_opacity});",
            "    white-space: nowrap;",
            "    z-index: -1000;",
            "    pointer-events: none;",
            "    letter-spacing: 2px;",
            "    text-transform: capitalize;",
            "}",
            ".school-header {",
            "    text-align: center;",
            "    border-bottom: 2px solid #1a365d;",
            "    padding-bottom: 6px;",
            "    margin-bottom: 10px;",
            "}",
            ".school-name {",
            "    font-size: 22px;",
            "    font-weight: 800;",
            "    color: #1a365d;",
            "    letter-spacing: normal;",
            "    word-spacing: normal;",
            "    text-transform: uppercase;",
            "    margin-bottom: 2px;",
            "}",
            ".school-sub {",
            "    font-size: 12px;",
            "    color: #4a5568;",
            "    font-weight: 500;",
            "    margin-bottom: 4px;",
            "}",
            ".exam-title {",
            "    font-size: 16px;",
            "    font-weight: 700;",
            "    color: #2b6cb0;",
            "    margin-top: 2px;",
            "}",
            ".meta-table {",
            "    width: 100%;",
            "    border-collapse: collapse;",
            "    margin-bottom: 10px;",
            "}",
            ".meta-table td {",
            "    padding: 3px 6px;",
            "    font-size: 13px;",
            "    color: #2d3748;",
            "}",
            ".meta-table .meta-label {",
            "    font-weight: 700;",
            "    color: #1a202c;",
            "}",
            ".meta-line {",
            "    display: inline-block;",
            "    border-bottom: 1px solid #4a5568;",
            "    min-width: 140px;",
            "    height: 14px;",
            "    vertical-align: middle;",
            "}",
            ".instructions-box {",
            "    border: 1px solid #cbd5e0;",
            "    background: #f7fafc;",
            "    border-radius: 4px;",
            "    padding: 6px 12px;",
            "    margin-bottom: 14px;",
            "}",
            ".instructions-title {",
            "    font-size: 12px;",
            "    font-weight: 700;",
            "    color: #2d3748;",
            "    margin-bottom: 3px;",
            "}",
            ".instructions-list {",
            "    margin: 0;",
            "    padding-left: 18px;",
            "    font-size: 11.5px;",
            "    color: #4a5568;",
            "}",
            ".instructions-list li {",
            "    margin-bottom: 2px;",
            "}",
            ".section-heading {",
            "    text-align: center;",
            "    font-size: 14px;",
            "    font-weight: 700;",
            "    color: #1a365d;",
            "    background: #edf2f7;",
            "    padding: 4px 0;",
            "    margin: 14px 0 8px 0;",
            "    border-radius: 3px;",
            "    letter-spacing: 0.5px;",
            "}",
            ".question-item {",
            "    display: flex;",
            "    justify-content: space-between;",
            "    align-items: flex-start;",
            "    margin-bottom: 8px;",
            "    page-break-inside: avoid;",
            "}",
            ".question-left {",
            "    display: flex;",
            "    flex: 1;",
            "}",
            ".question-num {",
            "    font-weight: 700;",
            "    min-width: 30px;",
            "    color: #1a202c;",
            "}",
            ".question-content {",
            "    flex: 1;",
            "    color: #2d3748;",
            "}",
            ".question-marks {",
            "    font-weight: 700;",
            "    min-width: 45px;",
            "    text-align: right;",
            "    color: #4a5568;",
            "    padding-left: 10px;",
            "}",
            ".or-separator {",
            "    text-align: center;",
            "    font-weight: 700;",
            "    color: #718096;",
            "    margin: 4px 0;",
            "    font-size: 12px;",
            "}",
            "</style>",
            "</head>",
            "<body>",
            f"<div class='watermark'>{wm_text}</div>",
            "<div class='school-header'>",
            f"    <div class='school-name'>{school_name}</div>",
            f"    <div class='school-sub'>{affiliation}</div>",
            f"    <div class='exam-title'>{exam_title}</div>",
            "</div>",
            "<table class='meta-table'>",
            "    <tr>",
            f"        <td><span class='meta-label'>Class:</span> {class_name}</td>",
            f"        <td style='text-align: right;'><span class='meta-label'>Time Allowed:</span> {time_allowed}</td>",
            "    </tr>",
            "    <tr>",
            f"        <td><span class='meta-label'>Subject:</span> {subject}</td>",
            f"        <td style='text-align: right;'><span class='meta-label'>Maximum Marks:</span> {max_marks}</td>",
            "    </tr>",
            "    <tr>",
            "        <td><span class='meta-label'>Date:</span> <span class='meta-line'></span></td>",
            "        <td style='text-align: right;'><span class='meta-label'>Roll No.:</span> <span class='meta-line' style='min-width: 100px;'></span></td>",
            "    </tr>",
            "</table>"
        ]

        # Instructions
        if instructions:
            html_parts.append("<div class='instructions-box'>")
            html_parts.append("    <div class='instructions-title'>सामान्य निर्देश (General Instructions):</div>")
            html_parts.append("    <ol class='instructions-list'>")
            for instr in instructions:
                clean_in = instr.strip()
                if clean_in:
                    html_parts.append(f"        <li>{clean_in}</li>")
            html_parts.append("    </ol>")
            html_parts.append("</div>")

        # Sections and Questions
        for sec in sections:
            sec_title = sec.get("title", "")
            if sec_title:
                html_parts.append(f"<div class='section-heading'>{sec_title}</div>")

            for q in sec.get("questions", []):
                q_num = str(q.get("number", "")).strip()
                q_text = q.get("text", "").strip()
                q_marks = str(q.get("marks", "")).strip()
                is_or = q.get("is_or_choice", False)

                if is_or:
                    html_parts.append("<div class='or-separator'>--- अथवा / OR ---</div>")

                marks_badge = f"[{q_marks}]" if q_marks else ""

                html_parts.append("<div class='question-item'>")
                html_parts.append("    <div class='question-left'>")
                html_parts.append(f"        <div class='question-num'>{q_num}</div>")
                html_parts.append(f"        <div class='question-content'>{q_text}</div>")
                html_parts.append("    </div>")
                html_parts.append(f"    <div class='question-marks'>{marks_badge}</div>")
                html_parts.append("</div>")

        html_parts.extend(["</body>", "</html>"])

        # Save temporary HTML and render via headless browser
        temp_html_path = out_file.parent / f".tmp_{out_file.stem}.html"
        with open(temp_html_path, "w", encoding="utf-8") as f:
            f.write("\n".join(html_parts))

        cmd = [
            self.browser_path,
            "--headless=new",
            "--disable-gpu",
            "--no-pdf-header-footer",
            f"--print-to-pdf={str(out_file)}",
            str(temp_html_path)
        ]

        subprocess.run(cmd, check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

        if temp_html_path.exists():
            try:
                temp_html_path.unlink()
            except Exception:
                pass

        return str(out_file)

    def _generate_reportlab_pdf(
        self,
        out_file: Path,
        metadata: Dict[str, Any],
        sections: List[Dict[str, Any]],
        general_instructions: Optional[List[str]] = None
    ) -> str:
        """ReportLab pure Python fallback."""
        from reportlab.lib.pagesizes import A4
        from reportlab.lib import colors
        from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
        from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, KeepTogether, HRFlowable
        from reportlab.pdfgen import canvas
        from reportlab.pdfbase import pdfmetrics
        from reportlab.pdfbase.ttfonts import TTFont

        class RLNumberedCanvas(canvas.Canvas):
            def __init__(self, *args, **kwargs):
                self.wm_config = kwargs.pop("wm_config", {})
                self.school_name = kwargs.pop("school_name", "Swami Pradeep Public School")
                super().__init__(*args, **kwargs)
                self._saved_page_states = []

            def showPage(self):
                self._saved_page_states.append(dict(self.__dict__))
                self._startPage()

            def save(self):
                num_pages = len(self._saved_page_states)
                for state in self._saved_page_states:
                    self.__dict__.update(state)
                    self.draw_wm()
                    self.draw_page_num(num_pages)
                    canvas.Canvas.showPage(self)
                canvas.Canvas.save(self)

            def draw_wm(self):
                self.saveState()
                w, h = self._pagesize
                self.setFillColor(colors.Color(0.70, 0.70, 0.70, alpha=0.12))
                self.setFont("Helvetica-Bold", 42)
                self.translate(w / 2.0, h / 2.0)
                self.rotate(-45)
                self.drawCentredString(0, 0, self.school_name)
                self.restoreState()

            def draw_page_num(self, total):
                self.saveState()
                self.setFont("Helvetica", 9)
                self.setFillColor(colors.HexColor("#4A5568"))
                self.drawCentredString(self._pagesize[0] / 2.0, 20, f"Page {self._pageNumber} of {total}")
                self.restoreState()

        # Register Nirmala if available
        font_name = "Helvetica"
        if os.path.exists("C:/Windows/Fonts/Nirmala.ttc"):
            try:
                pdfmetrics.registerFont(TTFont("Nirmala", "C:/Windows/Fonts/Nirmala.ttc", subfontIndex=0))
                font_name = "Nirmala"
            except Exception:
                pass

        doc = SimpleDocTemplate(str(out_file), pagesize=A4, leftMargin=40, rightMargin=40, topMargin=36, bottomMargin=40)
        styles = getSampleStyleSheet()
        p_title = ParagraphStyle("T", fontName=font_name, fontSize=18, alignment=1, textColor=colors.HexColor("#1A365D"))
        p_body = ParagraphStyle("B", fontName=font_name, fontSize=10, textColor=colors.HexColor("#1A202C"))

        story = [
            Paragraph(f"<b>{metadata.get('school_name', 'SWAMI PRADEEP PUBLIC SCHOOL')}</b>", p_title),
            Spacer(1, 15)
        ]
        for sec in sections:
            for q in sec.get("questions", []):
                story.append(Paragraph(f"{q.get('number')} {q.get('text')}", p_body))
                story.append(Spacer(1, 4))

        doc.build(story, canvasmaker=RLNumberedCanvas)
        return str(out_file)
