# ==============================================================================
# Author: Pharrell_WANG
# Date: 2017/6/28
# ==============================================================================
r"""visualizes the collected datasets (blocks of size 64x64, 32x32, 16x16, 8x8)

Usage:
```shell

$ python visualize_blocks.py \
    --block_size=8

$ python visualize_blocks.py \
    --block_size=16

$ python visualize_blocks.py \
    --block_size=32

$ python visualize_blocks.py \
    --block_size=64

sample code:
python data_visu/visualize_blocks.py --block_size=32 --mode=35 --skip_rows=20 --rows_to_read=4000
python data_visu/visualize_blocks.py --skip_rows=20 --rows_to_read=4000 --block_size=8 --mode=1

```
"""
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
import tensorflow as tf
import os
import pandas
import numpy as np
import matplotlib.pyplot as plt

homedir = os.environ['HOME']
CSV_FILES_FOR_VISUAL = [
    homedir + '/data/step2_output/size_08_files.csv',
    # homedir + '/data/smooth_removed/ave_90_size_08_files.csv',
    homedir + '/data/step2_output/size_16_files.csv',
    homedir + '/data/step2_output/size_32_files.csv',
    # '/Users/Pharrell_WANG/data/two_classes/32x32_train.csv',
    homedir + '/data/step2_output/size_64_files.csv'
]

FLAGS = tf.app.flags.FLAGS

tf.app.flags.DEFINE_string(
    'block_size',
    None,
    'The size of the block to visualize, one of 8, 16, 32, 64.')

tf.app.flags.DEFINE_string(
    'mode',
    None,
    'The number of the mode to visualize, one of the integers '
    'within the range of [0, 36].')

tf.app.flags.DEFINE_string(
    'skip_rows',
    0,
    'rows to skip when reading csv file, default 0')

tf.app.flags.DEFINE_string(
    'rows_to_read',
    4000,
    'rows to read when reading csv file, default 4000')

USE_SUBPLOTS = False


def set_title(ax, title, default=""):
    if title is not None and title != "":
        ax.set_title(title,
                     y=1.02)  # adjustment for plot title bottom margin
    else:
        ax.set_title(default,
                     y=1.02)  # adjustment for plot title bottom margin


def main(_):
    print('')
    print('=====================================================')
    print('')
    print('                 Friendly Hints                      ')
    print('-----------------------------------------------------')
    print(' # 1. block_size must be one of 8, 16, 32, 64')
    print(' # 2. mode must be one of the integers within [0,36]')
    print(' # 3. skip_rows')
    print(' # 4. rows_to_read')
    print('-----------------------------------------------------')
    print('')
    print('                 END of Hints')
    print('=====================================================')
    print('')
    if not FLAGS.block_size:
        raise ValueError('You must supply the '
                         'block size (8, 16, 32, 64) with --block_size')
    if not FLAGS.mode:
        raise ValueError('You must supply the mode [0, 36] with --mode')

    if FLAGS.block_size == '8':
        INDEX = 0
        RESHAPE = 8
    elif FLAGS.block_size == '16':
        INDEX = 1
        RESHAPE = 16
    elif FLAGS.block_size == '32':
        INDEX = 2
        RESHAPE = 32
    elif FLAGS.block_size == '64':
        INDEX = 3
        RESHAPE = 64
    else:
        raise ValueError(
            'block_size [%s] was not recognized.' % FLAGS.block_size)

    FILE = CSV_FILES_FOR_VISUAL[INDEX]

    csv = pandas.read_csv(FILE, skiprows=int(FLAGS.skip_rows),
                          nrows=int(FLAGS.rows_to_read)).values
    print(FILE)
    counter = 0
    fig = plt.figure(figsize=(20, 26), dpi=70)
    plt.gcf().canvas.set_window_title(
        "Visualization for Intra Mode: " + FLAGS.mode +
        ' Block Size: ' + FLAGS.block_size)
    fig.set_facecolor('#B2B2B2')
    fig.suptitle(
        "Intra mode: " + FLAGS.mode +
        ' Block size: ' + FLAGS.block_size, fontsize=24)
    # "Visualization of 48 (6x8) collected block data \n INTRA MODE: " + FLAGS.mode +
    # '\n BLOCK SIZE: ' + FLAGS.block_size, fontsize=24)
    for row in csv:
        selected_mode = int(FLAGS.mode)
        features, label = row[:-1], row[-1]
        if selected_mode == label:
            counter += 1
            if counter <= 48:
                features = features.reshape(RESHAPE, RESHAPE)

                features = np.repeat(features[:, :, np.newaxis], 3, axis=2)

                features = features.astype(np.uint8)

                if USE_SUBPLOTS:
                    fig, (ax0, ax1) = plt.subplots(1, 2)
                    ax0.imshow(features, cmap='gray')
                    plt.show()
                else:
                    ax = fig.add_subplot(6, 8, counter)
                    # ax.imshow(features, cmap='gray', vmin=0, vmax=255)
                    ax.imshow(features)
            else:
                break
    plt.axis('off')
    plt.show()


if __name__ == '__main__':
    tf.app.run()
