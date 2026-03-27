import cv2
import os
from db_utils import save_image
folder_path = r"C:\Users\Rudraksh Sharma\Downloads\archive\Formula One Cars"
for file in os.listdir(folder_path):
    if file.endswith((".jpg", ".png", ".jpeg")):
        path = os.path.join(folder_path, file)

        img = cv2.imread(path)
        save_image(file, img)

        print(f"Saved: {file}")