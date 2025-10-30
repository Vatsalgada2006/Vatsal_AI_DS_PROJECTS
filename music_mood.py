# Auto-install missing packages used in this script
import importlib, subprocess, sys
def install_if_missing(pkg_name, import_name=None):
    try:
        importlib.import_module(import_name or pkg_name)
    except Exception:
        print(f"Installing {pkg_name} ...")
        subprocess.check_call([sys.executable, "-m", "pip", "install", pkg_name])
install_if_missing("pygame")
import random, os
# This is a simple mood -> local song list recommender.
moods = {
    "happy": ["happy1.mp3", "happy2.mp3"],
    "sad": ["sad1.mp3", "sad2.mp3"],
    "neutral": ["neutral1.mp3"]
}
mood = input("Enter detected mood (happy/sad/neutral): ").strip().lower()
songs = moods.get(mood)
if not songs:
    print("No songs for this mood in sample. Edit the script to add local file paths.")
else:
    choice = random.choice(songs)
    print("Selected:", choice)
    print("To auto-play, place MP3 files in this folder and use pygame to play.")
