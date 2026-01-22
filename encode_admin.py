import face_recognition
import pickle

image = face_recognition.load_image_file("admin/admin.jpg")
encodings = face_recognition.face_encodings(image)

if len(encodings) == 0:
    print("No face found in admin image")
    exit()

with open("admin_encoding.pkl", "wb") as f:
    pickle.dump(encodings[0], f)

print("Admin encoding saved successfully")
