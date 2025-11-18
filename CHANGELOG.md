# Changelog

Alle wichtigen Änderungen an diesem Projekt werden in dieser Datei dokumentiert.

Das Format basiert auf [Keep a Changelog](https://keepachangelog.com/de/1.0.0/),
und dieses Projekt folgt [Semantic Versioning](https://semver.org/lang/de/).

---

## [1.0.0] - 2025-11-18

### 🎉 Erste offizielle Version

#### Hinzugefügt
- **Haupt-Script** (`video_downloader.py`)
  - Interaktive Benutzeroberfläche auf Deutsch
  - Unterstützung für 1000+ Video-Plattformen via yt-dlp
  - Video-Link Eingabe mit Validierung
  - Flexible Speicherortwahl mit Verzeichniserstellung
  - Echtzeit-Fortschrittsanzeige (Prozent, Geschwindigkeit, ETA)
  - Video-Informationsanzeige (Titel, Dauer, Uploader)
  - Download-Bestätigung vor Start
  - Mehrfach-Downloads nacheinander möglich
  - Automatische Auswahl der besten Video- und Audioqualität
  - MP4-Format als Standard
  - Fehlerbehandlung und aussagekräftige Fehlermeldungen

- **Windows Starter-Scripts**
  - `download.bat` - Batch-Script für CMD
    - Automatische Python-Überprüfung
    - Automatische yt-dlp Installation falls nötig
    - UTF-8 Encoding für deutsche Umlaute
  - `download.ps1` - PowerShell-Script
    - Farbige Ausgabe
    - Verbesserte Fehlerbehandlung
    - UTF-8 Support

- **Dokumentation**
  - `README.md` - Ausführliche Anleitung auf Deutsch
    - Features-Übersicht
    - Installationsanleitung
    - Bedienungsanleitung
    - Liste unterstützter Plattformen
    - Fehlerbehebung
    - Erweiterte Optionen
  - `BEISPIELE.md` - Erweiterte Beispiele
    - Verschiedene Nutzungsszenarien
    - Code-Beispiele für Anpassungen
    - Tipps und Tricks
    - Format-Optionen
    - Dateinamen-Anpassungen

- **Konfiguration**
  - `requirements.txt` - Python-Abhängigkeiten
  - `.gitignore` - Git-Konfiguration für Python-Projekte

#### Unterstützte Plattformen
- YouTube, YouTube Music
- Instagram (Posts, Reels, Stories)
- TikTok
- Facebook (Videos, Watch)
- Twitter/X
- Reddit
- Vimeo
- Dailymotion
- Twitch (VODs, Clips)
- und über 1000 weitere Websites

#### Technische Details
- Python 3.7+ Unterstützung
- yt-dlp Integration
- ffmpeg Support (optional)
- Windows 11 optimiert
- UTF-8 Encoding für deutsche Zeichen
- Robuste Fehlerbehandlung

---

## Versionshistorie

- **[1.0.0]** - 2025-11-18 - Erste offizielle Version

---

## Kommende Features

### Geplant für v1.1.0
- [ ] GUI (Grafische Benutzeroberfläche)
- [ ] Batch-Download aus Textdatei
- [ ] Download-Warteschlange
- [ ] Konfigurationsdatei für Standard-Einstellungen
- [ ] Automatische Untertitel-Downloads
- [ ] Download-Historie
- [ ] Fortschrittsbalken für Playlists

### Überlegungen für spätere Versionen
- [ ] Drag & Drop Support
- [ ] Browser-Extension
- [ ] Automatische Format-Konvertierung
- [ ] Cloud-Upload nach Download
- [ ] Scheduler für automatische Downloads
- [ ] Mehrsprachige Oberfläche (Englisch, etc.)

---

## Mitwirken

Fehler gefunden oder Verbesserungsvorschläge?
- Erstellen Sie ein Issue auf GitHub
- Reichen Sie einen Pull Request ein
- Diskutieren Sie neue Features in den Discussions

---

*Für detaillierte Release Notes siehe RELEASE_NOTES_v1.0.0.md*
