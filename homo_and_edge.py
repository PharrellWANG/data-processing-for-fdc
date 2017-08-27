# import csv
"""
this file is for splitting depth classes into two classes:
mode0, 1 and OTHERS
"""
import pandas as pd
import os
import datetime

SHAPE = 16
homedir = os.environ['HOME']
input_files = [
    homedir + '/data/step2_output/size_%s_files.csv' % SHAPE
]

output_files = [
    homedir + '/data/two_classes/%sx%s_2_class_homo_and_edge.csv' % (SHAPE, SHAPE)
]

for file_index in range(len(input_files)):
    now = datetime.datetime.now()
    print('start: ' + str(now))
    print("now we are reading: " + str(input_files[file_index]))
    df = pd.read_csv(input_files[file_index], header=None)

    number_of_rows = len(df.index)
    print('=======================')
    print('number_of_rows : ' + str(number_of_rows))
    print('=======================')

    for x in range(number_of_rows):
        if x % 50000 == 0:
            print('row index x now is : ' + str(x))
        if df[SHAPE*SHAPE][x] == 0 or df[SHAPE*SHAPE][x] == 1:
            df[SHAPE*SHAPE][x] = 0
        else:
            df[SHAPE*SHAPE][x] = 1
    print('')
    print('now we are writing: ' + str(
        output_files[file_index]) + ' . Please wait a few seconds...')
    print('............')
    df.to_csv(output_files[file_index], header=None, index=False)
    now = datetime.datetime.now()
    print('end: ' + str(now))
    print('==============')
    #
