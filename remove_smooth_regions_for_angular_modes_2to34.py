# # ==============================================================================
# # Author: Pharrell_WANG
# # Date: 2017/6/28
# # ==============================================================================
#
# import os
# import numpy as np
#
# homedir = os.environ['HOME']
#
# NAME_OF_FILE_TO_SEPARATE = homedir + '/data/step2_output/size_08_files.csv'
# TRAINING_FILE = homedir + '/data/angular_without_smooth_blocks/train_data_08x08.csv'
# TESTING_FILE = homedir + '/data/angular_without_smooth_blocks/test_data_08x08.csv'
# VALIDATING_FILE = homedir + '/data/angular_without_smooth_blocks/validation_data_08x08.csv'
#
# VALIDATION_FILES = {}
# for item in range(2, 35):
#     VALIDATION_FILES['validation_%02d' % item] = \
#         homedir + '/data/angular_without_smooth_blocks/validation_data_08x08_%02d.csv' % item
#
#
# # use ``VALIDATION_FILES['validation_02'] to get the file path for the first element``
# # ``VALIDATION_FILES['validation_03']`` until  ``VALIDATION_FILES['validation_34']``
#
# def data_separator(name_of_file_to_separate, training_file, testing_file,
#                    validating_file, valivation_files):
#     with open(name_of_file_to_separate, 'r') as orig_data, \
#             open(training_file, 'w') as training_data, \
#             open(testing_file, 'w') as testing_data, \
#             open(validating_file, 'w') as validating_data:
#
