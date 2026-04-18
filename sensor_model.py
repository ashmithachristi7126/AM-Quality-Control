import joblib
import numpy as np

# -------------------------------
# Load trained sensor model
# -------------------------------
def load_sensor_model():

    model = joblib.load("sensor_model.pkl")

    return model


# -------------------------------
# Predict internal defect
# -------------------------------
def predict_internal_defect(model, m1, m2, m3, m4, m5, m6, m7, m8, m9):

    data = np.array([[m1, m2, m3, m4, m5, m6, m7, m8, m9]])

    prediction = model.predict(data)[0]

    probability = model.predict_proba(data)[0][1]

    return prediction, probability