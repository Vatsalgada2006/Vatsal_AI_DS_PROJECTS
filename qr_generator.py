# Auto-install missing packages used in this script
import importlib, subprocess, sys
def install_if_missing(pkg_name, import_name=None):
    try:
        importlib.import_module(import_name or pkg_name)
    except Exception:
        print(f"Installing {pkg_name} ...")
        subprocess.check_call([sys.executable, "-m", "pip", "install", pkg_name])
install_if_missing("qrcode")
from PIL import Image
import qrcode
data = input("Enter text or URL to encode into QR: ")
img = qrcode.make(data)
img.save("qrcode.png")
print("Saved qrcode.png")
