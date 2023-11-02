import json
import os
from typing import List
import shutil

from process_data import CategorisedData

new_data_home = '/home/simon/smaller_dataset/'
image_home = '/home/simon/Downloads/small_dataset/resized_images/'
json_home = '/home/simon/Downloads/small_dataset/json/'


def retrieve_photos():
    categories: List[CategorisedData] = read_categories()
    copy_photos(categories)


def add_json_data():
    categories: List[CategorisedData] = read_categories()
    copy_jsons(categories)


def copy_jsons(categories: List[CategorisedData]):
    json_dir = new_data_home + 'json'
    os.makedirs(json_dir, exist_ok=True)
    for category in categories:
        file_names = list(map(lambda file_name: add_file_ending(file_name, file_ending='.json'), category['file_names']))
        for file_name in file_names:
            copy_file(file_name, json_dir, json_home)


def read_categories():
    with open(new_data_home + 'data_summary.json', 'r') as file:
        categories: List[CategorisedData] = json.load(file)
        return categories


def copy_photos(categories: List[CategorisedData]):
    i = 1
    image_dir = new_data_home + 'images'
    os.makedirs(image_dir, exist_ok=True)
    for category in categories:
        file_names = list(map(add_file_ending, category['file_names']))
        for file_name in file_names:
            copy_file(file_name, image_dir, image_home)
        i += 1


def copy_file(file_name, dest_dir, home):
    src_path = home + file_name
    dest_path = dest_dir + '/'
    shutil.copy(src_path, dest_path)


def add_file_ending(file_name: str, file_ending='_mask.png'):
    return file_name + file_ending
