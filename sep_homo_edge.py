# ==============================================================================
# Author: Pharrell_WANG
# Date: 2017/6/28
# ==============================================================================
# from csv_mode_counter import csv_mode_preprocessing
import os

homedir = os.environ['HOME']
ORIGINAL = homedir + '/data/two_classes/08_homo_edge.csv'
TRAIN = homedir + '/data/two_classes/08x08_train.csv'
TEST = homedir + '/data/two_classes/08x08_test.csv'
VALIDATE = homedir + '/data/two_classes/08x08_validation.csv'


def data_generator(ORIG, TRAINING, VALIDATING, TESTING):
    with open(ORIG, 'r') as orig_data, open(TRAINING, 'w') as training_data, \
            open(TESTING, 'w') as testing_data, \
            open(VALIDATING, 'w') as validating_data:

        mode_0 = 0  # homo
        mode_1 = 0  # edge

        for line in orig_data:
            mode = int(line[-2:-1])

            if mode == 0:
                mode_0 += 1
                if mode_0 <= 1462127:
                    training_data.write(line)
                elif 1462127 < mode_0 <= 1464127:
                    validating_data.write(line)
                elif 1464127 < mode_0 <= 1466127:
                    testing_data.write(line)
            elif mode == 1:
                mode_1 += 1
                if mode_1 <= 1462127:
                    training_data.write(line)
                elif 1462127 < mode_1 <= 1464127:
                    validating_data.write(line)
                elif 1464127 < mode_1 <= 1466127:
                    testing_data.write(line)


data_generator(ORIG=ORIGINAL, TRAINING=TRAIN, VALIDATING=VALIDATE,
               TESTING=TEST
               )
