import os
import numpy as np
from sklearn.model_selection import train_test_split
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Conv2D, MaxPooling2D, Flatten, Dense
from utils import preprocess_image

def load_data():
    data = []
    labels = []

    for category in ["normal", "defect"]:
        path = f"dataset/{category}"
        label = 0 if category == "normal" else 1

        for img in os.listdir(path):
            img_path = os.path.join(path, img)

            try:
                image = preprocess_image(img_path)
                data.append(image)
                labels.append(label)
            except:
                pass

    return np.array(data), np.array(labels)

def build_model():
    model = Sequential([
        Conv2D(32, (3,3), activation='relu', input_shape=(128,128,3)),
        MaxPooling2D(2,2),

        Conv2D(64, (3,3), activation='relu'),
        MaxPooling2D(2,2),

        Conv2D(128, (3,3), activation='relu'),
        MaxPooling2D(2,2),

        Flatten(),
        Dense(128, activation='relu'),
        Dense(1, activation='sigmoid')
    ])

    model.compile(
        optimizer='adam',
        loss='binary_crossentropy',
        metrics=['accuracy']
    )

    return model

def train_model():
    X, y = load_data()

    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2
    )

    model = build_model()

    model.fit(
        X_train, y_train,
        epochs=10,
        validation_data=(X_test, y_test)
    )

    loss, acc = model.evaluate(X_test, y_test)
    print("🔥 Final Accuracy:", acc)

    # 🟢 STEP 1: Evaluation Part Added
    from sklearn.metrics import classification_report, confusion_matrix

    # Predictions
    y_pred = model.predict(X_test)
    y_pred = (y_pred > 0.5).astype(int)

    print("\n📊 Confusion Matrix:")
    print(confusion_matrix(y_test, y_pred))

    print("\n📊 Classification Report:")
    print(classification_report(y_test, y_pred))

    model.save("model.h5")

    return model

if __name__ == "__main__":
    train_model()