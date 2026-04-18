import os
import shutil

# original mvtec dataset
SOURCE_DIR = "mvtec"

# new dataset folder
TARGET_DIR = "dataset_all"

os.makedirs(TARGET_DIR, exist_ok=True)

categories = os.listdir(SOURCE_DIR)

for category in categories:

    category_path = os.path.join(SOURCE_DIR, category)

    if not os.path.isdir(category_path):
        continue

    print("Processing:", category)

    defect_dir = os.path.join(TARGET_DIR, category, "defect")
    normal_dir = os.path.join(TARGET_DIR, category, "normal")

    os.makedirs(defect_dir, exist_ok=True)
    os.makedirs(normal_dir, exist_ok=True)

    # normal images (good)
    good_path = os.path.join(category_path, "train", "good")

    if os.path.exists(good_path):

        for img in os.listdir(good_path):

            src = os.path.join(good_path, img)
            dst = os.path.join(normal_dir, img)

            shutil.copy(src, dst)

    # defect images
    test_path = os.path.join(category_path, "test")

    if os.path.exists(test_path):

        for defect_type in os.listdir(test_path):

            if defect_type == "good":
                continue

            defect_folder = os.path.join(test_path, defect_type)

            for img in os.listdir(defect_folder):

                src = os.path.join(defect_folder, img)
                dst = os.path.join(defect_dir, img)

                shutil.copy(src, dst)

print("Dataset prepared successfully!")