import pandas

# import tensorflow as tf

FILE_TO_BE_CONVERTED = "./exam.csv"

csv = pandas.read_csv(FILE_TO_BE_CONVERTED).values
counter = 0
for row in csv:
    print('=====')
    print(row)
    print(row.shape)
    print(row.size)
    print(row.reshape(2, 2))
    print(row.reshape(2, 2).shape)
    print(type(row))
    counter += 1
    features, label = row[:-1], row[-1]
