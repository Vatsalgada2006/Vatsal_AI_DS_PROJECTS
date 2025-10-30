# Auto-install missing packages used in this script
import importlib, subprocess, sys
def install_if_missing(pkg_name, import_name=None):
    try:
        importlib.import_module(import_name or pkg_name)
    except Exception:
        print(f"Installing {pkg_name} ...")
        subprocess.check_call([sys.executable, "-m", "pip", "install", pkg_name])
install_if_missing("spacy")
# download model if needed (will try)
import os, subprocess, sys
try:
    import spacy
except:
    subprocess.check_call([sys.executable,"-m","pip","install","spacy"])
    import spacy
try:
    nlp = spacy.load("en_core_web_sm")
except:
    subprocess.check_call([sys.executable,"-m","spacy","download","en_core_web_sm"])
    nlp = spacy.load("en_core_web_sm")
skills = {"python","java","sql","machine learning","deep learning","tensorflow","keras","pandas","numpy"}
import glob
for file in glob.glob("resumes/*.txt"):
    text = open(file, encoding="utf-8", errors="ignore").read().lower()
    found = {s for s in skills if s in text}
    print(file, "-> Found skills:", found)
