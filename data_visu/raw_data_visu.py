# ------------------------------------------------------------------------------
# Author: Pharrell_WANG
# Date: 2017/6/28
# ------------------------------------------------------------------------------
USE_SUBPLOTS = False

import os
import pandas
import matplotlib.pyplot as plt
# from skimage import io
import numpy as np

homedir = os.environ['HOME']

list_of_output_files = [homedir + '/data/step2_output/size_08_files.csv',
                        homedir + '/data/step2_output/size_16_files.csv',
                        homedir + '/data/step2_output/size_32_files.csv',
                        homedir + '/data/step2_output/size_64_files.csv'
                        ]


def set_title(ax, title, default=""):
    if title is not None and title != "":
        ax.set_title(title,
                     y=1.02)  # adjustment for plot title bottom margin
    else:
        ax.set_title(default,
                     y=1.02)  # adjustment for plot title bottom margin


# FILE = "../exam.csv"
FILE = list_of_output_files[0]

csv = pandas.read_csv(FILE, nrows=3).values
print(FILE)
counter = 0
for row in csv:
    counter += 1
    # print(row)
    # print(type(row))
    # print(row.size)
    # print(row.shape)
    # print('//////////////')

    if counter == 1:
        features, label = row[:-1], row[-1]
        # print('>-----------=====>>>>>>>')
        #
        # print(np.asarray(features).ndim)
        # print('>----------->')
        # print(features)
        # print(features.shape)
        # print(features.size)
        # print(features.reshape(8, 8))
        # print(features.reshape(8, 8).shape)
        # print(type(features))
        # print('----')
        # print(label)
        # print(type(label))
        # print('')
        features = features.reshape(8, 8)
        print(features)

        features_divided = features // 2
        print(features_divided)

        if USE_SUBPLOTS:
            fig, (ax0, ax1) = plt.subplots(1, 2)
            ax0.imshow(features, cmap='gray')
            ax1.imshow(features_divided, cmap='gray')
            plt.show()
        else:
            fig = plt.figure(figsize=(20, 24), dpi=70)
            plt.gcf().canvas.set_window_title(
                "video coding block data visualization")
            fig.set_facecolor('#B2B2B2')
            ax1 = fig.add_subplot(6, 8, 1)
            ax2 = fig.add_subplot(6, 8, 2)
            ax3 = fig.add_subplot(6, 8, 3)
            ax4 = fig.add_subplot(6, 8, 4)
            ax5 = fig.add_subplot(6, 8, 5)
            ax6 = fig.add_subplot(6, 8, 6)
            ax7 = fig.add_subplot(6, 8, 7)
            ax8 = fig.add_subplot(6, 8, 8)
            ax9 = fig.add_subplot(6, 8, 9)
            ax10 = fig.add_subplot(6, 8, 10)
            # ax6 = fig.add_subplot(6810)

            title1 = ''
            title2 = ''
            title3 = ''
            title4 = ''
            title5 = ''
            title6 = ''

            set_title(ax1, title1, default="Intra mode: " + str(label))
            set_title(ax2, title2, default="Intra mode: " + str(label))
            set_title(ax3, title3, default="Intra mode: " + str(label))
            set_title(ax4, title4, default="Intra mode: " + str(label))
            set_title(ax5, title5, default="Intra mode: " + str(label))
            set_title(ax6, title6, default="Intra mode: " + str(label))

            ax1.set_axis_off()
            ax2.set_axis_off()
            ax3.set_axis_off()
            ax4.set_axis_off()
            ax5.set_axis_off()
            ax6.set_axis_off()
            ax7.set_axis_off()
            ax8.set_axis_off()
            ax9.set_axis_off()
            ax10.set_axis_off()

            ax1.imshow(features, cmap='gray')
            ax2.imshow(features_divided, cmap='gray')
            plt.axis('off')
            plt.show()

    else:
        break
