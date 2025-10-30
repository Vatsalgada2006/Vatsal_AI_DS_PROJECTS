# Auto-install missing packages used in this script
import importlib, subprocess, sys
def install_if_missing(pkg_name, import_name=None):
    try:
        importlib.import_module(import_name or pkg_name)
    except Exception:
        print(f"Installing {pkg_name} ...")
        subprocess.check_call([sys.executable, "-m", "pip", "install", pkg_name])
install_if_missing("SpeechRecognition","speech_recognition")
install_if_missing("pyttsx3")
import speech_recognition as sr, pyttsx3
r = sr.Recognizer()
tts = pyttsx3.init()
print("1) Speech to Text\n2) Text to Speech")
choice = input("Choose (1/2): ").strip()
if choice == "1":
    with sr.Microphone() as src:
        print("Say something...")
        audio = r.listen(src, phrase_time_limit=5)
    try:
        text = r.recognize_google(audio)
        print("You said:", text)
    except Exception as e:
        print("Could not recognize:", e)
else:
    text = input("Enter text to speak: ")
    tts.say(text)
    tts.runAndWait()
