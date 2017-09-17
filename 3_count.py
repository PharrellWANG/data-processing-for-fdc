# ==============================================================================
# Author: Pharrell_WANG
# Date: 2017/6/28
# ==============================================================================
import os
from utils.mode_counter import mode_counter

homedir = os.environ['HOME']
# input_file = homedir + '/data/smooth_removed/32_classes__ave_90_size_08_files.csv'
input_file = '/Users/pharrell_wang/data/last_trial/kendo/validate_08x08.csv'
# input_file = '/Users/Pharrell_WANG/data/smooth_removed/28_classes__ave_90_size_08_files__after_grouping.csv'
x_ordered_dict = mode_counter(INPUT_FILE=input_file)
