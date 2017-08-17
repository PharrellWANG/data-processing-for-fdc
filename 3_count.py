# ------------------------------------------------------------------------------
# Author: Pharrell_WANG
#   Date: 2017/6/28
# ------------------------------------------------------------------------------
import os
from utils.mode_counter import mode_counter

homedir = os.environ['HOME']
input_file = homedir + '/data/step2_output/size_16_files.csv'

x_ordered_dict = mode_counter(INPUT_FILE=input_file)
