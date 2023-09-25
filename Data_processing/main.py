import process_data

if __name__ == '__main__':
    regex = "F:\Dataset\\train\\annos\*.json"
    clothes = process_data.read_files(regex)
    categorised_clothes = process_data.split_categories(clothes)
    print(len(categorised_clothes))
