from ultralytics import YOLO

model = YOLO("yolov8n.pt")

def detect_human(frame):
    results = model(frame, verbose=False)

    for result in results:
        for box in result.boxes:
            cls = int(box.cls[0])
            if cls == 0:  # person
                return True

    return False