import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

fig, ax = plt.subplots()

# histogram our data with numpy
# data = np.random.randn(1000)
data = np.array([])
for x in range(1000):
    ran = np.random.randn(1)
    data = np.append(data, ran[0])
# print(type(data))
# print(data.shape)
# print(data.ndim)
df = pd.DataFrame(data)
df.to_csv('/Users/pharrell_wang/PycharmProjects/data-processing-for-fdc/sample_data/save_histogram_data.csv', index=False)