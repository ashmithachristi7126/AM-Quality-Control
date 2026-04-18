import os
import shutil

MVTEC_PATH = "mvtec"
OUTPUT_PATH = "dataset_all"

normal_folder = os.path.join(OUTPUT_PATH, "normal")
defect_folder = os.path.join(OUTPUT_PATH, "defect")

os.makedirs(normal_folder, exist_ok=True)
os.makedirs(defect_folder, exist_ok=True)

for category in os.listdir(MVTEC_PATH):

    category_path = os.path.join(MVTEC_PATH, category)

    if not os.path.isdir(category_path):
        continue

    print("Processing:", category)

    # train/good → normal
    train_good = os.path.join(category_path, "train", "good")

    if os.path.exists(train_good):
        for img in os.listdir(train_good):
            shutil.copy(os.path.join(train_good, img), normal_folder)

    # test folder
    test_path = os.path.join(category_path, "test")

    if not os.path.exists(test_path):
        continue

    for defect_type in os.listdir(test_path):

        defect_path = os.path.join(test_path, defect_type)

        if not os.path.isdir(defect_path):
            continue

        for img in os.listdir(defect_path):

            src = os.path.join(defect_path, img)

            if defect_type == "good":
                shutil.copy(src, normal_folder)
            else:
                shutil.copy(src, defect_folder)

print("Dataset creation completed.")