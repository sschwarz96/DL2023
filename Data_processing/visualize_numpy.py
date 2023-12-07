import numpy as np
import matplotlib.pyplot as plt
import os

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

folder_path = "/Users/ludvigbennbom/Desktop/dataset500/onehots"
file_paths = os.listdir(folder_path)
def visualize_numpy(npy):
    
    labels = np.argmax(npy, axis=-1)
    rgb_image = np.zeros((*labels.shape, 3), dtype=np.uint8)

    for class_label, color in color_dict.items():
        mask = labels == class_label
        rgb_image[mask] = color

    plt.imshow(rgb_image)
    plt.title('Segmentation Mask')
    plt.show()

def loop_through_masks(file_list):
    for file_name in file_list:
        file_path = os.path.join(folder_path, file_name)
        npy = np.load(file_path)
        visualize_numpy(npy)


loop_through_masks(file_paths)