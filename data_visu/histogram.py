import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as patches
import matplotlib.path as path
import pandas as pd

fig, ax = plt.subplots()

csv = pd.read_csv('/Users/pharrell_wang/PycharmProjects/data-processing-for-fdc/sample_data/save_histogram_data.csv')
# print(type(csv))
npcsv = csv.as_matrix()
npcsv = npcsv.flatten()
# print(type(npcsv))
# print(npcsv)
# print(npcsv.shape)
# print(npcsv.ndim)
# n, bins = np.histogram(data, 100)
n, bins = np.histogram(npcsv, 4)

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
# ax.set_xlim(-100, 5)
ax.set_ylim(bottom.min(), top.max())

plt.show()
