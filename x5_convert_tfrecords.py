import numpy as np
import pandas
import tensorflow as tf
import sys
from utils import dataset_utils

import os

# The names of the classes.
_CLASS_NAMES = [
	'ANGULAR 2',
	'ANGULAR 3',
	'ANGULAR 4',
	'ANGULAR 5',
	'ANGULAR 6',
	'ANGULAR 7',
	'ANGULAR 8',
	'ANGULAR 9-10-11',
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
	'ANGULAR 25-26-27',
	'ANGULAR 28',
	'ANGULAR 29',
	'ANGULAR 30',
	'ANGULAR 31',
	'ANGULAR 32',
	'ANGULAR 33',
]

homedir = os.environ['HOME']

# parameters to adjust pharrell >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# --- if you want to see the extra output from console, toggle it to true
VERBOSE = False

RESHAPE = 8
depth = 3
image_size = RESHAPE
# parameters to adjust pharrell >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

TRAINING = homedir + '/data/smooth_removed/slim/data/train_%sx%s.csv' % (
	RESHAPE, RESHAPE)
TESTING = homedir + '/data/smooth_removed/slim/data/test_%sx%s.csv' % (
	RESHAPE, RESHAPE)
VALIDATING = homedir + '/data/smooth_removed/slim/data/validation_%sx%s.csv' % (
	RESHAPE, RESHAPE)

FILE_TO_BE_CONVERTED_STR_ARRAY = ['training', 'testing', 'validating']
uv_values = np.zeros(128)

for x in FILE_TO_BE_CONVERTED_STR_ARRAY:
	FILE_TO_BE_CONVERTED = ''
	if x == 'training':
		FILE_TO_BE_CONVERTED = TRAINING
	elif x == 'testing':
		FILE_TO_BE_CONVERTED = TESTING
	elif x == 'validating':
		FILE_TO_BE_CONVERTED = VALIDATING
	
	dataset_dir = homedir + '/data/smooth_removed/slim/tfrecords'
	
	TFRecord_OUTPUT = homedir + '/data/smooth_removed/slim/tfrecords/%sx%s_%s.tfrecord' % (
		RESHAPE, RESHAPE, x)
	
	DATA_PATH = FILE_TO_BE_CONVERTED
	# please do pass header=None here, otherwise the first row is deemed as header.
	csv = pandas.read_csv(FILE_TO_BE_CONVERTED, header=None).values
	num_images = csv.shape[0]
	arrs_images = []
	arrs_labels = []
	for row in csv:
		features, label = row[:-1], row[-1]
		# populate the u and v as fake 0. Because with uv value to be 0s. it is almost the same as luma only blocks. Our model requires a 3 dim value.
		features_with_uv_values = np.hstack((features, uv_values))
		reshaped_depth_major_features = features_with_uv_values.reshape(depth, RESHAPE, RESHAPE)
		# from [depth, reshape, reshape] to [reshape, reshape, depth]
		reshaped_features = np.transpose(reshaped_depth_major_features, (1, 2, 0))
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
			encoded_jpeg = tf.image.encode_jpeg(image)
			
			with tf.Session('') as sess:
				for j in range(num_images):
					sys.stdout.write(
						'\r>> Converting depth block data %d/%d' % (
							j + 1, num_images))
					sys.stdout.flush()
					
					jpg_string = sess.run(encoded_jpeg,
																feed_dict={image: images[j]})
					
					# use  b'jpg' instead of png. Since in jpg, the yuv is used.
					# (JPG is the same as JPEG)
					example = dataset_utils.image_to_tfexample(
						jpg_string, b'jpg', RESHAPE, RESHAPE,
						labels[j])
					
					tfrecord_writer.write(example.SerializeToString())
	# write label file
	labels_to_class_names = dict(zip(range(len(_CLASS_NAMES)), _CLASS_NAMES))
	dataset_utils.write_label_file(labels_to_class_names, dataset_dir)
	print('\nFinished converting the FDC %s dataset!' % x)
