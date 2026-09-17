@echo off
title Swami Pradeep Public School - Exam Digitalization Pipeline
echo ============================================================
echo   SWAMI PRADEEP PUBLIC SCHOOL
echo   Exam Paper Digitalization Pipeline
echo ============================================================
echo.

cd /d "%~dp0"
python pipeline.py

echo.
echo ============================================================
echo   Pipeline execution completed!
echo ============================================================
pause
