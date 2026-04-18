import cv2
import numpy as np
from tensorflow.keras.models import load_model
import pandas as pd
import json

from sensor_model import predict_internal_defect


# Load CNN surface defect model
model = load_model("mvtec_defect_model.keras")

IMG_SIZE = 224

cap = cv2.VideoCapture(0)


while True:

    ret, frame = cap.read()

    if not ret:
        break

    img = cv2.resize(frame,(IMG_SIZE,IMG_SIZE))
    img = img/255.0
    img = np.expand_dims(img,axis=0)

    prediction = model.predict(img,verbose=0)

    surface_prob = prediction[0][0]

    if surface_prob > 0.5:
        surface_status = "DEFECT"
    else:
        surface_status = "NORMAL"


    # Simulated sensor metrics
    m1 = 200000000
    m2 = 55
    m3 = 0
    m4 = 52
    m5 = 6
    m6 = 407438
    m7 = 0
    m8 = 0
    m9 = 7


    internal_pred, sensor_prob = predict_internal_defect(
        m1,m2,m3,m4,m5,m6,m7,m8,m9
    )


    combined_risk = (surface_prob + sensor_prob) / 2


    if combined_risk > 0.7:
        system_status = "DEFECT RISK"
    else:
        system_status = "SYSTEM NORMAL"


    machine_state = {
        "temperature":50,
        "rpm":2700,
        "load":450,
        "vibration":1
    }


    # -------------------------------
    # Threshold Definitions
    # -------------------------------
    thresholds = {
        "temperature":45,
        "rpm":2500,
        "load":400,
        "vibration":0
    }


    # -------------------------------
    # Convert to DataFrame (ML Input)
    # -------------------------------
    input_data = pd.DataFrame([machine_state])


    # -------------------------------
    # Threshold Violation Check
    # -------------------------------
    alerts = []

    if machine_state["temperature"] > thresholds["temperature"]:
        alerts.append("temperature")

    if machine_state["rpm"] > thresholds["rpm"]:
        alerts.append("rpm")

    if machine_state["load"] > thresholds["load"]:
        alerts.append("load")

    if machine_state["vibration"] > thresholds["vibration"]:
        alerts.append("vibration")


    risk_score = int(combined_risk*100)
    health_score = 100-risk_score


    print("\nMachine State:")
    print(machine_state)

    print("\nSurface Defect Probability:",round(surface_prob*100,2),"%")
    print("Internal Defect Probability:",round(sensor_prob*100,2),"%")

    print("\nDefect Risk Score:",risk_score)
    print("Machine Health Score:",health_score)


    # -------------------------------
    # Combined ML + Threshold Logic
    # -------------------------------
    if surface_prob > 0.7 or sensor_prob > 0.7 or alerts:

        print("⚠ Defect risk detected. Applying correction logic...")


        if "temperature" in alerts:
            machine_state["temperature"] -= 3
            print("Reducing temperature")

        if "rpm" in alerts:
            machine_state["rpm"] -= 200
            print("Reducing RPM")

        if "load" in alerts:
            machine_state["load"] -= 50
            print("Reducing mechanical load")

        if "vibration" in alerts:
            machine_state["rpm"] -= 100
            print("Reducing RPM to stabilize vibration")


    print("\nUpdated Machine State:")
    for key, value in machine_state.items():
        print(f"{key.capitalize()}: {value}")


    # -------------------------------
    # Save Build Report
    # -------------------------------
    build_log = {
        "machine_state": machine_state,
        "surface_defect_probability": float(surface_prob),
        "internal_defect_probability": float(sensor_prob)
    }

    with open("build_report.json","w") as file:
        json.dump(build_log,file,indent=4)


    cv2.putText(frame,f"Surface Prob: {surface_prob:.2f}",(20,40),
                cv2.FONT_HERSHEY_SIMPLEX,0.7,(0,255,0),2)

    cv2.putText(frame,f"Sensor Prob: {sensor_prob:.2f}",(20,80),
                cv2.FONT_HERSHEY_SIMPLEX,0.7,(255,255,0),2)

    cv2.putText(frame,f"System: {system_status}",(20,120),
                cv2.FONT_HERSHEY_SIMPLEX,0.8,(0,0,255),2)

    cv2.imshow("Smart Manufacturing Monitor",frame)

    if cv2.waitKey(1)==27:
        break


cap.release()
cv2.destroyAllWindows()