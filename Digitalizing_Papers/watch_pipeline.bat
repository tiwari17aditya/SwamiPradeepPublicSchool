@echo off
title Swami Pradeep Public School - Continuous Pipeline Watcher
echo ============================================================
echo   SWAMI PRADEEP PUBLIC SCHOOL
echo   Continuous Google Drive Watcher Active
echo ============================================================
echo.
echo Watching for new papers dropped into Google Drive Input Folder...
echo Press Ctrl+C at any time to stop.
echo.

cd /d "%~dp0"
python pipeline.py --watch --interval 30

pause
