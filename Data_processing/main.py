import numpy as np

import process_data
from Data_processing import retrieve_data

if __name__ == '__main__':
    process_data.create_smaller_data_set()
    retrieve_data.retrieve_photos()
    retrieve_data.add_json_data()
   # path = '/home/simon/Downloads/onehot_encoded_masks/onehot_encoded_masks/000001_mask.npy'
