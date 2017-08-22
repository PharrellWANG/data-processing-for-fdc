import pandas
import tensorflow as tf

import os

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

    TFRecord_OUTPUT = homedir + '/data/TFRecords/%sx%s_%s.tfrecord' % (
        RESHAPE, RESHAPE, x)

    # filename_queue = tf.train.string_input_producer([FILE_TO_BE_CONVERTED])
    #
    # reader = tf.TextLineReader()
    # key, value = reader.read(filename_queue)
    #
    # # Default values, in case of empty columns. Also specifies the type of the
    # # decoded result.
    #
    # record_defaults = [[1] for _ in range(RESHAPE * RESHAPE + 1)]
    #
    # # list_of_RESHAPESQUARE_plus1_columns => square_plus_one
    # square_plus_one = tf.decode_csv(value,
    #                                 record_defaults=record_defaults)
    # single_image = tf.stack(square_plus_one[0:len(square_plus_one) - 1])
    # single_label = tf.stack(square_plus_one[len(square_plus_one) - 1])
    # depth_major = tf.reshape(single_image, [depth, image_size, image_size])
    # # Convert from [depth, height, width] to [height, width, depth].
    # image = tf.cast(tf.transpose(depth_major, [1, 2, 0]), tf.float32)
    #
    # single_label = tf.cast(single_label, tf.int64)
    # label = tf.reshape(single_label, (1,))

    csv = pandas.read_csv(FILE_TO_BE_CONVERTED, nrows=2).values
    print(type(csv))
    print(csv)
    print(csv.shape)
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
            # you have to follow the key names here, otherwise you will get key error. Or you need to modify a lot of source code from tensorflow models/slim.
            example.features.feature["image/encoded"].bytes_list.value.append(
                features.tostring())
            example.features.feature[
                "image/class/label"].int64_list.value.append(
                label)
            example.features.feature["image/format"].int64_list.value.append(
                'raw')
            example.features.feature["image/height"].int64_list.value.append(
                RESHAPE)
            example.features.feature["image/width"].int64_list.value.append(
                RESHAPE)
            if counter == 1 and VERBOSE:
                print(example)
                print(type(example))
                print('------')
                print(
                    type(example.features.feature[
                             "image/pixels"].float_list.value))
                print('------')
            writer.write(example.SerializeToString())
