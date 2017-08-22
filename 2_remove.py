# ------------------------------------------------------------------------------
# Author: Pharrell_WANG
#   Date: 2017/6/28
# ------------------------------------------------------------------------------
import os
from utils.comma_remover import comma_remover

homedir = os.environ['HOME']
list_of_input_files = [homedir + '/data/step1_output/size_08_files.csv',
                       homedir + '/data/step1_output/size_16_files.csv',
                       homedir + '/data/step1_output/size_32_files.csv',
                       homedir + '/data/step1_output/size_64_files.csv'
                       ]
list_of_output_files = [homedir + '/data/step2_output/size_08_files.csv',
                        homedir + '/data/step2_output/size_16_files.csv',
                        homedir + '/data/step2_output/size_32_files.csv',
                        homedir + '/data/step2_output/size_64_files.csv'
                        ]

# list_of_input_files = ['/Users/pharrell_wang/Downloads/mixed_data_1.csv']
# list_of_output_files = ['/Users/pharrell_wang/Downloads/mixed_32x32.csv']

for x in range(len(list_of_input_files)):
    comma_remover(list_of_input_files[x], list_of_output_files[x])
