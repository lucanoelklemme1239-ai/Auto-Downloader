#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Auto-Downloader für Videos
Unterstützt Downloads von YouTube, Vimeo, und vielen anderen Plattformen
"""

import os
import sys
import subprocess

def check_dependencies():
    """Überprüft ob yt-dlp installiert ist"""
    try:
        import yt_dlp
        return True
    except ImportError:
        print("=" * 60)
        print("FEHLER: yt-dlp ist nicht installiert!")
        print("=" * 60)
        print("\nBitte führen Sie folgende Befehle aus:")
        print("  pip install yt-dlp")
        print("\nOder installieren Sie alle Abhängigkeiten mit:")
        print("  pip install -r requirements.txt")
        print("=" * 60)
        return False

def get_video_link():
    """Fragt den Benutzer nach dem Video-Link"""
    print("\n" + "=" * 60)
    print("AUTO-DOWNLOADER FÜR VIDEOS")
    print("=" * 60)
    print("\nUnterstützte Plattformen:")
    print("  - YouTube, YouTube Music")
    print("  - Vimeo, Dailymotion")
    print("  - Facebook, Instagram, TikTok")
    print("  - Twitter/X, Reddit")
    print("  - und viele mehr...")
    print("=" * 60)

    while True:
        link = input("\nGeben Sie den Video-Link ein (oder 'q' zum Beenden): ").strip()

        if link.lower() == 'q':
            print("\nProgramm wird beendet...")
            sys.exit(0)

        if link and (link.startswith('http://') or link.startswith('https://')):
            return link
        else:
            print("⚠️  Ungültiger Link! Bitte geben Sie einen vollständigen Link ein (beginnend mit http:// oder https://)")

def get_save_location():
    """Fragt den Benutzer nach dem Speicherort"""
    print("\n" + "-" * 60)

    while True:
        location = input("Wo soll das Video gespeichert werden?\n(Pfad oder Enter für aktuelles Verzeichnis): ").strip()

        # Standard: Aktuelles Verzeichnis
        if not location:
            location = os.getcwd()
            print(f"✓ Verwende aktuelles Verzeichnis: {location}")
            return location

        # Expandiere Umgebungsvariablen und relative Pfade
        location = os.path.expanduser(location)
        location = os.path.expandvars(location)
        location = os.path.abspath(location)

        # Überprüfe ob Verzeichnis existiert
        if os.path.isdir(location):
            print(f"✓ Speicherort bestätigt: {location}")
            return location
        else:
            print(f"⚠️  Verzeichnis existiert nicht: {location}")
            create = input("Möchten Sie das Verzeichnis erstellen? (j/n): ").strip().lower()

            if create in ['j', 'ja', 'y', 'yes']:
                try:
                    os.makedirs(location, exist_ok=True)
                    print(f"✓ Verzeichnis erstellt: {location}")
                    return location
                except Exception as e:
                    print(f"❌ Fehler beim Erstellen des Verzeichnisses: {e}")
                    print("Bitte versuchen Sie einen anderen Pfad.")
            else:
                print("Bitte geben Sie einen anderen Pfad ein.")

def download_video(url, save_path):
    """Lädt das Video mit yt-dlp herunter"""
    import yt_dlp

    print("\n" + "=" * 60)
    print("STARTE DOWNLOAD...")
    print("=" * 60)

    # yt-dlp Optionen
    ydl_opts = {
        'outtmpl': os.path.join(save_path, '%(title)s.%(ext)s'),
        'format': 'bestvideo[ext=mp4]+bestaudio[ext=m4a]/best[ext=mp4]/best',
        'merge_output_format': 'mp4',
        'quiet': False,
        'no_warnings': False,
        'progress_hooks': [progress_hook],
    }

    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            print(f"\n📥 Hole Video-Informationen...")
            info = ydl.extract_info(url, download=False)

            print(f"\n📹 Titel: {info.get('title', 'Unbekannt')}")
            print(f"⏱️  Dauer: {format_duration(info.get('duration', 0))}")
            print(f"👤 Uploader: {info.get('uploader', 'Unbekannt')}")

            # Bestätigung vor Download
            print("\n" + "-" * 60)
            confirm = input("Download starten? (j/n): ").strip().lower()

            if confirm not in ['j', 'ja', 'y', 'yes']:
                print("❌ Download abgebrochen.")
                return False

            print("\n🚀 Starte Download...\n")
            ydl.download([url])

            print("\n" + "=" * 60)
            print("✅ DOWNLOAD ERFOLGREICH ABGESCHLOSSEN!")
            print("=" * 60)
            print(f"📁 Gespeichert in: {save_path}")
            print("=" * 60)
            return True

    except yt_dlp.utils.DownloadError as e:
        print("\n" + "=" * 60)
        print("❌ DOWNLOAD FEHLER!")
        print("=" * 60)
        print(f"Fehler: {str(e)}")
        print("\nMögliche Ursachen:")
        print("  - Video ist nicht verfügbar oder privat")
        print("  - Link ist ungültig")
        print("  - Geografische Beschränkungen")
        print("  - Altersbeschränkung")
        print("=" * 60)
        return False

    except Exception as e:
        print("\n" + "=" * 60)
        print("❌ UNERWARTETER FEHLER!")
        print("=" * 60)
        print(f"Fehler: {str(e)}")
        print("=" * 60)
        return False

def progress_hook(d):
    """Zeigt Download-Fortschritt an"""
    if d['status'] == 'downloading':
        percent = d.get('_percent_str', 'N/A')
        speed = d.get('_speed_str', 'N/A')
        eta = d.get('_eta_str', 'N/A')
        print(f"\r⏬ Fortschritt: {percent} | Geschwindigkeit: {speed} | ETA: {eta}", end='', flush=True)
    elif d['status'] == 'finished':
        print(f"\n✓ Download abgeschlossen, verarbeite Video...")

def format_duration(seconds):
    """Formatiert Sekunden zu MM:SS oder HH:MM:SS"""
    if not seconds:
        return "Unbekannt"

    hours = int(seconds // 3600)
    minutes = int((seconds % 3600) // 60)
    secs = int(seconds % 60)

    if hours > 0:
        return f"{hours}:{minutes:02d}:{secs:02d}"
    else:
        return f"{minutes}:{secs:02d}"

def main():
    """Hauptfunktion"""
    print("\n")
    print("╔" + "═" * 58 + "╗")
    print("║" + " " * 15 + "AUTO-DOWNLOADER FÜR VIDEOS" + " " * 16 + "║")
    print("╚" + "═" * 58 + "╝")

    # Überprüfe Abhängigkeiten
    if not check_dependencies():
        input("\nDrücken Sie Enter zum Beenden...")
        sys.exit(1)

    while True:
        try:
            # Hole Video-Link
            video_link = get_video_link()

            # Hole Speicherort
            save_location = get_save_location()

            # Starte Download
            success = download_video(video_link, save_location)

            # Frage ob weiterer Download gewünscht
            print("\n" + "=" * 60)
            another = input("\nMöchten Sie ein weiteres Video herunterladen? (j/n): ").strip().lower()

            if another not in ['j', 'ja', 'y', 'yes']:
                print("\n" + "=" * 60)
                print("Vielen Dank für die Nutzung des Auto-Downloaders!")
                print("=" * 60)
                break

        except KeyboardInterrupt:
            print("\n\n" + "=" * 60)
            print("Programm wurde durch Benutzer abgebrochen.")
            print("=" * 60)
            break
        except Exception as e:
            print(f"\n❌ Unerwarteter Fehler: {e}")
            print("Das Programm wird fortgesetzt...\n")

    input("\nDrücken Sie Enter zum Beenden...")

if __name__ == "__main__":
    main()
