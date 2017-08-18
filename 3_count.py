# ------------------------------------------------------------------------------
# Author: Pharrell_WANG
#   Date: 2017/6/28
# ------------------------------------------------------------------------------
import os
from utils.mode_counter import mode_counter

homedir = os.environ['HOME']
# input_file = homedir + '/data/step2_output/size_32_files.csv'
input_file = '/Users/pharrell_wang/data/step3_output/32x32/data_for_training/train_32x32.csv'
x_ordered_dict = mode_counter(INPUT_FILE=input_file)
