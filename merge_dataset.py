import os
import shutil

mvtec_path = "mvtec"
target_defect = "dataset/defect"

for category in os.listdir(mvtec_path):

    test_path = os.path.join(mvtec_path, category, "test")

    if os.path.exists(test_path):

        for defect_type in os.listdir(test_path):

            # Skip normal images
            if defect_type == "good":
                continue

            defect_path = os.path.join(test_path, defect_type)

            for img in os.listdir(defect_path):

                src = os.path.join(defect_path, img)

                # 🔥 IMPORTANT: rename to avoid duplicate names
                new_name = category + "_" + defect_type + "_" + img
                dst = os.path.join(target_defect, new_name)

                shutil.copy(src, dst)

print("✅ MVTec defect images copied!")

neu_path = "neu_dataset"

for defect_type in os.listdir(neu_path):

    defect_path = os.path.join(neu_path, defect_type)

    for img in os.listdir(defect_path):

        src = os.path.join(defect_path, img)

        # 🔥 rename to avoid duplicates
        new_name = "neu_" + defect_type + "_" + img
        dst = os.path.join(target_defect, new_name)

        shutil.copy(src, dst)

print("✅ NEU defect images copied!")

target_normal = "dataset/normal"

for category in os.listdir(mvtec_path):

    good_path = os.path.join(mvtec_path, category, "train", "good")

    if os.path.exists(good_path):

        for img in os.listdir(good_path):

            src = os.path.join(good_path, img)

            new_name = category + "_good_" + img
            dst = os.path.join(target_normal, new_name)

            shutil.copy(src, dst)

print("✅ Normal images copied!")