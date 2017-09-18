"""
Final classes: 32 classes. [0, 31]
"""
# import csv
import pandas as pd
import os
import sys
import datetime

homedir = os.environ['HOME']
list_of_input = [
    homedir + '/data/last_trial/step5_output/train_08x08.csv',
    homedir + '/data/last_trial/step5_output/test_08x08.csv',
    homedir + '/data/last_trial/step5_output/val_08x08.csv',
]
list_of_output = [
    homedir + '/data/last_trial/step6_output/train_08x08.csv',
    homedir + '/data/last_trial/step6_output/test_08x08.csv',
    homedir + '/data/last_trial/step6_output/val_08x08.csv',
]

for file_index in range(len(list_of_input)):
    start_timestamp = datetime.datetime.now()
    print('=================================================')
    print('start at: ')
    print(start_timestamp)
    print("now we are reading: " + str(list_of_input[file_index]))
    df = pd.read_csv(list_of_input[file_index], header=None)
    print('total num of rows in csv file:')
    print(df.shape[0])
    print('total elements in a row:')
    print(df.shape[1])

    if df.shape[1] == 17:
        RESHAPE = 4
        print('block size: 4x4')
    elif df.shape[1] == 65:
        RESHAPE = 8
        print('block size: 8x8')
    elif df.shape[1] == 257:
        RESHAPE = 16
        print('block size: 16x16')
    elif df.shape[1] == 1025:
        RESHAPE = 32
        print('block size: 32x32')
    elif df.shape[1] == 4097:
        RESHAPE = 64
        print('block size: 64x64')
    assert (df.shape[1] == RESHAPE * RESHAPE + 1)

    number_of_rows = len(df.index)
    print('number_of_rows : ' + str(number_of_rows))

    for x in range(number_of_rows):
        if x % 50 == 0:
            sys.stdout.write(
                '\r>> processing line: %d/%d' % (x, number_of_rows))
        if df[RESHAPE*RESHAPE][x] == 2:
            df[RESHAPE*RESHAPE][x] = 0
        elif df[RESHAPE*RESHAPE][x] == 3:
            df[RESHAPE*RESHAPE][x] = 1
        elif df[RESHAPE*RESHAPE][x] == 4:
            df[RESHAPE*RESHAPE][x] = 2
        elif df[RESHAPE*RESHAPE][x] == 5:
            df[RESHAPE*RESHAPE][x] = 3
        elif df[RESHAPE*RESHAPE][x] == 6:
            df[RESHAPE*RESHAPE][x] = 4
        elif df[RESHAPE*RESHAPE][x] == 7:
            df[RESHAPE*RESHAPE][x] = 5
        elif df[RESHAPE*RESHAPE][x] == 8:
            df[RESHAPE*RESHAPE][x] = 6
        elif df[RESHAPE*RESHAPE][x] == 9:
            df[RESHAPE*RESHAPE][x] = 7
        elif df[RESHAPE*RESHAPE][x] == 10:
            df[RESHAPE*RESHAPE][x] = 8
        elif df[RESHAPE*RESHAPE][x] == 11:
            df[RESHAPE*RESHAPE][x] = 9
        elif df[RESHAPE*RESHAPE][x] == 12:
            df[RESHAPE*RESHAPE][x] = 10
        elif df[RESHAPE*RESHAPE][x] == 13:
            df[RESHAPE*RESHAPE][x] = 11
        elif df[RESHAPE*RESHAPE][x] == 14:
            df[RESHAPE*RESHAPE][x] = 12
        elif df[RESHAPE*RESHAPE][x] == 15:
            df[RESHAPE*RESHAPE][x] = 13
        elif df[RESHAPE*RESHAPE][x] == 16:
            df[RESHAPE*RESHAPE][x] = 14
        elif df[RESHAPE*RESHAPE][x] == 17:
            df[RESHAPE*RESHAPE][x] = 15
        elif df[RESHAPE*RESHAPE][x] == 18:
            df[RESHAPE*RESHAPE][x] = 16
        elif df[RESHAPE*RESHAPE][x] == 19:
            df[RESHAPE*RESHAPE][x] = 17
        elif df[RESHAPE*RESHAPE][x] == 20:
            df[RESHAPE*RESHAPE][x] = 18
        elif df[RESHAPE*RESHAPE][x] == 21:
            df[RESHAPE*RESHAPE][x] = 19
        elif df[RESHAPE*RESHAPE][x] == 22:
            df[RESHAPE*RESHAPE][x] = 20
        elif df[RESHAPE*RESHAPE][x] == 23:
            df[RESHAPE*RESHAPE][x] = 21
        elif df[RESHAPE*RESHAPE][x] == 24:
            df[RESHAPE*RESHAPE][x] = 22
        elif df[RESHAPE*RESHAPE][x] == 25:
            df[RESHAPE*RESHAPE][x] = 23
        elif df[RESHAPE*RESHAPE][x] == 26:
            df[RESHAPE*RESHAPE][x] = 24
        elif df[RESHAPE*RESHAPE][x] == 27:
            df[RESHAPE*RESHAPE][x] = 25
        elif df[RESHAPE*RESHAPE][x] == 28:
            df[RESHAPE*RESHAPE][x] = 26
        elif df[RESHAPE*RESHAPE][x] == 29:
            df[RESHAPE*RESHAPE][x] = 27

        elif df[RESHAPE*RESHAPE][x] == 30:
            df[RESHAPE*RESHAPE][x] = 28

        elif df[RESHAPE*RESHAPE][x] == 31:
            df[RESHAPE*RESHAPE][x] = 29

        elif df[RESHAPE*RESHAPE][x] == 32:
            df[RESHAPE*RESHAPE][x] = 30

        elif df[RESHAPE*RESHAPE][x] == 33:
            df[RESHAPE*RESHAPE][x] = 31
    print('=======================')
    print('now we are writing: ' + str(
        list_of_output[file_index]) + ' . Please wait a few seconds...')
    df.to_csv(list_of_output[file_index], header=None, index=False)
    print('=================================================')
    end_timestamp = datetime.datetime.now()

    time_duration = end_timestamp - start_timestamp

    print('++++++++++++++++++++')
    print('end at: ')
    print(end_timestamp)
    print('++++++++++++++++++++')
    print('The time spent is:')
    print(time_duration)
    print('++++++++++++++++++++')
