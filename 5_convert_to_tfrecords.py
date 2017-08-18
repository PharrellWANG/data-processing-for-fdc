import pandas
import tensorflow as tf

import os

homedir = os.environ['HOME']
TRAINING = homedir + '/data/step3_output/32x32/data_for_training/train_32x32.csv'
TESTING = homedir + '/data/step3_output/32x32/data_for_testing/test_32x32.csv'
VALIDATING = homedir + '/data/step3_output/32x32/data_for_validating/validate_32x32.csv'

# FILE_TO_BE_CONVERTED = TRAINING
# FILE_TO_BE_CONVERTED = TESTING
FILE_TO_BE_CONVERTED = VALIDATING

TFRecord_OUTPUT = homedir + '/data/TFRecords/32x32_validate.tfrecord'

csv = pandas.read_csv(FILE_TO_BE_CONVERTED).values
with tf.python_io.TFRecordWriter(TFRecord_OUTPUT) as writer:
    counter = 0
    for row in csv:
        counter += 1
        features, label = row[:-1], row[-1]
        example = tf.train.Example()
        example.features.feature["image/pixels"].float_list.value.extend(features)
        example.features.feature["image/class/label"].int64_list.value.append(label)
        example.features.feature["image/height"].int64_list.value.append(32)
        example.features.feature["image/width"].int64_list.value.append(32)
        if counter == 1:
            print(example)
            print(type(example))
        writer.write(example.SerializeToString())
