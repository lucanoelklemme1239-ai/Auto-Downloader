# 🎥 Auto-Downloader für Videos

Ein benutzerfreundlicher Video-Downloader für Windows 11, der Videos von praktisch jeder Plattform herunterladen kann.

## ✨ Features

- 📥 **Automatischer Download** von Videos von verschiedenen Plattformen
- 🌐 **Breite Plattform-Unterstützung**: YouTube, Vimeo, Facebook, Instagram, TikTok, Twitter/X, Reddit und viele mehr
- 💬 **Interaktive Benutzeroberfläche** im CMD/PowerShell
- 📁 **Flexible Speicherortwahl** - speichern Sie Videos wo immer Sie möchten
- 🎯 **Beste Qualität** - lädt automatisch die beste verfügbare Video- und Audioqualität herunter
- 📊 **Fortschrittsanzeige** - sehen Sie den Download-Fortschritt in Echtzeit
- 🔄 **Mehrfach-Downloads** - laden Sie mehrere Videos nacheinander herunter

## 🚀 Schnellstart

### Voraussetzungen

1. **Python 3.7 oder höher** muss installiert sein
   - Download: [python.org/downloads](https://www.python.org/downloads/)
   - ⚠️ **Wichtig**: Bei der Installation "Add Python to PATH" aktivieren!

2. **ffmpeg** (optional, aber empfohlen für beste Qualität)
   - Download: [ffmpeg.org](https://ffmpeg.org/download.html)
   - Oder mit Chocolatey: `choco install ffmpeg`

### Installation

1. **Repository klonen oder herunterladen**
   ```bash
   git clone https://github.com/IHR-USERNAME/Auto-Downloader.git
   cd Auto-Downloader
   ```

2. **Abhängigkeiten installieren**
   ```bash
   pip install -r requirements.txt
   ```

   Oder manuell:
   ```bash
   pip install yt-dlp
   ```

### 🎯 Verwendung

Es gibt drei Möglichkeiten, den Auto-Downloader zu starten:

#### Option 1: Batch-Script (Empfohlen für CMD)
Doppelklicken Sie auf `download.bat` oder führen Sie im CMD aus:
```cmd
download.bat
```

#### Option 2: PowerShell-Script
Rechtsklick auf `download.ps1` → "Mit PowerShell ausführen"

Oder im PowerShell-Terminal:
```powershell
.\download.ps1
```

#### Option 3: Direkt mit Python
```bash
python video_downloader.py
```

## 📖 Bedienung

1. **Starten Sie das Programm** mit einer der oben genannten Methoden

2. **Video-Link eingeben**
   - Kopieren Sie den Link des Videos, das Sie herunterladen möchten
   - Fügen Sie ihn ein, wenn Sie danach gefragt werden
   - Beispiel: `https://www.youtube.com/watch?v=dQw4w9WgXcQ`

3. **Speicherort wählen**
   - Geben Sie den vollständigen Pfad ein, z.B.: `C:\Users\IhrName\Videos`
   - Oder drücken Sie einfach Enter, um im aktuellen Verzeichnis zu speichern
   - Das Programm kann nicht-existierende Verzeichnisse für Sie erstellen

4. **Download bestätigen**
   - Das Programm zeigt Ihnen Video-Informationen an (Titel, Dauer, Uploader)
   - Bestätigen Sie mit `j` (ja) oder `n` (nein)

5. **Fertig!**
   - Der Download startet und zeigt den Fortschritt an
   - Nach Abschluss können Sie weitere Videos herunterladen

## 🌐 Unterstützte Plattformen

Der Auto-Downloader unterstützt über 1000 verschiedene Websites, darunter:

- **Video-Plattformen**: YouTube, Vimeo, Dailymotion
- **Social Media**: Facebook, Instagram, TikTok, Twitter/X, Reddit
- **Streaming**: Twitch, Livestreams
- **Und viele mehr...**

Eine vollständige Liste finden Sie hier: [yt-dlp supported sites](https://github.com/yt-dlp/yt-dlp/blob/master/supportedsites.md)

## ⚙️ Erweiterte Optionen

### Video-Format und Qualität

Das Programm lädt standardmäßig die beste verfügbare Qualität herunter. Um dies anzupassen, können Sie die Datei `video_downloader.py` bearbeiten:

```python
# In der download_video() Funktion, Zeile ~95
'format': 'bestvideo[ext=mp4]+bestaudio[ext=m4a]/best[ext=mp4]/best',
```

Beispiele für andere Formate:
- `'format': 'worst'` - Niedrigste Qualität (kleinste Dateigröße)
- `'format': 'bestvideo[height<=720]+bestaudio/best[height<=720]'` - Max 720p
- `'format': 'bestaudio/best'` - Nur Audio (für Musik)

### Batch-Download

Um mehrere Videos auf einmal herunterzuladen, erstellen Sie eine Textdatei mit Links (ein Link pro Zeile) und passen Sie das Script an.

## 🛠️ Fehlerbehebung

### "Python ist nicht installiert"
- Installieren Sie Python von [python.org](https://www.python.org/downloads/)
- Stellen Sie sicher, dass "Add Python to PATH" aktiviert ist
- Starten Sie CMD/PowerShell neu nach der Installation

### "yt-dlp ist nicht installiert"
```bash
pip install yt-dlp
```

### "Video konnte nicht heruntergeladen werden"
Mögliche Ursachen:
- Video ist privat oder gelöscht
- Geografische Beschränkungen
- Altersbeschränkungen
- Ungültiger Link

Lösung: Versuchen Sie es mit einem anderen Video oder aktualisieren Sie yt-dlp:
```bash
pip install --upgrade yt-dlp
```

### PowerShell Execution Policy Fehler
Falls PowerShell-Scripts blockiert werden:
```powershell
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
```

## 📝 Hinweise

### Rechtliche Hinweise
- Respektieren Sie Urheberrechte und Nutzungsbedingungen
- Laden Sie nur Videos herunter, für die Sie die Berechtigung haben
- Die Entwickler übernehmen keine Verantwortung für missbräuchliche Nutzung

### Datenschutz
- Dieses Programm sendet keine Daten an externe Server (außer zum Download)
- Alle Downloads erfolgen direkt von der Quellplattform

## 🔄 Updates

Um yt-dlp auf dem neuesten Stand zu halten (empfohlen):
```bash
pip install --upgrade yt-dlp
```

## 🤝 Beitragen

Fehler gefunden oder Verbesserungsvorschläge? Erstellen Sie gerne ein Issue oder Pull Request!

## 📄 Lizenz

Dieses Projekt verwendet yt-dlp, welches unter der Unlicense veröffentlicht ist.

## 🙏 Credits

- [yt-dlp](https://github.com/yt-dlp/yt-dlp) - Der beste Video-Downloader für Python
- [FFmpeg](https://ffmpeg.org/) - Multimedia-Framework

---

**Viel Spaß beim Herunterladen! 🎉**
