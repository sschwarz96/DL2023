import os
import cv2
import numpy as np


directory = "/Users/ludvigbennbom/Desktop/dataset500/masks"
width = 224
height = 224
layers = 11 #10 categories and background

color_dict = {
    0: (255, 0, 0),    # Red
    1: (0, 255, 0),    # Green
    2: (0, 0, 255),    # Blue
    3: (255, 255, 0),  # Yellow
    4: (255, 0, 255),  # Magenta
    5: (0, 128, 0),  # CYAN
    6: (128, 0, 0),    # Maroon
    7: (0, 255, 255),    # Green (Dark)
    8: (0, 0, 128),    # Navy
    9: (128, 128, 0),  # Olive
    10: (0,0,0)         # Black
}


def find_matching_category(color_to_check):
    for category, color in color_dict.items():
        if color_to_check == color:
            return category
    return None

def get_file_paths():
    file_paths = os.listdir(directory)
    return file_paths

def create_onehot_masks():
    file_paths = get_file_paths()
    for file in file_paths:
        if not file.startswith('.'):

            image = cv2.imread(directory+"/"+file)
            mask = np.zeros((width, height, layers), dtype=np.uint8)

            for x in range(width):
                for y in range(height):

                    b, g, r = image[y, x]
                    matching_category = find_matching_category((r, g, b))

                    if matching_category is not None:
                        mask[y,x,matching_category] = 1
            np.save('/Users/ludvigbennbom/Desktop/dataset500/onehotstest/' + file.split(".")[0] + '.npy', mask)
create_onehot_masks()
