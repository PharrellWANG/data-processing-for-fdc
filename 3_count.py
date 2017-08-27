# ==============================================================================
# Author: Pharrell_WANG
# Date: 2017/6/28
# ==============================================================================
import os
from utils.mode_counter import mode_counter

homedir = os.environ['HOME']
# input_file = homedir + '/data/step2_output/size_32_files.csv'
input_file = '/Users/Pharrell_WANG/data/two_classes/16_homo_edge.csv'
x_ordered_dict = mode_counter(INPUT_FILE=input_file)
