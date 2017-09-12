# ==============================================================================
# Author: Pharrell_WANG
# Date: 2017/6/28
# ==============================================================================
import os
from utils.mode_counter import mode_counter

homedir = os.environ['HOME']
input_file = homedir + '/data/smooth_removed/ave_90_size_08_files.csv'
# input_file = '/Users/Pharrell_WANG/data/two_classes/16x16_validation.csv'
# input_file = '/Users/Pharrell_WANG/data/two_classes/32x32_homo_edge/train.csv'
x_ordered_dict = mode_counter(INPUT_FILE=input_file)
