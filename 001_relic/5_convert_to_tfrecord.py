import numpy as np
import pandas
import tensorflow as tf
import sys
from utils import dataset_utils

import os

# The names of the classes.
_CLASS_NAMES = [
    'homo',
    'edge'
]

homedir = os.environ['HOME']

# parameters to adjust pharrell >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# --- if you want to see the extra output from console, toggle it to true
VERBOSE = False

RESHAPE = 32
depth = 3
image_size = RESHAPE
# parameters to adjust pharrell >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

TRAINING = homedir + '/data/two_classes/32x32_homo_edge/train.csv'
TESTING = homedir + '/data/two_classes/32x32_homo_edge/test.csv'
VALIDATING = homedir + '/data/two_classes/32x32_homo_edge/validation.csv'

FILE_TO_BE_CONVERTED_STR_ARRAY = ['training', 'testing', 'validating']
for x in FILE_TO_BE_CONVERTED_STR_ARRAY:
    FILE_TO_BE_CONVERTED = ''
    if x == 'training':
        FILE_TO_BE_CONVERTED = TRAINING
    elif x == 'testing':
        FILE_TO_BE_CONVERTED = TESTING
    elif x == 'validating':
        FILE_TO_BE_CONVERTED = VALIDATING

    dataset_dir = homedir + '/data/two_classes/tfrecords/'

    TFRecord_OUTPUT = homedir + '/data/two_classes/tfrecords/%sx%s_%s.tfrecord' % (
        RESHAPE, RESHAPE, x)

    DATA_PATH = FILE_TO_BE_CONVERTED
    # please do pass header=None here, otherwise the first row is deemed as header.
    csv = pandas.read_csv(FILE_TO_BE_CONVERTED, header=None).values
    num_images = csv.shape[0]
    arrs_images = []
    arrs_labels = []
    for row in csv:
        features, label = row[:-1], row[-1]
        reshaped_features = features.reshape(RESHAPE, RESHAPE)

        reshaped_features = np.repeat(reshaped_features[:, :, np.newaxis], 3,
                                      axis=2)

        reshaped_features = reshaped_features.astype(np.uint8)
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
                        '\r>> Converting depth block of size %s %d/%d' % (x,
                                                                          j + 1,
                                                                          num_images))
                    sys.stdout.flush()

                    png_string = sess.run(encoded_png,
                                          feed_dict={image: images[j]})

                    example = dataset_utils.image_to_tfexample(
                        png_string, b'png', RESHAPE, RESHAPE,
                        labels[j])
                    tfrecord_writer.write(example.SerializeToString())
    # write label file
    labels_to_class_names = dict(zip(range(len(_CLASS_NAMES)), _CLASS_NAMES))
    dataset_utils.write_label_file(labels_to_class_names, dataset_dir)
    print('\nFinished converting homo and edge blocks!')
