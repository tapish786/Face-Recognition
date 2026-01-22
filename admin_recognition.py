import cv2
import face_recognition
import pickle
import numpy as np

with open("admin_encoding.pkl", "rb") as f:
    admin_encoding = pickle.load(f)

cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    if not ret:
        break

    rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    face_locations = face_recognition.face_locations(rgb)
    face_encodings = face_recognition.face_encodings(rgb, face_locations)

    name = "Unauthorized"
    color = (0, 0, 255)

    for enc in face_encodings:
        distance = face_recognition.face_distance([admin_encoding], enc)

        if distance[0] < 0.45:
            name = "Admin"
            color = (0, 255, 0)

    for (top, right, bottom, left) in face_locations:
        cv2.rectangle(frame, (left, top), (right, bottom), color, 2)
        cv2.putText(
            frame,
            name,
            (left, top - 10),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.8,
            color,
            2
        )

    cv2.imshow("Admin Face Recognition", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
