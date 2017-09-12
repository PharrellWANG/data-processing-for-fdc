# ==============================================================================
# Author: Pharrell_WANG
# Date: 2017/6/28
# ==============================================================================
import numpy as np
import sys
import pandas as pd
import datetime
import os

homedir = os.environ['HOME']
INFILE = homedir + '/data/step2_output/size_08_files.csv'
OUTFILE = homedir + '/data/smooth_removed/ave_90_size_08_files.csv'


def remove_smooth(INPUT_FILE, OUTPUT_FILE):
    start_timestamp = datetime.datetime.now()
    print('=================================================')
    print('start at: ')
    print(start_timestamp)
    print('Name of the data file: ' + str(INPUT_FILE))

    RESHAPE = 8  # INIT
    csv = pd.read_csv(INPUT_FILE, header=None).values
    print('total num of rows in csv file:')
    print(csv.shape[0])
    print('total elements in a row:')
    print(csv.shape[1])

    if csv.shape[1] == 65:
        RESHAPE = 8
        print('block size: 8x8')
    elif csv.shape[1] == 257:
        RESHAPE = 16
        print('block size: 16x16')
    elif csv.shape[1] == 1025:
        RESHAPE = 32
        print('block size: 32x32')
    assert (csv.shape[1] == RESHAPE * RESHAPE + 1)

    with open(INPUT_FILE, 'r') as r, \
            open(OUTPUT_FILE, 'w') as w:
        cnt = 0
        new_cnt = 0
        for num, line in enumerate(r):
            data = np.array([])
            cnt += 1
            sys.stdout.write(
                '\r>> processing line: %d / %d' % (cnt, csv.shape[0]))
            # edge strength analysis
            # read one line every time
            total_strength = 0

            row = csv[cnt - 1]
            # local_counter = 0
            features, label = row[:-1], row[-1]
            features = features.reshape(RESHAPE, RESHAPE)
            for i in range(RESHAPE - 1):
                for j in range(RESHAPE - 1):
                    # local_counter += 1
                    # sys.stdout.write(
                    #     '\r>> processing %d/%d' % (local_counter,
                    #                                RESHAPE ** 2))
                    horizontal_strength = \
                        features[i][j] + \
                        features[i + 1][j] - \
                        features[i][j + 1] - \
                        features[i + 1][j + 1]
                    vertical_strength = \
                        features[i][j] + \
                        features[i][j + 1] - \
                        features[i + 1][j] - \
                        features[i + 1][j + 1]
                    strength = horizontal_strength ** 2 + vertical_strength ** 2
                    data = np.append(data, np.array([
                        strength]))  # total strength of a block (or you can say a line in the csv file)
                    # df = pd.DataFrame(data)
                    # df.to_csv(
                    #     '/Users/pharrell_wang/PycharmProjects/data-processing-for-fdc/sample_data/save_histogram_data.csv',
                    #     index=False)
                    total_strength += strength

            assert (data.ndim == 1)
            # top RESHAPE*2 && non-zero average.
            # step1: top RESHAPE*2 values in the numpy arrary
            top_k = data[np.argsort(data)][data.size - RESHAPE * 2:]
            assert (top_k.ndim == 1)
            # step2: non-zero values (because sometimes the edge length can be short. We only want the sharpness. We do not want smooth regions to affect the sharpness.)
            data = top_k[top_k.nonzero()]
            data = data[np.where(
                data > 8)]  # for [[2, 0], [0, 0]], i exclude it from the concept of sharp
            if data.size == 0:  # all the strength are zero. (that is to say , it is the DC mode)
                ave = 0
            else:
                ave = np.mean(data)

            if ave >= 90:
                new_cnt += 1
                # sys.stdout.write(
                #     '\r>> yes, write new line please: %d' % new_cnt)
                newline = line
                w.write(newline)

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


remove_smooth(INPUT_FILE=INFILE, OUTPUT_FILE=OUTFILE)
