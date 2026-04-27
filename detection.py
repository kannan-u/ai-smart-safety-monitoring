from ultralytics import YOLO

model = YOLO("yolov8n.pt")

def detect_human(frame):
    results = model(frame)

    for r in results:
        for box in r.boxes:
            cls = int(box.cls[0])
            if cls == 0:  # 0 = person
                return True
    return False