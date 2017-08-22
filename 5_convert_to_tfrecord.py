import numpy as np
import pandas
import tensorflow as tf
import sys
from utils import dataset_utils

import os

# The names of the classes.
_CLASS_NAMES = [
    'planar',
    'DC',
    'ANGULAR 2',
    'ANGULAR 3',
    'ANGULAR 4',
    'ANGULAR 5',
    'ANGULAR 6',
    'ANGULAR 7',
    'ANGULAR 8',
    'ANGULAR 9',
    'ANGULAR 10',
    'ANGULAR 11',
    'ANGULAR 12',
    'ANGULAR 13',
    'ANGULAR 14',
    'ANGULAR 15',
    'ANGULAR 16',
    'ANGULAR 17',
    'ANGULAR 18',
    'ANGULAR 19',
    'ANGULAR 20',
    'ANGULAR 21',
    'ANGULAR 22',
    'ANGULAR 23',
    'ANGULAR 24',
    'ANGULAR 25',
    'ANGULAR 26',
    'ANGULAR 27',
    'ANGULAR 28',
    'ANGULAR 29',
    'ANGULAR 30',
    'ANGULAR 31',
    'ANGULAR 32',
    'ANGULAR 33',
    'ANGULAR 34',
    'DMM 1',
    'DMM 4',
]

homedir = os.environ['HOME']

# parameters to adjust pharrell >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# --- if you want to see the extra output from console, toggle it to true
VERBOSE = False

RESHAPE = 16
depth = 1
image_size = RESHAPE
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

    dataset_dir = homedir + '/data/TFRecords/'

    TFRecord_OUTPUT = homedir + '/data/TFRecords/%sx%s_%s.tfrecord' % (
        RESHAPE, RESHAPE, x)

    DATA_PATH = FILE_TO_BE_CONVERTED
    # please do pass header=None here, otherwise the first row is deemed as header.
    csv = pandas.read_csv(FILE_TO_BE_CONVERTED, header=None).values
    num_images = csv.shape[0]
    arrs_images = []
    arrs_labels = []
    for row in csv:
        features, label = row[:-1], row[-1]
        reshaped_features = features.reshape(RESHAPE, RESHAPE, depth)
        arrs_images.append(reshaped_features)
        arrs_labels.append(label)
    res_images = np.concatenate([arr[np.newaxis] for arr in arrs_images])
    images = res_images
    res_labels = np.concatenate([arr[np.newaxis] for arr in arrs_labels])
    labels = res_labels

    shape = (RESHAPE, RESHAPE, depth)
    with tf.python_io.TFRecordWriter(TFRecord_OUTPUT) as tfrecord_writer:
        with tf.Graph().as_default():
            image = tf.placeholder(dtype=tf.uint8, shape=shape)
            encoded_png = tf.image.encode_png(image)

            with tf.Session('') as sess:
                for j in range(num_images):
                    sys.stdout.write(
                        '\r>> Converting block data (depth block/image) %d/%d' % (
                            j + 1, num_images))
                    sys.stdout.flush()

                    png_string = sess.run(encoded_png,
                                          feed_dict={image: images[j]})

                    example = dataset_utils.image_to_tfexample(
                        png_string, 'png'.encode(), RESHAPE, RESHAPE,
                        labels[j])
                    tfrecord_writer.write(example.SerializeToString())
    # write label file
    labels_to_class_names = dict(zip(range(len(_CLASS_NAMES)), _CLASS_NAMES))
    dataset_utils.write_label_file(labels_to_class_names, dataset_dir)
    print('\nFinished converting the fast depth coding dataset!')
