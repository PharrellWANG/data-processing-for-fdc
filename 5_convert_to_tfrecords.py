import pandas
import tensorflow as tf

import os

homedir = os.environ['HOME']

# parameters to adjust pharrell >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# --- if you want to see the extra output from console, toggle it to true
VERBOSE = False

RESHAPE = 16
# parameters to adjust pharrell >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

TRAINING = homedir + '/data/step3_output/%sx%s/data_for_training/train_%sx%s.csv' % (
    RESHAPE, RESHAPE, RESHAPE, RESHAPE)
TESTING = homedir + '/data/step3_output/%sx%s/data_for_testing/test_%sx%s.csv' % (
    RESHAPE, RESHAPE, RESHAPE, RESHAPE)
VALIDATING = homedir + '/data/step3_output/%sx%s/data_for_validating/validate_%sx%s.csv' % (
    RESHAPE, RESHAPE, RESHAPE, RESHAPE)

FILE_TO_BE_CONVERTED_STR_ARRAY = ['training', 'testing', 'validating']
for x in FILE_TO_BE_CONVERTED_STR_ARRAY:
    FILE_TO_BE_CONVERTED = ''
    if x == 'training':
        FILE_TO_BE_CONVERTED = TRAINING
    elif x == 'testing':
        FILE_TO_BE_CONVERTED = TESTING
    elif x == 'validating':
        FILE_TO_BE_CONVERTED = VALIDATING

    TFRecord_OUTPUT = homedir + '/data/TFRecords/%sx%s_%s.tfrecord' % (
        RESHAPE, RESHAPE, x)

    csv = pandas.read_csv(FILE_TO_BE_CONVERTED).values
    with tf.python_io.TFRecordWriter(TFRecord_OUTPUT) as writer:
        counter = 0
        for row in csv:
            counter += 1
            features, label = row[:-1], row[-1]
            features = features.reshape(RESHAPE, RESHAPE)
            if counter == 1 and VERBOSE:
                print('=======================')
                # io.imshow(features)
                print(type(features))
                print(features.tostring())
                print(type(features.tostring()))

            example = tf.train.Example()
            example.features.feature["image/string"].bytes_list.value.append(
                features.tostring())
            example.features.feature["image/class/label"].int64_list.value.append(
                label)
            example.features.feature["image/height"].int64_list.value.append(
                RESHAPE)
            example.features.feature["image/width"].int64_list.value.append(RESHAPE)
            if counter == 1 and VERBOSE:
                print(example)
                print(type(example))
                print('------')
                print(
                    type(example.features.feature["image/pixels"].float_list.value))
                print('------')
            writer.write(example.SerializeToString())
