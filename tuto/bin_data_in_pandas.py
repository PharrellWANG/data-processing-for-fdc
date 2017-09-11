import pandas as pd

csv = pd.read_csv(
    '/Users/pharrell_wang/PycharmProjects/data-processing-for-fdc/sample_data/save_histogram_data.csv')
print(type(csv))
npcsv = csv.as_matrix()
npcsv = npcsv.flatten()

raw_data = {
    # 'regiment': ['Nighthawks', 'Nighthawks', 'Nighthawks', 'Nighthawks',
    #                      'Dragoons', 'Dragoons', 'Dragoons', 'Dragoons',
    #                      'Scouts', 'Scouts', 'Scouts', 'Scouts'],
    #         'company': ['1st', '1st', '2nd', '2nd', '1st', '1st', '2nd', '2nd',
    #                     '1st', '1st', '2nd', '2nd'],
    #         'name': ['Miller', 'Jacobson', 'Ali', 'Milner', 'Cooze', 'Jacon',
    #                  'Ryaner', 'Sone', 'Sloan', 'Piger', 'Riani', 'Ali'],
    #         'preTestScore': [4, 24, 31, 2, 3, 4, 24, 31, 2, 3, 2, 3],
    # 'postTestScore': [25, 94, 57, 62, 70, 25, 94, 57, 62, 70, 62, 70]}
    'postTestScore': npcsv}

df = pd.DataFrame(raw_data,
                  columns=[
                      # 'regiment', 'company', 'name', 'preTestScore',
                      'postTestScore'])
# print('now the dataframe is:')
# print(df)

# bins = [0, 50, 100, 150, 200]
bins = 4

# group_names = ['Low', 'Okay', 'Good', 'Great']
group_names = [1, 2, 3, 4]

categories = pd.cut(df['postTestScore'], bins, labels=group_names)
# print(categories)
df['mode_00'] = pd.cut(df['postTestScore'], bins, labels=group_names)
df['scoresBinned'] = pd.cut(df['postTestScore'], bins)

# print('now the categories is:')
# print(categories)
# print(df)

value_count = pd.value_counts(df['mode_00'], sort=False)

# print('now the value_count is:')
# print(value_count)
# print(type(value_count))
# print(value_count[1])
# print('now value count frame is: ')
value_count_frame = value_count.to_frame()
# print(type(value_count_frame))
# print('====')
# print(value_count_frame['mode_00'])
# print('====----')
value_count.to_csv(
    path='/Users/pharrell_wang/PycharmProjects/data-processing-for-fdc/sample_data/saved.csv',
    header=True,
    index=False)

# print(value_count_frame)
# print('now the dataframe is:')
# print(df)
