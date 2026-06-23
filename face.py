import cv2
import mediapipe as mp
import os

os.environ["GLOG_minloglevel"] = "3"
os.environ["TF_CPP_MIN_LOG_LEVEL"] = "3"

# --- Test camera first ---
print("Testing camera...")
cap = cv2.VideoCapture(0, cv2.CAP_MSMF)

if not cap.isOpened():
    print("Camera 0 failed, trying camera 1...")
    cap = cv2.VideoCapture(1)

if not cap.isOpened():
    print("ERROR: No camera found!")
    exit()

print("Camera opened! You should see a window now.")

MODEL_PATH = "face_landmarker.task"
if not os.path.exists(MODEL_PATH):
    import urllib.request
    print("Downloading model...")
    urllib.request.urlretrieve(
        "https://storage.googleapis.com/mediapipe-models/face_landmarker/face_landmarker/float16/1/face_landmarker.task",
        MODEL_PATH
    )
    print("Done!")

BaseOptions = mp.tasks.BaseOptions
FaceLandmarker = mp.tasks.vision.FaceLandmarker
FaceLandmarkerOptions = mp.tasks.vision.FaceLandmarkerOptions
VisionRunningMode = mp.tasks.vision.RunningMode

options = FaceLandmarkerOptions(
    base_options=BaseOptions(model_asset_path=MODEL_PATH),
    running_mode=VisionRunningMode.IMAGE,
    num_faces=1
)

CONNECTIONS = mp.tasks.vision.FaceLandmarksConnections.FACE_LANDMARKS_TESSELATION

print("Starting face mesh... Press Q to quit")

with FaceLandmarker.create_from_options(options) as landmarker:
    while True:
        ret, frame = cap.read()

        if not ret:
            print("ERROR: Can't read frame!")
            break

        frame = cv2.flip(frame, 1)
        h, w = frame.shape[:2]

        rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        mp_image = mp.Image(image_format=mp.ImageFormat.SRGB, data=rgb)
        result = landmarker.detect(mp_image)

        if result.face_landmarks:
            for face in result.face_landmarks:
                for conn in CONNECTIONS:
                    x1 = int(face[conn.start].x * w)
                    y1 = int(face[conn.start].y * h)
                    x2 = int(face[conn.end].x * w)
                    y2 = int(face[conn.end].y * h)
                    cv2.line(frame, (x1, y1), (x2, y2), (0, 200, 100), 1)
                for lm in face:
                    cx, cy = int(lm.x * w), int(lm.y * h)
                    cv2.circle(frame, (cx, cy), 1, (0, 255, 0), -1)
        else:
            cv2.putText(frame, "No face detected", (20, 40),
                        cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)

        cv2.imshow("Face Mesh", frame)

        key = cv2.waitKey(1) & 0xFF
        if key == ord('q'):
            break

cap.release()
cv2.destroyAllWindows()
print("Done!")