# ==============================================================================
# Author: Pharrell_WANG
# Date: 2017/6/28
# ==============================================================================
import os
from utils.comma_remover import comma_remover

homedir = os.environ['HOME']
list_of_input_files = [
    homedir + '/data/newspaper/mixed_data_1.csv',
    homedir + '/data/newspaper/mixed_data_2.csv',
    homedir + '/data/newspaper/mixed_data_3.csv',
]
list_of_output_files = [
    homedir + '/data/newspaper/cr_mixed_data_1.csv',
    homedir + '/data/newspaper/cr_mixed_data_2.csv',
    homedir + '/data/newspaper/cr_mixed_data_3.csv',
]

for x in range(len(list_of_input_files)):
    comma_remover(list_of_input_files[x], list_of_output_files[x])
