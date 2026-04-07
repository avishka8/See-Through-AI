import cv2
from app.detection import ObjectDetector
from app.distance import DistanceEstimator
from app.voice import speak
from app.config import DISTANCE_THRESHOLD
import time

ALLOWED_CLASSES = [
    "person",
    "car",
    "bicycle",
    "motorcycle",
    "chair",
    "table",
    "door",
    "stairs",
    "ceiling fan",
    "tv",
]

last_spoken = 0

detector = ObjectDetector()
distance_estimator = DistanceEstimator()

cap = cv2.VideoCapture("https://192.168.31.45:8080/video")

frame_count = 0


while True:

    ret, frame = cap.read()
    if not ret:
        break

    frame_count += 1

    if frame_count % 25 != 0:
        results = detector.detect(frame)

    for r in results:
        for box in r.boxes:
            x1, y1, x2, y2 = map(int, box.xyxy[0])
            width = x2 - x1

            distance = distance_estimator.estimate(width)
            label = detector.model.names[int(box.cls)]
            

    detected_objects = set()

    for r in results:
        for box in r.boxes:
            label = detector.model.names[int(box.cls)]
            print("detected", label)
            if label not in ALLOWED_CLASSES:
                continue

            detected_objects.add(label)

    if detected_objects and time.time() - last_spoken > 3:
        speak("I see " + ", ".join(detected_objects))
        last_spoken = time.time()

    cv2.imshow("See Through AI", frame)

    if cv2.waitKey(1) & 0xFF == 27:
        break

cap.release()
cv2.destroyAllWindows()