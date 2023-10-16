import os
import json
import cv2
import numpy as np
from PIL import Image

directory = "/Users/ludvigbennbom/Desktop/train/"

category_colors = {
    1: (255, 0, 0),    # Red
    2: (0, 255, 0),    # Green
    3: (0, 0, 255),    # Blue
    4: (255, 255, 0),  # Yellow
    5: (255, 0, 255),  # Magenta
    6: (0, 128, 0),  # Cyan
    7: (128, 0, 0),    # Maroon
    8: (0, 255, 255),    # Green (Dark)
    9: (0, 0, 128),    # Navy
    10: (128, 128, 0),  # Olive
    11: (128, 0, 128),  # Purple
    12: (0, 128, 128),  # Teal
    13: (128, 128, 128) # Gray
}
def get_file_paths():
    file_paths = os.listdir("/Users/ludvigbennbom/Desktop/small_dataset/json")
    return file_paths

def create_mask():
    json_file_paths = get_file_paths()

    for file_name in json_file_paths:
        data = json.load(open("/Users/ludvigbennbom/Desktop/small_dataset/json/" + file_name))
        img_path = file_name.split(".")[0] + ".jpg"
        img = cv2.imread("/Users/ludvigbennbom/Desktop/train/image/" + img_path)
        mask = np.zeros_like(img, dtype=np.uint8)
        for key in data:
            if key.startswith("item"):
                segmentation_list = data[key]["segmentation"]
                category_id = data[key]["category_id"]
                color = category_colors.get(category_id, (0, 0, 0))
                ##points = np.array(segmentation_list)
                for polygon_coords in segmentation_list:
                    polygon_coords = np.array(polygon_coords, dtype=np.float32).reshape((-1, 2))
                    polygon_coords = polygon_coords.astype(np.int32)  

                    cv2.fillPoly(mask, [polygon_coords], color)  

                # Displaying the image
        mask_image = Image.fromarray(mask)
        mask_image.save('/Users/ludvigbennbom/Desktop/small_dataset/masks/' + file_name.split(".")[0] + '_mask.png')  # Save with a unique name


create_mask()