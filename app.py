from flask import Flask, request, jsonify, render_template
import cv2
import numpy as np
import dlib
from imutils import face_utils
import base64

app = Flask(__name__)

# Load face detector and landmark predictor
detector = dlib.get_frontal_face_detector()
predictor = dlib.shape_predictor("shape_predictor_68_face_landmarks.dat")

def compute(ptA, ptB):
    return np.linalg.norm(ptA - ptB)

def blinked(a, b, c, d, e, f):
    up = compute(b, d) + compute(c, e)
    down = compute(a, f)
    ratio = up / (2.0 * down)
    if ratio > 0.25:
        return 2
    elif 0.21 < ratio <= 0.25:
        return 1
    else:
        return 0

# ✅ Homepage route
@app.route("/")
def index():
    return render_template("index.html")  # will look for templates/index.html

# ✅ Detection API
@app.route("/detect", methods=["POST"])
def detect():
    data = request.json
    image_data = data["image"]

    # Decode base64 → numpy image
    nparr = np.frombuffer(base64.b64decode(image_data), np.uint8)
    frame = cv2.imdecode(nparr, cv2.IMREAD_COLOR)

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = detector(gray)

    status = "No Face"
    for face in faces:
        landmarks = predictor(gray, face)
        landmarks = face_utils.shape_to_np(landmarks)

        left_blink = blinked(landmarks[36], landmarks[37],
                             landmarks[38], landmarks[41],
                             landmarks[40], landmarks[39])
        right_blink = blinked(landmarks[42], landmarks[43],
                              landmarks[44], landmarks[47],
                              landmarks[46], landmarks[45])

        if left_blink == 0 or right_blink == 0:
            status = "SLEEPING"
        elif left_blink == 1 or right_blink == 1:
            status = "DROWSY"
        else:
            status = "ACTIVE"

    return jsonify({"status": status})
