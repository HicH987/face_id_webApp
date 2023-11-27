# Project: Face Identification React App with Flask API

This project combines a ReactJS frontend and a Flask backend for face identification.

## Frontend (ReactJS App)

### Setup

1. Clone the repository:

    ```bash
    git clone https://github.com/HicH987/face_id_webApp.git
    cd face_id_webApp/Frontend
    npm install
    ```

2. Development:

    ```bash
    npm run dev
    ```

    Open the app in your browser.

3. Build:

    ```bash
    npm run build
    ```

    Deploy the contents of the `dist` directory to your web server.


## Backend (Face Identification Flask API)

### Installation

1. Clone the Flask API repository:

    ```bash
    git clone https://github.com/HicH987/face_id_webApp.git
    cd face_id_webApp/Backend
    pip install -r requirements.txt
    ```

2. Usage:

    ```bash
    python app.py
    ```

#### API Endpoints:

1. **POST /api/face-identification**

   - Request: `multipart/form-data` file with key `"image"`
   - Response: JSON with `"name"` or `"Unknown_face"`

2. **POST /api/add-face-name**

   - Request: JSON object `{"textInput": "Name of the person"}`
   - Response: JSON with `"message"`

3. **GET /test/**

   - Returns a message indicating the Flask app is working.

#### Example:

Recognize a face:

```bash
curl -X POST -F "image=@path/to/image.jpg" http://localhost:5000/api/face-identification
```

Add a name:

```bash
curl -X POST -H "Content-Type: application/json" -d '{"textInput": "Name of the person"}' http://localhost:5000/api/add-face-name
```


Deploy the API on [Google Colab](https://colab.research.google.com/github/HicH987/face_id_webApp/blob/master/Backend/_deployment_colab.ipynb).