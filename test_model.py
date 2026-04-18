import cv2
import numpy as np
from tensorflow.keras.models import load_model
from utils import preprocess_image

model = load_model("model.h5")

img_path = "dataset/defect/your_image.jpg"  # change image

img = preprocess_image(img_path)
img = np.reshape(img, (1,128,128,3))

pred = model.predict(img)

if pred[0][0] > 0.5:
    print("❌ DEFECT")
else:
    print("✅ NORMAL")

cv2.imshow("Image", cv2.imread(img_path))
cv2.waitKey(0)
cv2.destroyAllWindows()