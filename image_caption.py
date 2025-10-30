# Auto-install missing packages used in this script
import importlib, subprocess, sys
def install_if_missing(pkg_name, import_name=None):
    try:
        importlib.import_module(import_name or pkg_name)
    except Exception:
        print(f"Installing {pkg_name} ...")
        subprocess.check_call([sys.executable, "-m", "pip", "install", pkg_name])
# This is a starter stub. Full image captioning requires training or a pretrained model.
# The script demonstrates how to load an image and (optionally) call a pretrained caption model if available.
install_if_missing("opencv-python","cv2")
import cv2, os
img_path = input("Enter image filename in this folder (e.g., sample.jpg) or leave blank to skip: ").strip()
if not img_path:
    print("No image provided. See README for instructions to add a caption model.")
else:
    if not os.path.exists(img_path):
        print("Image not found:", img_path)
    else:
        img = cv2.imread(img_path)
        h,w = img.shape[:2]
        print(f"Loaded image {img_path} with size {w}x{h}")
        print("This starter does not include a pretrained caption model. You can integrate models from TensorFlow Hub or train on Flickr8k.")
