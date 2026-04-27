import cv2
from detection import detect_human
from sensor import ir_trigger
from alert import send_alert
import time

last_state = "IDLE"

def log_event(state):
    print(f"[{time.strftime('%H:%M:%S')}] STATUS: {state}")

def run_system():
    global last_state

    cap = cv2.VideoCapture(0)

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        motion = ir_trigger()

        if motion:
            human = detect_human(frame)

            if human:
                current_state = "🚨 HUMAN DETECTED"
            else:
                current_state = "⚠️ MOTION DETECTED (NO HUMAN)"

        else:
            current_state = "✅ NO ACTIVITY"

        # 🔥 PRINT ONLY IF STATE CHANGES
        if current_state != last_state:
            log_event(current_state)
            last_state = current_state

            if "HUMAN" in current_state:
                send_alert()

        cv2.imshow("Smart Safety Monitoring", frame)

        if cv2.waitKey(1) == 27:
            break

    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    run_system()