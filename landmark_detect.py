import cv2
import mediapipe as mp
from mediapipe import solutions

# Initialize MediaPipe Face Mesh
mp_face_mesh = mp.solutions.face_mesh
face_mesh = mp_face_mesh.FaceMesh(
    max_num_faces=1,
    refine_landmarks=True,  # Crucial: This enables iris detection
    min_detection_confidence=0.5,
    min_tracking_confidence=0.5
)

cap = cv2.VideoCapture(0)

while cap.isOpened():
    success, image = cap.read()
    if not success: break

    # Convert to RGB for MediaPipe processing
    rgb_image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    results = face_mesh.process(rgb_image)

    if results.multi_face_landmarks:
        for face_landmarks in results.multi_face_landmarks:
            # Indices for Left and Right Iris
            # These provide the "iris vector" data for your model 
            LEFT_IRIS = [468, 469, 470, 471, 472]
            RIGHT_IRIS = [473, 474, 475, 476, 477]
            
            h, w, _ = image.shape
            for idx in LEFT_IRIS + RIGHT_IRIS:
                point = face_landmarks.landmark[idx]
                cx, cy = int(point.x * w), int(point.y * h)
                cv2.circle(image, (cx, cy), 1, (0, 255, 0), -1)

    cv2.imshow('EyeScribe: Iris Extraction', image)
    if cv2.waitKey(5) & 0xFF == 27: break

cap.release()
cv2.destroyAllWindows()