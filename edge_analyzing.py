# ==============================================================================
# Author: Pharrell_WANG
# Date: 2017/6/28
# ==============================================================================
r"""analyze the edge strength

Usage:
```shell

$
python edge_analyzing.py --sequence='undo_dancer_1920x1088' --file='/data/undo_dancer_1920x1088/cr_mixed_data_3.csv' &> '/Users/pharrell_wang/PycharmProjects/data-processing-for-fdc/sample_data/undo_dancer_1920x1088/08x08_edge_analysis_result.txt'

python edge_analyzing.py --sequence='undo_dancer_1920x1088' --file='/data/undo_dancer_1920x1088/cr_mixed_data_2.csv' &> '/Users/pharrell_wang/PycharmProjects/data-processing-for-fdc/sample_data/undo_dancer_1920x1088/16x16_edge_analysis_result.txt'

python edge_analyzing.py --sequence='undo_dancer_1920x1088' --file='/data/undo_dancer_1920x1088/cr_mixed_data_1.csv' &> '/Users/pharrell_wang/PycharmProjects/data-processing-for-fdc/sample_data/undo_dancer_1920x1088/32x32_edge_analysis_result.txt'
ghost_fly
quick-memo: in the name 'cr_mixed_data_3.csv',
        `cr` means `comma-at-the-csv-line-end-has-been-removed`

Note:
    skip ``cr_mixed_data__0.csv``, since 64x64 is not considered for
    DMM fast search algorithm.

    That is to say, for every sequence, you should be able
    to run 3 csv files:
     {size_1(32x32), size_2(16x16), size_3(08x08)}.csv
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

tf.app.flags.DEFINE_string(
    'sequence',
    'balloons',  # default
    'Sequence names, one element from [balloons, ghost_fly, kendo, newspaper, poznan_hall_1920x1088, poznan_street_1920x1088, shark_1920x1088, undo_dancer_1920x1088 ]')

homedir = os.environ['HOME']


def main(_):
    input_file = homedir + FLAGS.file
    sequence_name = FLAGS.sequence
    x_ordered_dict, strength_dict = edge_analyzer(INPUT_FILE=input_file, SEQUENCE=sequence_name)


if __name__ == '__main__':
    tf.app.run()
