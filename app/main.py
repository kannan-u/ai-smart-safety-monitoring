import cv2
from app.detection import detect_human
from app.sensor import ir_trigger
from app.alert import send_alert

def run_system():
    cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)

    if not cap.isOpened():
        print("❌ Camera failed to open")
        return
    else:
        print("✅ Camera started")

    last_state = ""

    while True:
        ret, frame = cap.read()
        if not ret:
            print("❌ Failed to read frame")
            break

        motion = ir_trigger()

        if motion:
            human = detect_human(frame)
            if human:
                current_state = "🚨 HUMAN DETECTED"
            else:
                current_state = "⚠️ MOTION DETECTED"
        else:
            current_state = "✅ NO ACTIVITY"

        # Print only on change
        if current_state != last_state:
            print(current_state)
            last_state = current_state

            if "HUMAN" in current_state:
                send_alert()

        # Show status on screen
        cv2.putText(
            frame,
            current_state,
            (10, 30),
            cv2.FONT_HERSHEY_SIMPLEX,
            1,
            (0, 255, 0),
            2
        )

        cv2.imshow("Smart Safety Monitoring", frame)

        if cv2.waitKey(1) == 27:
            break

    cap.release()
    cv2.destroyAllWindows()


if __name__ == "__main__":
    run_system()