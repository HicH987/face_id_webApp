import cv2
import argparse
import numpy as np

from flask_cors import CORS
from flask import Flask, request, jsonify

from utils.face_id_functions import add_face, run_identification


app = Flask(__name__)
CORS(app)


@app.route("/test")
def test():
    return "!!!! test flask app !!!!"


@app.route("/api/face-identification", methods=["POST"])
def face_identification():
    image_file = request.files["image"]
    image = cv2.imdecode(
        np.frombuffer(image_file.read(), np.uint8), cv2.IMREAD_UNCHANGED
    )
    face_name = run_identification(image)

    return {"name": f"{face_name}"}


@app.route("/api/add-face-name", methods=["POST"])
def add_face_name():
    data = request.get_json()
    text_input = data["textInput"]

    add_face(text_input)

    response = {"message": f"The face was named: {text_input}"}
    return jsonify(response)



parser = argparse.ArgumentParser()
parser.add_argument('--url', help='ACCESS LINK', default=None)

args = parser.parse_args()

if __name__ == "__main__":
    if args.url:
        for rule in list(app.url_map.iter_rules())[1:]:
                print(str(args.url)+str(rule))
        print('\n')
        
    app.run(debug=True)
