import cv2
import numpy as np
from db import collection
from model import extract_features

def save_image(name, image):
    _, buffer = cv2.imencode('.png', image)
    features = extract_features(image)

    document = {
        "name": name,
        "image": buffer.tobytes(),
        "features": features.tolist()
    }

    collection.insert_one(document)


def load_images():
    data = collection.find()

    images = []
    for item in data:
        img_array = np.frombuffer(item["image"], np.uint8)
        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)

        features = np.array(item["features"])

        images.append((item["name"], img, features))

    return images