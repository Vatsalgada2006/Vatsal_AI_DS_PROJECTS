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
import tensorflow as tf
from tensorflow import keras
import os
model_file = "digit_model.h5"
if os.path.exists(model_file):
    model = keras.models.load_model(model_file)
    print("Loaded existing model:", model_file)
else:
    print("Training a small model on MNIST (this may take a minute)...")
    (x_train,y_train),(x_test,y_test)=keras.datasets.mnist.load_data()
    x_train,x_test = x_train/255.0, x_test/255.0
    model = keras.Sequential([
        keras.layers.Flatten(input_shape=(28,28)),
        keras.layers.Dense(128, activation='relu'),
        keras.layers.Dense(10, activation='softmax')
    ])
    model.compile(optimizer='adam', loss='sparse_categorical_crossentropy', metrics=['accuracy'])
    model.fit(x_train,y_train, epochs=3, validation_data=(x_test,y_test))
    model.save(model_file)
    print("Model trained and saved to", model_file)
# Simple test: predict on first 5 test samples
import numpy as np
(x_train,y_train),(x_test,y_test)=keras.datasets.mnist.load_data()
preds = model.predict(x_test[:5]/255.0)
print("Predictions:", np.argmax(preds, axis=1), "Ground truth:", y_test[:5])
