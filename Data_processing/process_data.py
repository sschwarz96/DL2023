import glob
import json
import math
from dataclasses import dataclass
from typing import List


@dataclass()
class CategorisedData:
    cat_id: int
    file_names: []


def extract_file_name(path):
    file_name = path.split('\\')[-1]
    file_name = file_name.split('.')[0]
    return file_name


def read_files(regex):
    paths = glob.glob(regex)
    clothes_data = []
    for path in paths:
        with open(path, 'r') as file:
            piece_of_clothing = json.load(file)
        piece_of_clothing['file_name'] = extract_file_name(path)
        clothes_data.append(piece_of_clothing)
    return clothes_data


def write_data(categorised_list: List[CategorisedData]):
    with open('F:\Dataset\small_dataset\data_summary.json', 'w') as outfile:
        outfile.write(json.dumps(categorised_list, default=lambda obj: obj.__dict__))


def get_index(categorised_list: List[CategorisedData], cat_id):
    for i in range(0, len(categorised_list) - 1):
        category = categorised_list[i]
        if category.cat_id == cat_id:
            return i

    return False


def split_categories(data):
    categorised_list: List[CategorisedData] = []
    for item in data:
        indices = list(map(lambda x: x.cat_id, categorised_list))
        category_id = item['item1']['category_id']
        if category_id not in indices:
            category_data = CategorisedData(category_id, [item['file_name']])
            categorised_list.append(category_data)
        else:
            index = indices.index(category_id)
            categorised_list[index].file_names.append(item['file_name'])
    return categorised_list


def remove_categories(categorised_clothes: List[CategorisedData]):
    categorised_clothes.pop(12)
    categorised_clothes.pop(5)
    categorised_clothes.pop(2)
    return categorised_clothes


def select_smaller_data_set(categorised_clothes: List[CategorisedData]):
    for item in categorised_clothes:
        file_length = len(item.file_names)
        step_size = 1
        if file_length > 3000:
            step_size = math.floor(file_length / 3000)
        item.file_names = item.file_names[0: file_length: step_size]
        item.file_names = item.file_names[0: 3000]
    return categorised_clothes


def create_smaller_data_set():
    regex = "F:\Dataset\\train\\annos\*.json"
    clothes = read_files(regex)
    categorised_clothes: List[CategorisedData] = split_categories(clothes)
    categorised_clothes.sort(key=lambda x: x.cat_id)
    categorised_clothes = remove_categories(categorised_clothes)
    categorised_clothes = select_smaller_data_set(categorised_clothes)
    write_data(categorised_clothes)
