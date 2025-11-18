# Auto-Downloader für Videos - PowerShell Starter
# UTF-8 Encoding für korrekte Darstellung
[Console]::OutputEncoding = [System.Text.Encoding]::UTF8

Write-Host ""
Write-Host "========================================" -ForegroundColor Cyan
Write-Host "Auto-Downloader für Videos" -ForegroundColor Cyan
Write-Host "========================================" -ForegroundColor Cyan
Write-Host ""

# Überprüfe ob Python installiert ist
try {
    $pythonVersion = python --version 2>&1
    Write-Host "Python gefunden: $pythonVersion" -ForegroundColor Green
    Write-Host ""
}
catch {
    Write-Host "FEHLER: Python ist nicht installiert!" -ForegroundColor Red
    Write-Host ""
    Write-Host "Bitte installieren Sie Python von: https://www.python.org/downloads/" -ForegroundColor Yellow
    Write-Host "Stellen Sie sicher, dass Sie bei der Installation 'Add Python to PATH' auswählen!" -ForegroundColor Yellow
    Write-Host ""
    Read-Host "Drücken Sie Enter zum Beenden"
    exit 1
}

# Überprüfe ob yt-dlp installiert ist
python -c "import yt_dlp" 2>$null
if ($LASTEXITCODE -ne 0) {
    Write-Host "yt-dlp ist nicht installiert. Installiere Abhängigkeiten..." -ForegroundColor Yellow
    Write-Host ""

    if (Test-Path "requirements.txt") {
        pip install -r requirements.txt
    }
    else {
        pip install yt-dlp
    }

    Write-Host ""
    Write-Host "Installation abgeschlossen!" -ForegroundColor Green
    Write-Host ""
}

# Starte das Python-Script
python video_downloader.py

Write-Host ""
Read-Host "Drücken Sie Enter zum Beenden"
