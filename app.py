import cv2
import numpy as np
from flask_cors import CORS
from flask import Flask, request, jsonify

app = Flask(__name__)
CORS(app)

@app.route('/test/')
def test() :
    return '!!!! test flask app !!!!'

@app.route('/add_hello', methods=['POST'])
def add_hello():
    data = request.get_json()
    input_string = data['input_string']
    output_string = input_string + ' hello'
    print(output_string)
    response = {'output_string': output_string}
    return jsonify(response)


@app.route('/api/upload-image', methods=['POST'])
def upload_image():
    image_file = request.files['image']
    image = cv2.imdecode(np.frombuffer(image_file.read(), np.uint8), cv2.IMREAD_UNCHANGED)
    cv2.imwrite('./uploaded_image.jpg', image)
    return {'message': 'Image uploaded successfully'}

if __name__ == '__main__':
    app.run(debug=True)