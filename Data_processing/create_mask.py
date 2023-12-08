import os
import json
import cv2
import numpy as np

directory = "/Users/ludvigbennbom/Desktop/train/"

colors_rgb = {
    1: (255, 0, 0),    # Red
    2: (0, 255, 0),    # Green
    4: (255, 255, 0),  # Yellow
    5: (255, 0, 255),  # Magenta
    7: (128, 0, 0),    # Maroon
    8: (0, 255, 255),    # Green (Dark)
    9: (0, 0, 128),    # Navy
    10: (128, 128, 0),  # Olive
    11: (0, 0, 255), #BLUE
    12: (0, 128, 0),    #CYANA
}

colors_bgr = {key: (color[2], color[1], color[0]) for key, color in colors_rgb.items()}

def get_file_paths():
    file_paths = os.listdir("/Users/ludvigbennbom/Desktop/small_dataset/json")
    return file_paths

def create_mask():
    json_file_paths = get_file_paths()

    for file_name in json_file_paths:
        if not file_name.startswith("."):
            data = json.load(open("/Users/ludvigbennbom/Desktop/small_dataset/json/" + file_name))
            img_path = file_name.split(".")[0] + ".jpg"
            img = cv2.imread("/Users/ludvigbennbom/Desktop/train/image/" + img_path)
            mask = np.zeros_like(img, dtype=np.uint8)
            for key in data:
                if key.startswith("item"):
                    segmentation_list = data[key]["segmentation"]
                    category_id = data[key]["category_id"]
                    color = colors_bgr.get(category_id, (0, 0, 0))
                    for polygon_coords in segmentation_list:
                        polygon_coords = np.array(polygon_coords, dtype=np.float32).reshape((-1, 2))
                        polygon_coords = polygon_coords.astype(np.int32)

                        cv2.fillPoly(mask, [polygon_coords], color)

            resized_mask = cv2.resize(mask, (224, 224), interpolation=cv2.INTER_NEAREST)
            resized_image = cv2.resize(img, (224, 224), interpolation=cv2.INTER_NEAREST)
            cv2.imwrite('/Users/ludvigbennbom/Desktop/dataset_inter_nearest/masks_30k/' + file_name.split(".")[0] + '_mask.png', resized_mask)
            cv2.imwrite('/Users/ludvigbennbom/Desktop/dataset_inter_nearest/images_30k/' + file_name.split(".")[0] + '_image.png', resized_image)


def create_file_paths():
    data = json.load(open("/Users/ludvigbennbom/Desktop/dataset500/data_summary.json"))
    file_paths = []
    for category in data:
        file_names = category["file_names"]
        for file_name in file_names:
            file_paths.append(file_name)

create_mask()