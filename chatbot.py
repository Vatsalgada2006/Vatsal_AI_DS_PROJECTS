# Auto-install missing packages used in this script
import importlib, subprocess, sys
def install_if_missing(pkg_name, import_name=None):
    try:
        importlib.import_module(import_name or pkg_name)
    except Exception:
        print(f"Installing {pkg_name} ...")
        subprocess.check_call([sys.executable, "-m", "pip", "install", pkg_name])
# Simple rule-based chatbot for college FAQs
responses = {
    "hi":"Hello! How can I help you?",
    "what are the office hours":"Office hours are 9 AM to 5 PM, Monday to Friday.",
    "where is the library":"The college library is in block B, ground floor.",
    "bye":"Goodbye! Have a nice day."
}
def respond(q):
    q = q.lower().strip()
    for k in responses:
        if k in q:
            return responses[k]
    return "I am not sure. Please contact administration."
print("Chatbot started. Type 'bye' to exit.")
while True:
    q = input("You: ")
    print("Bot:", respond(q))
    if q.lower().strip() == "bye":
        break
