@echo off
chcp 65001 >nul
REM Auto-Downloader für Videos - Windows Batch Starter

title Auto-Downloader für Videos

echo.
echo ========================================
echo Auto-Downloader für Videos
echo ========================================
echo.

REM Überprüfe ob Python installiert ist
python --version >nul 2>&1
if errorlevel 1 (
    echo FEHLER: Python ist nicht installiert!
    echo.
    echo Bitte installieren Sie Python von: https://www.python.org/downloads/
    echo Stellen Sie sicher, dass Sie bei der Installation "Add Python to PATH" auswählen!
    echo.
    pause
    exit /b 1
)

echo Python gefunden:
python --version
echo.

REM Überprüfe ob yt-dlp installiert ist
python -c "import yt_dlp" >nul 2>&1
if errorlevel 1 (
    echo yt-dlp ist nicht installiert. Installiere Abhängigkeiten...
    echo.

    if exist requirements.txt (
        pip install -r requirements.txt
    ) else (
        pip install yt-dlp
    )

    echo.
    echo Installation abgeschlossen!
    echo.
)

REM Starte das Python-Script
python video_downloader.py

pause
