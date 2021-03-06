# import csv
"""
this file is for splitting depth classes into two classes:
mode0, 1 and OTHERS
"""
import pandas as pd
import os
import sys
import datetime

SHAPE = 16
homedir = os.environ['HOME']
input_files = [
    # homedir + '/data/step2_output/size_%s_files.csv' % SHAPE
    '/Users/Pharrell_WANG/data/two_classes/separate_classes/train_16x16.csv',
    '/Users/Pharrell_WANG/data/two_classes/separate_classes/test_16x16.csv',
    '/Users/Pharrell_WANG/data/two_classes/separate_classes/validation_16x16.csv'
]


output_files = [
    homedir + '/data/two_classes/train_16x16_homo_and_edge.csv',
    homedir + '/data/two_classes/test_16x16_homo_and_edge.csv',
    homedir + '/data/two_classes/validation_16x16_homo_and_edge.csv'
]

for file_index in range(len(input_files)):
    start = datetime.datetime.now()
    print("now reading: " + str(input_files[file_index]))
    df = pd.read_csv(input_files[file_index], header=None)

    number_of_rows = len(df.index)
    print('number_of_rows : ' + str(number_of_rows))

    for x in range(number_of_rows):
        sys.stdout.write(
            '\r>> Converting rows %d/%d' % (x + 1, number_of_rows))
        sys.stdout.flush()
        if df[SHAPE*SHAPE][x] == 0 or df[SHAPE*SHAPE][x] == 1:
            df[SHAPE*SHAPE][x] = 0
        else:
            df[SHAPE*SHAPE][x] = 1
    print('\n')
    print('now write into : ' + str(
        output_files[file_index]) + ' . Please wait a while.')
    print('>>>......')
    df.to_csv(output_files[file_index], header=None, index=False)
    end = datetime.datetime.now()
    print('duration: ' + str(end-start))
    print('END.')
    #
