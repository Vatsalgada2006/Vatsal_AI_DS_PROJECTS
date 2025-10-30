# Auto-install missing packages used in this script
import importlib, subprocess, sys
def install_if_missing(pkg_name, import_name=None):
    try:
        importlib.import_module(import_name or pkg_name)
    except Exception:
        print(f"Installing {pkg_name} ...")
        subprocess.check_call([sys.executable, "-m", "pip", "install", pkg_name])
install_if_missing("mediapipe")
install_if_missing("pyautogui")
install_if_missing("opencv-python","cv2")
import cv2, mediapipe as mp, pyautogui
mp_hands = mp.solutions.hands
mp_drawing = mp.solutions.drawing_utils
screen_w, screen_h = pyautogui.size()
cap = cv2.VideoCapture(0)
with mp_hands.Hands(max_num_hands=1, min_detection_confidence=0.6) as hands:
    while True:
        ret, frame = cap.read()
        if not ret: break
        frame = cv2.flip(frame,1)
        h,w,_ = frame.shape
        rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        results = hands.process(rgb)
        if results.multi_hand_landmarks:
            for handLms in results.multi_hand_landmarks:
                mp_drawing.draw_landmarks(frame, handLms, mp_hands.HAND_CONNECTIONS)
                lm = handLms.landmark[8]  # index finger tip
                x, y = int(lm.x * w), int(lm.y * h)
                pyautogui.moveTo(screen_w/w*x, screen_h/h*y)
        cv2.imshow("Virtual Mouse", frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
cap.release()
cv2.destroyAllWindows()
