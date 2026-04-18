import os
import shutil

mvtec_path = "mvtec"
neu_path = "neu_dataset"

normal_dest = "dataset/normal"
defect_dest = "dataset/defect"

os.makedirs(normal_dest, exist_ok=True)
os.makedirs(defect_dest, exist_ok=True)

counter = 0

# -------- MVTec NORMAL --------
for root, dirs, files in os.walk(mvtec_path):
    if "good" in root:
        for file in files:
            if file.endswith((".png", ".jpg")):
                src = os.path.join(root, file)
                dst = os.path.join(normal_dest, f"normal_{counter}.jpg")
                shutil.copy(src, dst)
                counter += 1

# -------- MVTec DEFECT --------
for root, dirs, files in os.walk(mvtec_path):
    if "test" in root and "good" not in root:
        for file in files:
            if file.endswith((".png", ".jpg")):
                src = os.path.join(root, file)
                dst = os.path.join(defect_dest, f"defect_{counter}.jpg")
                shutil.copy(src, dst)
                counter += 1

# -------- NEU DEFECT --------
for root, dirs, files in os.walk(neu_path):
    if "images" in root:
        for file in files:
            if file.endswith((".png", ".jpg")):
                src = os.path.join(root, file)
                dst = os.path.join(defect_dest, f"defect_{counter}.jpg")
                shutil.copy(src, dst)
                counter += 1

print("✅ Dataset prepared successfully!")