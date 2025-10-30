# Auto-install missing packages used in this script
import importlib, subprocess, sys
def install_if_missing(pkg_name, import_name=None):
    try:
        importlib.import_module(import_name or pkg_name)
    except Exception:
        print(f"Installing {pkg_name} ...")
        subprocess.check_call([sys.executable, "-m", "pip", "install", pkg_name])
install_if_missing("tensorflow")
install_if_missing("keras")
install_if_missing("opencv-python","cv2")
install_if_missing("numpy")
import cv2, numpy as np, tensorflow as tf
from tensorflow.keras.models import load_model
import os
# This script expects a model file 'emotion_model.h5' in the same folder OR will offer to download a small example model.
MODEL_PATH = "emotion_model.h5"
if not os.path.exists(MODEL_PATH):
    print("No pretrained model found. To run full emotion detection, download a model and save as 'emotion_model.h5' in this folder.")
    print("As fallback, the script will run face detection only.")
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")
cap = cv2.VideoCapture(0)
labels = ['Angry','Disgust','Fear','Happy','Sad','Surprise','Neutral']
model = None
if os.path.exists(MODEL_PATH):
    model = load_model(MODEL_PATH)
while True:
    ret, frame = cap.read()
    if not ret: break
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray,1.3,5)
    for (x,y,w,h) in faces:
        roi = gray[y:y+h, x:x+w]
        cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),2)
        if model is not None:
            img = cv2.resize(roi,(48,48))/255.0
            pred = labels[np.argmax(model.predict(img.reshape(1,48,48,1)))]
            cv2.putText(frame,pred,(x,y-10),cv2.FONT_HERSHEY_SIMPLEX,0.9,(255,0,0),2)
    cv2.imshow("Emotion Detection", frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
cap.release(); cv2.destroyAllWindows()
