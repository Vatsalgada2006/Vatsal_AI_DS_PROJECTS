# Auto-install missing packages used in this script
import importlib, subprocess, sys
def install_if_missing(pkg_name, import_name=None):
    try:
        importlib.import_module(import_name or pkg_name)
    except Exception:
        print(f"Installing {pkg_name} ...")
        subprocess.check_call([sys.executable, "-m", "pip", "install", pkg_name])
install_if_missing("requests")
import requests
api = input("Enter OpenWeatherMap API key (or press Enter to skip): ").strip()
city = input("Enter city name: ").strip()
if not api:
    print("No API key provided. Sign up at openweathermap.org to get one.")
else:
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api}&units=metric"
    r = requests.get(url)
    data = r.json()
    if data.get("cod") != 200:
        print("Error:", data.get("message"))
    else:
        print("Temperature:", data['main']['temp'], "°C")
