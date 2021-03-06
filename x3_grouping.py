"""
for grouping [9, 10, 11] and [25, 26, 27]

Final classes: 28 classes.
"""
# import csv
import pandas as pd
import os
import sys
import datetime

homedir = os.environ['HOME']
input_files = [
	homedir + '/data/smooth_removed/32_classes__ave_90_size_08_files.csv'
]

output_files = [
	homedir + '/data/smooth_removed/32_classes__ave_90_size_08_files__after_grouping.csv'
]

for file_index in range(len(input_files)):
	start_timestamp = datetime.datetime.now()
	print('=================================================')
	print('start at: ')
	print(start_timestamp)
	print("now we are reading: " + str(input_files[file_index]))
	df = pd.read_csv(input_files[file_index], header=None)
	
	number_of_rows = len(df.index)
	print('number_of_rows : ' + str(number_of_rows))
	
	for x in range(number_of_rows):
		if x % 50 == 0:
			sys.stdout.write('\r>> processing line: %d/%d' % (x, number_of_rows))
		if df[64][x] == 2:
			df[64][x] = 0
		elif df[64][x] == 3:
			df[64][x] = 1
		elif df[64][x] == 4:
			df[64][x] = 2
		elif df[64][x] == 5:
			df[64][x] = 3
		elif df[64][x] == 6:
			df[64][x] = 4
		elif df[64][x] == 7:
			df[64][x] = 5
		elif df[64][x] == 8:
			df[64][x] = 6
		elif df[64][x] == 9 or df[64][x] == 10 or df[64][x] == 11:
			df[64][x] = 7
		elif df[64][x] == 12:
			df[64][x] = 8
		elif df[64][x] == 13:
			df[64][x] = 9
		elif df[64][x] == 14:
			df[64][x] = 10
		elif df[64][x] == 15:
			df[64][x] = 11
		elif df[64][x] == 16:
			df[64][x] = 12
		elif df[64][x] == 17:
			df[64][x] = 13
		elif df[64][x] == 18:
			df[64][x] = 14
		elif df[64][x] == 19:
			df[64][x] = 15
		elif df[64][x] == 20:
			df[64][x] = 16
		elif df[64][x] == 21:
			df[64][x] = 17
		elif df[64][x] == 22:
			df[64][x] = 18
		elif df[64][x] == 23:
			df[64][x] = 19
		elif df[64][x] == 24:
			df[64][x] = 20
		elif df[64][x] == 25 or df[64][x] == 26 or df[64][x] == 27:
			df[64][x] = 21
		elif df[64][x] == 28:
			df[64][x] = 22
		elif df[64][x] == 29:
			df[64][x] = 23
		elif df[64][x] == 30:
			df[64][x] = 24
		elif df[64][x] == 31:
			df[64][x] = 25
		elif df[64][x] == 32:
			df[64][x] = 26
		elif df[64][x] == 33:
			df[64][x] = 27
	print('=======================')
	print('now we are writing: ' + str(
		output_files[file_index]) + ' . Please wait a few seconds...')
	df.to_csv(output_files[file_index], header=None, index=False)
	print('=================================================')
	end_timestamp = datetime.datetime.now()
	
	time_duration = end_timestamp - start_timestamp
	
	print('++++++++++++++++++++')
	print('end at: ')
	print(end_timestamp)
	print('++++++++++++++++++++')
	print('The time spent is:')
	print(time_duration)
	print('++++++++++++++++++++')
