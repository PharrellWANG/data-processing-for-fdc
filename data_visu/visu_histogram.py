# ==============================================================================
# Author: Pharrell_WANG
# Date: 2017/9/12
# ==============================================================================
r"""visualizes the edge strength.

For one time, you can visu one mode one size for one sequence.

E.g., You can visu size 8x8, mode 2 for video sequence Balloons.

Usage:
```shell

$
python data_visu/visu_histogram.py --seq='newspaper' --size='8x8' --file='newspaper/csv/size_8_hist_data_for_mode_09.csv' --mode='09'

```
"""
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
import tensorflow as tf
import os
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as patches
import matplotlib.path as path
import pandas as pd

homedir = os.environ['HOME']

FLAGS = tf.app.flags.FLAGS

tf.app.flags.DEFINE_string(
    'file',
    'newspaper/csv/size_8_hist_data_for_mode_09.csv',
    'The file name of the csv to read, related to homedir, '
    'like `/data/step2_output/size_32_files.csv`')

tf.app.flags.DEFINE_string(
    'size',
    '8x8',
    '[only for display in fig] block size')

tf.app.flags.DEFINE_string(
    'seq',
    'newspaper',
    'sequence name, used as directory name')

tf.app.flags.DEFINE_string(
    'mode',
    '09',
    '[only for display in fig] mode number, [0,36]')


def main(_):
    fig, ax = plt.subplots()
    csv = pd.read_csv(
        homedir + '/PycharmProjects/data-processing-for-fdc/sample_data/' + str(
            FLAGS.file))
    # print(type(csv))
    np_array_from_csv_file = csv.as_matrix()
    np_array_from_csv_file = np_array_from_csv_file.flatten()
    # print(type(np_array_from_csv_file))
    # print(np_array_from_csv_file)
    # print(np_array_from_csv_file.shape)
    # print(np_array_from_csv_file.ndim)
    # n, bins = np.histogram(data, 100)
    n, bins = np.histogram(np_array_from_csv_file, 20)

    # get the corners of the rectangles for the histogram
    left = np.array(bins[:-1])
    right = np.array(bins[1:])
    bottom = np.zeros(len(left))
    top = bottom + n

    # we need a (numrects x numsides x 2) numpy array for the path helper
    # function to build a compound path
    XY = np.array([[left, left, right, right], [bottom, top, top, bottom]]).T

    # get the Path object
    barpath = path.Path.make_compound_path_from_polys(XY)

    # make a patch out of it
    patch = patches.PathPatch(barpath)
    ax.add_patch(patch)

    # update the view limits
    ax.set_xlim(left[0], right[-1])
    ax.set_ylim(bottom.min(), top.max())
    fig.suptitle(
        "Distribution of Edge Strength\n Sequence: %s , Block size: %s , Mode: %s" % (
            FLAGS.seq, FLAGS.size, FLAGS.mode), fontsize=10)

    plt.xlabel('Edge Strength', fontsize=10)
    plt.ylabel('No. of Samples', fontsize=10)
    fig.savefig(homedir + '/PycharmProjects/data-processing-for-fdc/sample_data/%s/pdf/size%s.pdf' % (FLAGS.seq, str(FLAGS.size) + '_mode' + str(FLAGS.mode)))

    plt.show()


if __name__ == '__main__':
    tf.app.run()
