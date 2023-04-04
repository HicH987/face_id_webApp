import cv2
import numpy as np

import face_recognition
# try:
    # import face_recognition
# except:
    # import subprocess

    # subprocess.check_call(
        # [
            # "pip",
            # "install",
            # "cmake",
            # "https://github.com/jloh02/dlib/releases/download/v19.22/dlib-19.22.99-cp310-cp310-win_amd64.whl",
            # "face-recognition",
        # ]
    # )

data_path = "./data/face_data.npz"
loaded_data = np.load(data_path)
known_face_names = list(loaded_data["names"])
known_face_encodings = list(loaded_data["encodings"])


def add_face(face_name):
    current_image = cv2.imread('./data/current_face.jpg')
    face_encoding = face_recognition.face_encodings(current_image)[0]
    known_face_names.append(face_name)
    known_face_encodings.append(np.array(face_encoding))
    np.savez_compressed(
        data_path,
        names=np.array(known_face_names),
        encodings=np.array(known_face_encodings),
    )


def run_identification(frame):
    cv2.imwrite('../data/current_face.jpg', frame)
    
    small_frame = cv2.resize(frame, (0, 0), fx=0.25, fy=0.25)
    rgb_small_frame = cv2.cvtColor(small_frame, cv2.COLOR_BGR2RGB)

    face_locations = face_recognition.face_locations(rgb_small_frame)
    face_encoding = face_recognition.face_encodings(rgb_small_frame, face_locations)[0]

    matches = face_recognition.compare_faces(known_face_encodings, face_encoding)

    face_distances = face_recognition.face_distance(known_face_encodings, face_encoding)

    best_match_index = np.argmin(face_distances)
    if matches[best_match_index]:
        return known_face_names[best_match_index]
    
    return "Unknown_face"