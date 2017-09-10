# ==============================================================================
# Author: Pharrell_WANG
# Date: 2017/6/28
# ==============================================================================
import os
from utils.edge_strength_analysis import edge_analyzer

homedir = os.environ['HOME']
input_file = homedir + '/data/step2_output/size_16_files.csv'
x_ordered_dict, strength_dict = edge_analyzer(INPUT_FILE=input_file)
