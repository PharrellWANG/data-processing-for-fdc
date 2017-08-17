# ------------------------------------------------------------------------------
# Author: Pharrell_WANG
#   Date: 2017/6/28
# ------------------------------------------------------------------------------
from csv_mode_counter import csv_mode_preprocessing

# ORIG_DATA = '/Users/Pharrell_WANG/PycharmProjects/fdc-tf-data-preprocessing/data_after_step2_remove/comma_removed_size_16.csv'
ORIG_DATA = '/Users/Pharrell_WANG/PycharmProjects/fdc-tf-data-preprocessing/train_data/training_data_16x16.csv'
x_ordered_dict = csv_mode_preprocessing(OUTPUT_FILE=ORIG_DATA)
