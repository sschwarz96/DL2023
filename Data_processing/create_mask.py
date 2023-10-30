import os
import json
import cv2
import numpy as np
from PIL import Image

directory = "F:/Dataset/small_dataset/"

category_colors = {
    1: (255, 0, 0),  # Red
    2: (0, 255, 0),  # Green
    3: (0, 0, 255),  # Blue
    4: (255, 255, 0),  # Yellow
    5: (255, 0, 255),  # Magenta
    6: (0, 128, 0),  # Cyan
    7: (128, 0, 0),  # Maroon
    8: (0, 255, 255),  # Green (Dark)
    9: (0, 0, 128),  # Navy
    10: (128, 128, 0),  # Olive
    11: (128, 0, 128),  # Purple
    12: (0, 128, 128),  # Teal
    13: (128, 128, 128)  # Gray
}


def get_file_paths():
    file_paths = os.listdir(directory + "json")
    return file_paths


def create_mask():
    json_file_paths = get_file_paths()

    for file_name in json_file_paths:
        data = json.load(open(directory + "json/" + file_name))
        img_path = file_name.split(".")[0] + ".jpg"
        img = cv2.imread(directory + "/images/" + img_path)
        img = cv2.resize(img, (224, 224), interpolation=cv2.INTER_AREA)
        cv2.imwrite(directory + '/resized_images/' + file_name.split(".")[
            0] + '_mask.png', img)  # Save with a unique name


create_mask()
