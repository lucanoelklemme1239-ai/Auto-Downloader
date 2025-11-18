# Beispiele für die Nutzung des Auto-Downloaders

## Grundlegende Nutzung

### Beispiel 1: YouTube Video herunterladen
```
Link: https://www.youtube.com/watch?v=dQw4w9WgXcQ
Speicherort: C:\Users\MeinName\Videos\YouTube
```

### Beispiel 2: Instagram Video herunterladen
```
Link: https://www.instagram.com/p/XXXXXXXXX/
Speicherort: C:\Users\MeinName\Videos\Instagram
```

### Beispiel 3: TikTok Video herunterladen
```
Link: https://www.tiktok.com/@username/video/1234567890
Speicherort: C:\Users\MeinName\Videos\TikTok
```

## Erweiterte Beispiele

### Nur Audio herunterladen (z.B. für Musik)

Bearbeiten Sie `video_downloader.py` und ändern Sie Zeile 95:
```python
# Original:
'format': 'bestvideo[ext=mp4]+bestaudio[ext=m4a]/best[ext=mp4]/best',

# Geändert (nur Audio):
'format': 'bestaudio/best',
```

### Maximale Auflösung begrenzen (z.B. 720p)

```python
# Original:
'format': 'bestvideo[ext=mp4]+bestaudio[ext=m4a]/best[ext=mp4]/best',

# Geändert (max 720p):
'format': 'bestvideo[height<=720]+bestaudio/best[height<=720]',
```

### Bestimmtes Dateiformat erzwingen

```python
# Für WebM:
'format': 'bestvideo[ext=webm]+bestaudio[ext=webm]/best[ext=webm]',

# Für MKV:
'format': 'bestvideo+bestaudio',
'merge_output_format': 'mkv',
```

## Tipps und Tricks

### 1. Standard-Speicherort festlegen

Bearbeiten Sie in `video_downloader.py` die Funktion `get_save_location()`:

```python
def get_save_location():
    # Fügen Sie diese Zeile am Anfang hinzu:
    default_location = r"C:\Users\MeinName\Videos"

    print("\n" + "-" + 60)
    location = input(f"Wo soll das Video gespeichert werden?\n(Enter für: {default_location}): ").strip()

    if not location:
        return default_location
    # ... rest des Codes
```

### 2. Automatisch "Ja" zum Download sagen

Um die Bestätigung zu überspringen, kommentieren Sie in `video_downloader.py` Zeilen 120-125 aus:

```python
# confirm = input("Download starten? (j/n): ").strip().lower()
#
# if confirm not in ['j', 'ja', 'y', 'yes']:
#     print("❌ Download abgebrochen.")
#     return False
```

### 3. Dateinamen anpassen

Das Standard-Format ist: `%(title)s.%(ext)s`

Andere Optionen:
```python
# Mit Uploader-Name:
'outtmpl': os.path.join(save_path, '%(uploader)s - %(title)s.%(ext)s'),

# Mit Datum:
'outtmpl': os.path.join(save_path, '%(upload_date)s - %(title)s.%(ext)s'),

# Mit ID:
'outtmpl': os.path.join(save_path, '%(title)s [%(id)s].%(ext)s'),

# Nur ID als Name:
'outtmpl': os.path.join(save_path, '%(id)s.%(ext)s'),
```

### 4. Untertitel herunterladen

Fügen Sie diese Optionen zu `ydl_opts` hinzu:

```python
ydl_opts = {
    'outtmpl': os.path.join(save_path, '%(title)s.%(ext)s'),
    'format': 'bestvideo[ext=mp4]+bestaudio[ext=m4a]/best[ext=mp4]/best',
    'merge_output_format': 'mp4',

    # Untertitel-Optionen:
    'writesubtitles': True,  # Untertitel herunterladen
    'writeautomaticsub': True,  # Automatische Untertitel
    'subtitleslangs': ['de', 'en'],  # Sprachen
    'subtitlesformat': 'srt',  # Format

    # ... rest der Optionen
}
```

### 5. Thumbnails speichern

```python
ydl_opts = {
    # ... andere Optionen
    'writethumbnail': True,  # Thumbnail herunterladen
    'embedthumbnail': True,  # In Video einbetten (benötigt ffmpeg)
}
```

### 6. Playlist herunterladen

Das Script unterstützt bereits Playlists! Geben Sie einfach den Playlist-Link ein:
```
https://www.youtube.com/playlist?list=PLXXXXXXXXXXXXXXXXX
```

Um nur bestimmte Videos aus einer Playlist zu laden:
```python
ydl_opts = {
    # ... andere Optionen
    'playlist_items': '1-5',  # Nur erste 5 Videos
    # oder
    'playlist_items': '1,3,5,7',  # Nur Videos 1, 3, 5 und 7
}
```

## Häufig verwendete Links

### YouTube
- Einzelnes Video: `https://www.youtube.com/watch?v=VIDEO_ID`
- Playlist: `https://www.youtube.com/playlist?list=PLAYLIST_ID`
- Kanal: `https://www.youtube.com/@username`

### Instagram
- Post: `https://www.instagram.com/p/POST_ID/`
- Reel: `https://www.instagram.com/reel/REEL_ID/`

### TikTok
- Video: `https://www.tiktok.com/@username/video/VIDEO_ID`
- Oder kurzer Link: `https://vm.tiktok.com/XXXXXX/`

### Twitter/X
- Tweet: `https://twitter.com/username/status/TWEET_ID`
- Oder: `https://x.com/username/status/TWEET_ID`

### Reddit
- Post: `https://www.reddit.com/r/subreddit/comments/POST_ID/title/`

## Fehlerbehebung

### "Dieses Video ist nicht verfügbar"
- Prüfen Sie, ob das Video öffentlich ist
- Versuchen Sie, yt-dlp zu aktualisieren: `pip install --upgrade yt-dlp`

### "HTTP Error 429: Too Many Requests"
- Warten Sie einige Minuten
- Die Plattform hat zu viele Anfragen erkannt
- Versuchen Sie es später erneut

### Download ist sehr langsam
- Das liegt oft an der Internetverbindung
- Oder an der Download-Geschwindigkeit der Plattform
- Versuchen Sie eine niedrigere Qualität

### Video und Audio sind getrennt
- Installieren Sie ffmpeg
- ffmpeg kombiniert Video und Audio automatisch

## Weitere Ressourcen

- [yt-dlp Dokumentation](https://github.com/yt-dlp/yt-dlp#readme)
- [yt-dlp Format Selection](https://github.com/yt-dlp/yt-dlp#format-selection)
- [yt-dlp Output Template](https://github.com/yt-dlp/yt-dlp#output-template)
- [FFmpeg Download](https://ffmpeg.org/download.html)
