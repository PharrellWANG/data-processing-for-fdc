import pandas as pd

df1 = pd.DataFrame({'0': [2, 3, 4, 7],
                    '1': [3, 4, 5, 6],
                    '2': [6, 7, 8, 9],
                    '3': [9, 10, 11, 12]},
                   index=[0, 1, 2, 3])

df2 = pd.DataFrame({'4': [0, 1, 2, 3],
                    '5': [3, 4, 5, 6],
                    '6': [6, 7, 8, 9],
                    '7': [9, 10, 11, 12]},
                   index=[0, 1, 2, 3])

df3 = pd.DataFrame({'8': [0, 1, 2, 3],
                    '9': [3, 4, 5, 6],
                    '10': [6, 7, 8, 9],
                    '11': [9, 10, 11, 12]},
                   index=[0, 1, 2, 3])

df4 = pd.DataFrame({'12': [0, 1, 2, 3],
                    '13': [3, 4, 5, 6],
                    '14': [6, 7, 8, 9],
                    '15': [9, 10, 11, 12]},
                   index=[0, 1, 2, 3])


df5 = pd.DataFrame({'16': [0, 1, 2, 3],
                    '17': [3, 4, 5, 6],
                    '18': [6, 7, 8, 9],
                    '19': [9, 10, 11, 12]},
                   index=[0, 1, 2, 3])

df6 = pd.DataFrame({'20': [0, 1, 2, 3],
                    '21': [3, 4, 5, 6],
                    '22': [6, 7, 8, 9],
                    '23': [9, 10, 11, 12]},
                   index=[0, 1, 2, 3])

df7 = pd.DataFrame({'24': [0, 1, 2, 3],
                    '25': [3, 4, 5, 6],
                    '26': [6, 7, 8, 9],
                    '27': [9, 10, 11, 12]},
                   index=[0, 1, 2, 3])

result = pd.concat([df1, df2, df3, df4, df5, df6, df7], axis=1)
res = pd.DataFrame(result)
file='/Users/pharrell_wang/PycharmProjects/data-processing-for-fdc/sample_data/saved.csv'
res.to_csv(file, index=True, index_label='range', encoding='utf-8')
