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
install_if_missing("pyaudio")
import speech_recognition as sr, pyttsx3, webbrowser, datetime
listener = sr.Recognizer()
engine = pyttsx3.init()
def speak(text):
    engine.say(text); engine.runAndWait()
def listen():
    with sr.Microphone() as source:
        print("Listening...")
        audio = listener.listen(source, phrase_time_limit=5)
    try:
        return listener.recognize_google(audio).lower()
    except Exception as e:
        return ""
speak("Hello! I am Jarvis.")
while True:
    command = listen()
    if not command:
        continue
    print("You:", command)
    if 'time' in command:
        speak(datetime.datetime.now().strftime("%I:%M %p"))
    elif 'open youtube' in command:
        webbrowser.open("https://youtube.com")
        speak("Opening YouTube")
    elif 'stop' in command or 'exit' in command:
        speak("Goodbye")
        break
    else:
        speak("I heard " + command)
