import os
import cv2
import glob
import numpy as np
import mediapipe as mp

try:
    import face_recognition
except:
    import subprocess

    subprocess.check_call(
        [
            "pip",
            "install",
            "cmake",
            "https://github.com/jloh02/dlib/releases/download/v19.22/dlib-19.22.99-cp310-cp310-win_amd64.whl",
            "face-recognition",
        ]
    )
from tkinter import Tk, simpledialog


def get_face_name():
    root = Tk()
    root.withdraw()
    face_name = simpledialog.askstring("Input", "Enter face name:")
    root.destroy()
    return face_name


mp_face_detection = mp.solutions.face_detection
mp_drawing = mp.solutions.drawing_utils


images_dir_path = "faces"
data_path = "face_data.npz"

try:
    loaded_data = np.load(data_path)
    known_face_names = list(loaded_data["names"])
    known_face_encodings = list(loaded_data["encodings"])
except:
    images_path = glob.glob(f"{images_dir_path}/*")
    known_face_names = []
    known_face_encodings = []
    for img_path in images_path:
        face_name = os.path.splitext(os.path.basename(img_path))[0]

        face_image = face_recognition.load_image_file(img_path)
        face_encoding = face_recognition.face_encodings(face_image)[0]

        known_face_names.append(face_name)
        known_face_encodings.append(np.array(face_encoding))
    np.savez_compressed(
        data_path,
        names=np.array(known_face_names),
        encodings=np.array(known_face_encodings),
    )


face_locations = []
face_encodings = []
face_names = []
process_current_frame = False
video_capture = cv2.VideoCapture(0)
while True:
    ret, frame = video_capture.read()

    # Only process every other frame of video to save time
    if process_current_frame:
        # Resize frame of video to 1/4 size for faster face recognition processing
        small_frame = cv2.resize(frame, (0, 0), fx=0.25, fy=0.25)

        # Convert the image from BGR color (which OpenCV uses) to RGB color (which face_recognition uses)
        rgb_small_frame = small_frame[:, :, ::-1]

        # Find all the faces and face encodings in the current frame of video
        face_locations = face_recognition.face_locations(rgb_small_frame)
        face_encodings = face_recognition.face_encodings(
            rgb_small_frame, face_locations
        )

        face_names = []
        for face_encoding in face_encodings:
            # See if the face is a match for the known face(s)
            matches = face_recognition.compare_faces(
                known_face_encodings, face_encoding
            )
            # Calculate the shortest distance to face
            face_distances = face_recognition.face_distance(
                known_face_encodings, face_encoding
            )

            best_match_index = np.argmin(face_distances)
            if matches[best_match_index]:
                name = known_face_names[best_match_index]
            else:
                name = "Unknown"
            print(name)
            face_names.append(name)

        if face_names and face_names[0] == "Unknown":
            face_name = get_face_name()
            if not (face_name is None):
                # face_name = input("entre face name: ")
                face_encoding = face_recognition.face_encodings(frame)[0]
                known_face_names.append(face_name)
                known_face_encodings.append(np.array(face_encoding))
                np.savez_compressed(
                    data_path,
                    names=np.array(known_face_names),
                    encodings=np.array(known_face_encodings),
                )
                face_names[0] = face_name

        if face_names:
            process_current_frame = False

    # Display the results
    for (top, right, bottom, left), name in zip(face_locations, face_names):
        cv2.putText(
            frame, name, (10, 30), cv2.FONT_HERSHEY_DUPLEX, 0.95, (0, 255, 0), 1
        )

    # Display the resulting image
    cv2.imshow("Face Recognition", frame)

    if cv2.waitKey(1) == ord("s"):
        print("<< -s- pressed >>")
        process_current_frame = not process_current_frame

    # Hit 'q' on the keyboard to quit!
    if cv2.waitKey(1) == ord("q"):
        cv2.destroyAllWindows()
        break

# Release handle to the webcam
video_capture.release()
