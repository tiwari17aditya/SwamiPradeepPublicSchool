"""
Google Drive Sync Module for Swami Pradeep Public School.
Supports both:
1. Local mounted Google Drive desktop folders (e.g. 'G:/My Drive/...')
2. Cloud Google Drive API (OAuth / Service Account)

Features:
- Downloads incoming handwritten papers from Drive Input Folder into raw_inputs/
- Uploads generated PDFs into hierarchical Drive Output Folders:
  <Output Folder>/<Year>/<Quarterly | Half-Yearly | Final | General>/<pdf_name>
"""

import os
import io
import shutil
import logging
from pathlib import Path
from typing import List, Dict, Any, Optional

from config.config_manager import (
    config_mgr,
    get_exam_subfolder,
    get_year_folder,
    get_class_subfolder,
    normalize_paper_key,
    parse_paper_key_from_filename
)

logger = logging.getLogger("DriveSyncer")

class DriveSyncer:
    def __init__(self, config_path: str = "config/drive_config.json", base_dir: Optional[str] = None):
        self.config_mgr = config_mgr
        self.base_dir = Path(base_dir or config_mgr.BASE_DIR).resolve()
        self.config = self.config_mgr.get_drive_config()

        raw_rel = self.config.get("local_raw_dir", "raw_inputs")
        self.local_raw_dir = (self.base_dir / raw_rel).resolve()
        self.local_raw_dir.mkdir(parents=True, exist_ok=True)

        out_rel = self.config.get("local_output_dir", "output_pdfs")
        self.local_output_dir = (self.base_dir / out_rel).resolve()
        self.local_output_dir.mkdir(parents=True, exist_ok=True)

        self.state_file = self.local_raw_dir / ".sync_state.json"
        self._service = None

    def _get_input_target(self) -> Optional[str]:
        return (
            self.config.get("drive_input_path") or
            self.config.get("drive_input_folder_id") or
            self.config.get("drive_folder_id")
        )

    def _get_output_target(self) -> Optional[str]:
        return (
            self.config.get("drive_output_path") or
            self.config.get("drive_output_folder_id")
        )

    def sync(self) -> List[str]:
        """
        Synchronizes handwritten PDFs from Google Drive Input Folder into local raw_inputs/.
        """
        target = self._get_input_target()
        if not target:
            logger.info("[DriveSyncer] Drive input folder not set. Using local raw_inputs/ directly.")
            return self.get_local_raw_files()

        # Check if target is a local mounted Google Drive directory
        target_path = Path(target)
        if target_path.exists() and target_path.is_dir():
            logger.info(f"[DriveSyncer] Scanning local Google Drive input folder: {target_path}")
            synced = []
            for src_pdf in target_path.glob("*.pdf"):
                dest_pdf = self.local_raw_dir / src_pdf.name
                # Copy if not present or modified
                if not dest_pdf.exists() or src_pdf.stat().st_mtime > dest_pdf.stat().st_mtime:
                    shutil.copy2(src_pdf, dest_pdf)
                    logger.info(f"[DriveSyncer] Synced from Drive to local: {src_pdf.name}")
                synced.append(str(dest_pdf))
            return synced

        # Fallback to Google Drive API if target is a cloud folder ID
        return self._sync_via_api(target)

    def upload_output(self, local_pdf_path: str, metadata: Dict[str, Any]) -> Optional[str]:
        """
        Uploads generated PDF to Google Drive Output Folder under hierarchical structure:
        <Drive Output>/<Year>/<Quarterly | Half-Yearly | Final | General>/<pdf_name>
        Always removes any stale variant of the same paper to prevent duplicates.
        """
        target = self._get_output_target()
        if not target:
            return None

        pdf_file = Path(local_pdf_path)
        if not pdf_file.exists():
            return None

        year_folder = get_year_folder(metadata, config_mgr.get_format_config().get("school", {}).get("academic_session", "2026-2027"))
        exam_subfolder = get_exam_subfolder(metadata.get("exam_type", ""))
        class_subfolder = get_class_subfolder(metadata.get("class_name", ""))

        target_path = Path(target)
        if target_path.exists() and target_path.is_dir():
            # Build hierarchical folder: <Drive Output>/<Year>/<ExamType>/<Class>/
            dest_dir = target_path / year_folder / exam_subfolder / class_subfolder
            dest_dir.mkdir(parents=True, exist_ok=True)

            # Deduplication: remove any existing stale variant of the same paper
            current_key = normalize_paper_key(
                metadata.get("exam_type", ""),
                metadata.get("class_name", ""),
                metadata.get("subject", "")
            )
            for existing_pdf in dest_dir.glob("*.pdf"):
                if existing_pdf.name != pdf_file.name:
                    if parse_paper_key_from_filename(existing_pdf.name) == current_key:
                        existing_pdf.unlink(missing_ok=True)
                        logger.info(f"[DriveSyncer] Removed stale duplicate in Google Drive: {existing_pdf.name}")

            dest_file = dest_dir / pdf_file.name
            shutil.copy2(pdf_file, dest_file)
            logger.info(f"[DriveSyncer] Updated in Google Drive hierarchy: {dest_file}")
            return str(dest_file)

        # Fallback to Google Drive API
        return self._upload_via_api(pdf_file, target, year_folder, exam_subfolder)

    def _sync_via_api(self, folder_id: str) -> List[str]:
        service = self._get_api_service()
        if not service:
            return self.get_local_raw_files()

        try:
            from googleapiclient.http import MediaIoBaseDownload
            query = f"'{folder_id}' in parents and trashed = false and mimeType = 'application/pdf'"
            results = service.files().list(q=query, fields="files(id, name, md5Checksum)").execute()
            files = results.get("files", [])

            downloaded = []
            for item in files:
                local_path = self.local_raw_dir / item["name"]
                request = service.files().get_media(fileId=item["id"])
                with io.FileIO(str(local_path), "wb") as fh:
                    dl = MediaIoBaseDownload(fh, request)
                    done = False
                    while not done:
                        _, done = dl.next_chunk()
                downloaded.append(str(local_path))
            return downloaded
        except Exception as e:
            logger.error(f"[DriveSyncer API] Error: {e}")
            return self.get_local_raw_files()

    def _upload_via_api(self, pdf_file: Path, base_folder_id: str, year_folder: str, exam_subfolder: str) -> Optional[str]:
        service = self._get_api_service()
        if not service:
            return None
        try:
            from googleapiclient.http import MediaFileUpload
            # Create or find Year folder, then Exam folder, then upload
            year_id = self._get_or_create_drive_folder(service, year_folder, base_folder_id)
            exam_id = self._get_or_create_drive_folder(service, exam_subfolder, year_id)

            file_metadata = {"name": pdf_file.name, "parents": [exam_id]}
            media = MediaFileUpload(str(pdf_file), mimetype="application/pdf", resumable=True)
            res = service.files().create(body=file_metadata, media_body=media, fields="id, webViewLink").execute()
            return res.get("webViewLink")
        except Exception as e:
            logger.error(f"[DriveSyncer API] Upload error: {e}")
            return None

    def _get_or_create_drive_folder(self, service, folder_name: str, parent_id: str) -> str:
        q = f"name = '{folder_name}' and '{parent_id}' in parents and mimeType = 'application/vnd.google-apps.folder' and trashed = false"
        res = service.files().list(q=q, fields="files(id, name)").execute()
        files = res.get("files", [])
        if files:
            return files[0]["id"]
        meta = {
            "name": folder_name,
            "mimeType": "application/vnd.google-apps.folder",
            "parents": [parent_id]
        }
        folder = service.files().create(body=meta, fields="id").execute()
        return folder["id"]

    def _get_api_service(self):
        if self._service is not None:
            return self._service
        creds_path = self.base_dir / self.config.get("credentials_file", "config/credentials.json")
        if not creds_path.exists():
            return None
        try:
            from googleapiclient.discovery import build
            from google.oauth2 import service_account
            creds = service_account.Credentials.from_service_account_file(
                str(creds_path), scopes=["https://www.googleapis.com/auth/drive"]
            )
            self._service = build("drive", "v3", credentials=creds)
            return self._service
        except Exception:
            return None

    def get_local_raw_files(self) -> List[str]:
        return [str(p) for p in self.local_raw_dir.glob("*.pdf") if not p.name.startswith(".")]
