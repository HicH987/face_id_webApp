

# Face Identification Flask API

This is a Flask API for face identification, capable of recognizing known faces and associating them with names. The API is written in Python 3.10.7 and uses OpenCV for face recognition.

## Prerequire
- [Python](https://www.python.org/downloads/) 
- pip (Python package installer) it come with python


## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/your-username/face_id_flask_api.git
   cd face_id_flask_api
   ```

2. Install the required packages:

   ```bash
   pip install -r requirements.txt
   ```

## Usage

To start the server, run the following command:

```bash
flask run
```
or
```bash
python app.py
```

### API Endpoints

The API provides the following endpoints:

#### 1. `POST /api/face-identification`

   This endpoint receives a face image and searches the known faces data to determine if the face is known. If the face is known, the endpoint returns the name of the person associated with the face. If the face is unknown, the endpoint returns `"Unknown_face"`.

- ##### Request

   The request should contain a `multipart/form-data` file with the key `"image"`.

- ##### Response

   If the face is known, the response is a JSON object containing the `"name"` of the person associated with the face.

   If the face is unknown, the response is a JSON object containing `"Unknown_face"`.

#### 2. `POST /api/add-face-name`

This endpoint receives a name to associate with an unknown face and adds it to the known faces data.

- ##### Request

   The request should contain a JSON object with the following structure:

   ```json
   {
   "textInput": "Name of the person"
   }
   ```

- ##### Response

   The response is a JSON object containing a `"message"` indicating that the face was named with the given name.

- #### `GET /test/`

   This endpoint returns a simple message indicating that the Flask app is working.

### Example

Here's an example of how to use the API endpoints using `curl`.

To recognize a face:

```bash
curl -X POST -F "image=@path/to/image.jpg" http://localhost:5000/api/face-identification
```

To add a name to an unknown face:

```bash
curl -X POST -H "Content-Type: application/json" -d '{"textInput": "Name of the person"}' http://localhost:5000/api/add-face-name
```

If you are familiar with react js here is a simple app that use this api [link](https://github.com/HicH987/react_app_face_id_api_test)

## Additional Information

This API was created using the following packages:

- Flask (v2.2.3)
- Flask-Cors (v3.0.10)

For more information on how to use Flask, please refer to the official Flask documentation: https://flask.palletsprojects.com/.

For more information on face recognition with OpenCV, please refer to the OpenCV documentation: https://face-recognition.readthedocs.io/en/latest/readme.html.