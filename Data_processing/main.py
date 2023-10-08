from typing import List

import process_data

if __name__ == '__main__':
    regex = "F:\Dataset\\train\\annos\*.json"
    clothes = process_data.read_files(regex)
    categorised_clothes: List[process_data.CategorisedData] = process_data.split_categories(clothes)
    categorised_clothes.sort(key=lambda x: x.cat_id)
    categorised_clothes.pop(12)
    categorised_clothes.pop(5)
    categorised_clothes.pop(2)
    print(categorised_clothes)
