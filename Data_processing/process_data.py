import glob
import json
from typing import List


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
        piece_of_clothing = json.load(open(path))
        piece_of_clothing['file_name'] = extract_file_name(path)
        clothes_data.append(piece_of_clothing)
    return clothes_data


def get_index(categorised_list: List[CategorisedData], cat_id):
    for i in range(0, len(categorised_list) - 1):
        category = categorised_list[i]
        if category.cat_id == cat_id:
            return i

    return False

#def add_to_category(category_id: int, category_list: List[CategorisedData] ):


def split_categories(data):
    categorised_list: List[CategorisedData] = []
    for item in data:
        indices = list(map(lambda x: x.cat_id, categorised_list))
        category_id = item['item1']['category_id']
        if category_id not in indices:
            category_data = CategorisedData()
            category_data.cat_id = category_id
            category_data.file_names = [item['file_name']]
            categorised_list.append(category_data)
        elif len(categorised_list[indices.index(category_id)].file_names) < 3000:
            index = indices.index(category_id)
            categorised_list[index].file_names.append(item['file_name'])
        else:
            try:
                category_id = item['item2']['category_id']
                index = indices.index(category_id)
                categorised_list[index].file_names.append(item['file_name'])
            except KeyError:
                category_id = item['item1']['category_id']
                index = indices.index(category_id)
                categorised_list[index].file_names.append(item['file_name'])
    return categorised_list
