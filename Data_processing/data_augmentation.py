import cv2
import numpy as np
from matplotlib import pyplot as plt
from albumentations import (
    Compose,
    HorizontalFlip,
    ColorJitter,
    Defocus,
    RandomBrightnessContrast,
    CoarseDropout,
    PixelDropout,
    Blur
)
import os

augmentation_pipeline = Compose([
    HorizontalFlip(p=0.5),
    CoarseDropout(p=0.5),
    ColorJitter(p=1, brightness=(0.8, 1), saturation=(0.8, 1), contrast=(0.8, 1), hue=(-0.2, 0.2)),
    RandomBrightnessContrast(p=0.5),
    PixelDropout(p=0.5),
    Blur(p=0.5, blur_limit=(2,6))
])

color_dict = {
    0: (255, 0, 0),  # Red
    1: (0, 255, 0),  # Green
    2: (0, 0, 255),  # Blue
    3: (255, 255, 0),  # Yellow
    4: (255, 0, 255),  # Magenta
    5: (0, 128, 0),  # CYAN
    6: (128, 0, 0),  # Maroon
    7: (0, 255, 255),  # Green (Dark)
    8: (0, 0, 128),  # Navy
    9: (128, 128, 0),  # Olive
    10: (0, 0, 0)  # Black
}

folder_path = "/Users/ludvigbennbom/Desktop/dataset500/onehots"
file_paths = os.listdir(folder_path)


def visualize_numpy(npy):
    labels = np.argmax(npy, axis=-1)
    rgb_image = np.zeros((*labels.shape, 3), dtype=np.uint8)

    for class_label, color in color_dict.items():
        mask = labels == class_label
        rgb_image[mask] = color

    return rgb_image

image_paths = '/Users/ludvigbennbom/Desktop/dataset500/images'
mask_paths = '/Users/ludvigbennbom/Desktop/masks_resized_new'
onehot_masks_path = '/Users/ludvigbennbom/Desktop/dataset500/onehots'
file_paths = os.listdir(onehot_masks_path)

def augment_data(image,mask):

    data = {'image': image, 'mask': mask}
    augmented = augmentation_pipeline(**data)

    augmented_image = augmented['image']
    augmented_mask = augmented['mask']

    plt.subplot(2, 2, 1)
    plt.imshow(image)
    plt.title('Original Image')

    plt.subplot(2, 2, 2)
    plt.imshow(visualize_numpy(mask), cmap='gray')
    plt.title('Original Mask')

    plt.subplot(2, 2, 3)
    plt.imshow(augmented_image)
    plt.title('Augmented Image')

    plt.subplot(2, 2, 4)
    plt.imshow(visualize_numpy(augmented_mask), cmap='gray')
    plt.title('Augmented Mask')

    plt.show()

def loop_augments(file_paths):
    for file_name in file_paths:
        file_name_image = str(file_name.split('_')[0]) + '_image.png'
        image_path = os.path.join(image_paths, file_name_image)
        mask_path = os.path.join(onehot_masks_path, file_name)
        image = cv2.imread(image_path)
        mask = np.load(mask_path)

        augment_data(image,mask)

loop_augments(file_paths)

