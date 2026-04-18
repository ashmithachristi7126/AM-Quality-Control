import os
import cv2
import numpy as np
from tensorflow.keras.models import load_model

# Path to MVTec dataset
MVTEC_PATH = "mvtec"

# Load trained model
model = load_model("mvtec_defect_model.keras")
IMG_SIZE = 224

correct = 0
total = 0


def predict_image(image_path, actual_label):
    global correct, total

    img = cv2.imread(image_path)

    if img is None:
        return

    img = cv2.resize(img, (IMG_SIZE, IMG_SIZE))
    img = img / 255.0
    img = np.expand_dims(img, axis=0)

    prediction = model.predict(img, verbose=0)

    if prediction[0][0] > 0.5:
        predicted_label = "defect"
    else:
        predicted_label = "normal"

    print(image_path, "| Actual:", actual_label, "| Predicted:", predicted_label)

    if predicted_label == actual_label:
        correct += 1

    total += 1


# Loop through categories
for category in os.listdir(MVTEC_PATH):

    test_folder = os.path.join(MVTEC_PATH, category, "test")

    if not os.path.isdir(test_folder):
        continue

    print("\nChecking category:", category)

    for defect_type in os.listdir(test_folder):

        defect_path = os.path.join(test_folder, defect_type)

        if not os.path.isdir(defect_path):
            continue

        if defect_type == "good":
            actual_label = "normal"
        else:
            actual_label = "defect"

        for img_name in os.listdir(defect_path):

            img_path = os.path.join(defect_path, img_name)

            predict_image(img_path, actual_label)


accuracy = correct / total

print("\n==========================")
print("Total Images:", total)
print("Correct Predictions:", correct)
print("Accuracy:", accuracy)
print("==========================")