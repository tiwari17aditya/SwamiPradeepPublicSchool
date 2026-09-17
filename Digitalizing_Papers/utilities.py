"""
Utilities and Diagnostics Tool for Swami Pradeep Public School Pipeline.
Provides system health checks, Google Drive sync inspection, exam paper catalogs, and cache cleaning.
"""

import os
import sys
import argparse
from pathlib import Path
from typing import Dict, Any

BASE_DIR = Path(__file__).resolve().parent
if str(BASE_DIR) not in sys.path:
    sys.path.insert(0, str(BASE_DIR))

from config.config_manager import config_mgr

def check_system_status():
    print("=" * 65)
    print(" SWAMI PRADEEP PUBLIC SCHOOL - PIPELINE STATUS REPORT")
    print("=" * 65)

    # 1. Environment & Dependencies
    print("\n[1] Environment & Engine Diagnostics:")
    print(f"  * Python Version    : {sys.version.split()[0]}")
    try:
        import reportlab
        print(f"  * ReportLab Engine  : v{reportlab.__version__} (OK)")
    except ImportError:
        print(f"  * ReportLab Engine  : NOT INSTALLED")

    try:
        import pypdf
        print(f"  * PyPDF Engine      : v{pypdf.__version__} (OK)")
    except ImportError:
        print(f"  * PyPDF Engine      : NOT INSTALLED")

    # Check Browser Engine for High-Fidelity Rendering
    candidates = [
        r"C:\Program Files\Google\Chrome\Application\chrome.exe",
        r"C:\Program Files (x86)\Google\Chrome\Application\chrome.exe",
        r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe",
        r"C:\Program Files\Microsoft\Edge\Application\msedge.exe"
    ]
    browser = next((p for p in candidates if os.path.exists(p)), None)
    if browser:
        print(f"  * High-Fidelity PDF : Enabled ({Path(browser).stem})")
    else:
        print(f"  * High-Fidelity PDF : Fallback to ReportLab")

    # 2. Google Drive Sync Configuration
    print("\n[2] Google Drive Sync Configuration:")
    drive_cfg = config_mgr.get_drive_config()
    inp_target = drive_cfg.get("drive_input_path") or drive_cfg.get("drive_input_folder_id") or "Not configured"
    out_target = drive_cfg.get("drive_output_path") or drive_cfg.get("drive_output_folder_id") or "Not configured"
    print(f"  * Input Path / ID   : {inp_target}")
    if os.path.exists(inp_target):
        print(f"    |-- Status        : Connected (Local Mounted Drive)")
    else:
        print(f"    |-- Status        : Configured / Standby")

    print(f"  * Output Path / ID  : {out_target}")
    if os.path.exists(out_target):
        print(f"    |-- Status        : Connected (Local Mounted Drive)")
    else:
        print(f"    |-- Status        : Configured / Standby")

    # 3. Exam Papers Storage Summary
    print("\n[3] Digitalized Exam Papers Catalog:")
    out_root = config_mgr.OUTPUT_PDFS_DIR
    pdf_count = 0
    if out_root.exists():
        for year_dir in out_root.iterdir():
            if year_dir.is_dir() and not year_dir.name.startswith("."):
                print(f"  * Academic Session [{year_dir.name}]:")
                for exam_dir in year_dir.iterdir():
                    if exam_dir.is_dir():
                        pdfs = list(exam_dir.glob("*.pdf"))
                        pdf_count += len(pdfs)
                        print(f"    |-- {exam_dir.name:<14} : {len(pdfs)} paper(s)")
                        for p in pdfs:
                            print(f"        -> {p.name}")
    if pdf_count == 0:
        print("  (No production papers in output_pdfs; sample papers stored in sample/)")

    # Sample directory check
    sample_dir = config_mgr.SAMPLE_DIR
    if sample_dir.exists():
        sample_pdfs = list(sample_dir.glob("*.pdf"))
        print(f"\n[4] Isolated Sample Storage: {len(sample_pdfs)} sample file(s) in sample/")

    print("=" * 65)

def clean_cache():
    print("Cleaning cache and temporary files...")
    count = 0
    for p in config_mgr.BASE_DIR.rglob("__pycache__"):
        if p.is_dir():
            import shutil
            shutil.rmtree(p, ignore_errors=True)
            count += 1
    for p in config_mgr.BASE_DIR.rglob("*.tmp*"):
        try:
            p.unlink()
            count += 1
        except Exception:
            pass
    print(f"Cleaned {count} cache directories/files.")

def main():
    parser = argparse.ArgumentParser(description="Swami Pradeep Public School - Utilities & Diagnostics")
    parser.add_argument("--status", "-s", action="store_true", help="Display full system and pipeline status report")
    parser.add_argument("--clean", "-c", action="store_true", help="Clean cache files and bytecode")

    args = parser.parse_args()
    if args.clean:
        clean_cache()
    else:
        check_system_status()

if __name__ == "__main__":
    main()
