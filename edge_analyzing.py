# ==============================================================================
# Author: Pharrell_WANG
# Date: 2017/6/28
# ==============================================================================
r"""analyze the edge strength

Usage:
```shell

$ python edge_analyzing.py \
    --file='/data/step2_output/size_16_files.csv'
```
"""
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
import tensorflow as tf
import os
from utils.edge_strength_analysis import edge_analyzer

FLAGS = tf.app.flags.FLAGS

tf.app.flags.DEFINE_string(
    'file',
    '/data/step2_output/size_16_files.csv',  # default
    'part of the file name, such as /data/step2_output/file.csv')

homedir = os.environ['HOME']


def main(_):
    input_file = homedir + FLAGS.file
    x_ordered_dict, strength_dict = edge_analyzer(INPUT_FILE=input_file)

if __name__ == '__main__':
    tf.app.run()
