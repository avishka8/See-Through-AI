from ultralytics import YOLO

class ObjectDetector:
    def __init__(self):
        self.model = YOLO("yolov8m.pt")

    def detect(self, frame):
        return self.model(frame, conf=0.5)