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
```
"""
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
# The future statement is intended to ease migration to future versions of
# Python that introduce incompatible changes to the language. It allows use
# of the new features on a per-module basis before the release in which the
# feature becomes standard.
import tensorflow as tf

import os
import pandas
import matplotlib.pyplot as plt

homedir = os.environ['HOME']
CSV_FILES_FOR_VISUAL = [homedir + '/data/step2_output/size_08_files.csv',
                        homedir + '/data/step2_output/size_16_files.csv',
                        homedir + '/data/step2_output/size_32_files.csv',
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
    print('-----------------------------------------------------')
    print('')
    print('                 END of Hints')
    print('=====================================================')
    print('')
    print(FLAGS.block_size)
    print(type(FLAGS.block_size))

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

    csv = pandas.read_csv(FILE, nrows=10000).values
    print(FILE)
    counter = 0
    fig = plt.figure(figsize=(20, 26), dpi=70)
    plt.gcf().canvas.set_window_title(
        "Visualization for Intra Mode: " + FLAGS.mode +
        ' Block Size: ' + FLAGS.block_size)
    fig.set_facecolor('#B2B2B2')
    for row in csv:
        # print(row)
        # print(type(row))
        # print(row.size)
        # print(row.shape)
        # print('//////////////')
        selected_mode = int(FLAGS.mode)
        features, label = row[:-1], row[-1]
        if selected_mode == label:
            counter += 1
            if counter <= 48:
                features = features.reshape(RESHAPE, RESHAPE)
                if USE_SUBPLOTS:
                    fig, (ax0, ax1) = plt.subplots(1, 2)
                    ax0.imshow(features, cmap='gray')
                    # ax1.imshow(features_divided, cmap='gray')
                    plt.show()
                else:

                    # name = 'ax' + str(counter)
                    # assert (type('string') == type(name))
                    ax = fig.add_subplot(6, 8, counter)
                    # ax2 = fig.add_subplot(6, 8, 2)
                    # ax3 = fig.add_subplot(6, 8, 3)
                    # ax4 = fig.add_subplot(6, 8, 4)
                    # ax5 = fig.add_subplot(6, 8, 5)
                    # ax6 = fig.add_subplot(6, 8, 6)
                    # ax7 = fig.add_subplot(6, 8, 7)
                    # ax8 = fig.add_subplot(6, 8, 8)
                    # ax9 = fig.add_subplot(6, 8, 9)
                    # ax10 = fig.add_subplot(6, 8, 10)
                    # ax6 = fig.add_subplot(6810)

                    # title1 = ''
                    # title2 = ''
                    # title3 = ''
                    # title4 = ''
                    # title5 = ''
                    # title6 = ''

                    # set_title(ax1, title1, default="Intra mode: " + str(label))
                    # set_title(ax2, title2, default="Intra mode: " + str(label))
                    # set_title(ax3, title3, default="Intra mode: " + str(label))
                    # set_title(ax4, title4, default="Intra mode: " + str(label))
                    # set_title(ax5, title5, default="Intra mode: " + str(label))
                    # set_title(ax6, title6, default="Intra mode: " + str(label))

                    ax.set_axis_off()
                    # ax2.set_axis_off()
                    # ax3.set_axis_off()
                    # ax4.set_axis_off()
                    # ax5.set_axis_off()
                    # ax6.set_axis_off()
                    # ax7.set_axis_off()
                    # ax8.set_axis_off()
                    # ax9.set_axis_off()
                    # ax10.set_axis_off()

                    ax.imshow(features, cmap='gray', vmin=0, vmax=255)
                    # ax2.imshow(features_divided, cmap='gray', vmin=0, vmax=255)
                    # ax3.imshow(features, cmap='gray', interpolation='none',
                    #            vmin=0, vmax=255)
                    # ref 1: http://scipy-cookbook.readthedocs.io/items/Matplotlib_Show_colormaps.html
                    # ref 2: https://stackoverflow.com/questions/30301986/matplotlib-imshow-and-pixel-intensity

            else:
                break
    plt.axis('off')
    plt.show()

    # if counter == 35:
    #     features, label = row[:-1], row[-1]
    #     # print('>-----------=====>>>>>>>')
    #     #
    #     # print(np.asarray(features).ndim)
    #     # print('>----------->')
    #     # print(features)
    #     # print(features.shape)
    #     # print(features.size)
    #     # print(features.reshape(8, 8))
    #     # print(features.reshape(8, 8).shape)
    #     # print(type(features))
    #     print('----')
    #     print(label)
    #     print(label==0)
    #     print(type(label))
    #     # print('')
    #     features = features.reshape(RESHAPE, RESHAPE)
    #     print(features)
    #
    #     # features_divided = features // 2
    #     # print(features_divided)


if __name__ == '__main__':
    tf.app.run()
