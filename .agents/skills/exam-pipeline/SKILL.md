---
name: exam-pipeline
description: >-
  Operational guide for the Swami Pradeep Public School Exam Paper Digitalization Pipeline.
  Use when running digitalization, overriding exam types, managing Google Drive sync,
  troubleshooting typography or watermarks, or formatting paper layouts.
---

# Exam Pipeline Operational Guide

## Core Commands
- **Run Standard Pipeline (Auto-sync & process):**
  ```powershell
  python Digitalizing_Papers/pipeline.py
  ```
- **Process Specific Input Paper:**
  ```powershell
  python Digitalizing_Papers/pipeline.py --input "path/to/paper.pdf"
  ```
- **Override / Rewrite Exam Type:**
  ```powershell
  python Digitalizing_Papers/pipeline.py --exam-type Quarterly
  python Digitalizing_Papers/pipeline.py --exam-type Half_Yearly
  python Digitalizing_Papers/pipeline.py --exam-type Final_Exam
  python Digitalizing_Papers/pipeline.py --exam-type none
  ```
- **Continuous Background Watch Mode:**
  ```powershell
  python Digitalizing_Papers/pipeline.py --watch --interval 30
  ```

## Output Hierarchy
All output PDFs are placed into a 4-level class hierarchy:
`output_pdfs/<Academic_Year>/<Quarterly | Half-Yearly | Final | General>/<Class>/<filename>.pdf`
And mirrored to Google Drive Output folder:
`<Drive_Output>/<Academic_Year>/<Quarterly | Half-Yearly | Final | General>/<Class>/<filename>.pdf`

## Formatting Configurations (`config/format_config.json`)
- School Name: `school.name`
- Watermark Text & Angle: `watermark.text`, `watermark.angle` (-40 degrees for top-left to bottom-right)
- Margins: `page_layout.margin_*`
- Default Exam Type: `exam_settings.config_exam_type`
