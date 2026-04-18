import cv2
import numpy as np
from tensorflow.keras.models import load_model
from sensor_model import load_sensor_model, predict_internal_defect

from flask import Flask, jsonify
import datetime

app = Flask(__name__)

# -------------------------------
# Load the trained CNN model
# -------------------------------
model = load_model("defect_model.keras")

# Load sensor ML model
sensor_model = load_sensor_model()

# Show expected input shape
print("Model expects input shape:", model.input_shape)

IMG_SIZE = 128

# -------------------------------
# Start webcam
# -------------------------------
cap = cv2.VideoCapture(0)


def get_machine_data():

    ret, frame = cap.read()

    if not ret:
        return None

    # -------------------------------
    # Image Preprocessing
    # -------------------------------
    img = cv2.resize(frame, (IMG_SIZE, IMG_SIZE))
    img = img.astype("float32") / 255.0
    img = np.expand_dims(img, axis=0)

    # -------------------------------
    # CNN Surface Defect Prediction
    # -------------------------------
    prediction = model.predict(img, verbose=0)

    if prediction[0][0] > 0.5:
        surface_status = "DEFECT"
        surface_color = (0, 0, 255)
    else:
        surface_status = "NORMAL"
        surface_color = (0, 255, 0)

    surface_prob = float(prediction[0][0])

    # -------------------------------
    # Simulated Sensor Values
    # -------------------------------
    m1 = 200000000
    m2 = 55
    m3 = 0
    m4 = 52
    m5 = 6
    m6 = 407438
    m7 = 0
    m8 = 0
    m9 = 7

    # -------------------------------
    # Predict internal defect
    # -------------------------------
    pred, probability = predict_internal_defect(
        sensor_model,
        m1, m2, m3, m4, m5, m6, m7, m8, m9
    )

    print("Failure probability:", probability)

    # -------------------------------
    # Temporary Sensor Values
    # -------------------------------
    temperature = 65
    vibration = 0
    load = 120
    rpm = 1500

    # -------------------------------
    # Sensor Condition Check
    # -------------------------------
    if temperature > 80 or vibration == 1 or load > 180:
        sensor_status = "ABNORMAL"
    else:
        sensor_status = "NORMAL"

    # -------------------------------
    # Final System Decision
    # -------------------------------
    if surface_status == "DEFECT" or pred == 1:
        system_status = "DEFECT DETECTED"
    else:
        system_status = "SYSTEM NORMAL"

    # -------------------------------
    # Correction Logic
    # -------------------------------
    if pred == 1:

        print("⚠ Internal defect predicted")

        m2 = m2 - 5
        m3 = m3 - 10

        print("Suggested correction applied")

    # -------------------------------
    # Digital Twin Display
    # -------------------------------
    print("----- DIGITAL TWIN -----")
    print("Metric1:", m1)
    print("Metric2:", m2)
    print("Metric3:", m3)
    print("Metric4:", m4)
    print("Failure Probability:", probability)
    print("------------------------")

    # -------------------------------
    # Prepare JSON Data
    # -------------------------------
    health_score = int((1 - surface_prob) * 100)

    data = {

        "timestamp": str(datetime.datetime.now()),

        "temperature": temperature,
        "rpm": rpm,
        "load": load,
        "vibration": vibration,

        "surface_defect": surface_prob,
        "internal_defect": probability,

        "health_score": health_score,

        "machine_status": system_status
    }

    return data


# -------------------------------
# API Endpoint for Dashboard
# -------------------------------
@app.route("/machine-data")
def machine_data():

    data = get_machine_data()

    return jsonify(data)


# -------------------------------
# Run server
# -------------------------------
if __name__ == "__main__":

    app.run(debug=True)