# ==============================================================================
# Author: Pharrell_WANG
# Date: 2017/6/28
# ==============================================================================

import os
import datetime

homedir = os.environ['HOME']
ORIG = homedir + '/data/smooth_removed/23_classes__ave_90_size_08_files__after_grouping.csv'
TRAINING = homedir + '/data/smooth_removed/data/train_08x08.csv'
TESTING = homedir + '/data/smooth_removed/data/test_08x08.csv'
VALIDATING = homedir + '/data/smooth_removed/data/validation_08x08.csv'

VALIDATING0 = homedir + '/data/smooth_removed/data/validation_08x08_0.csv'
VALIDATING1 = homedir + '/data/smooth_removed/data/validation_08x08_1.csv'
VALIDATING2 = homedir + '/data/smooth_removed/data/validation_08x08_2.csv'
VALIDATING3 = homedir + '/data/smooth_removed/data/validation_08x08_3.csv'
VALIDATING4 = homedir + '/data/smooth_removed/data/validation_08x08_4.csv'
VALIDATING5 = homedir + '/data/smooth_removed/data/validation_08x08_5.csv'
VALIDATING6 = homedir + '/data/smooth_removed/data/validation_08x08_6.csv'
VALIDATING7 = homedir + '/data/smooth_removed/data/validation_08x08_7.csv'
VALIDATING8 = homedir + '/data/smooth_removed/data/validation_08x08_8.csv'
VALIDATING9 = homedir + '/data/smooth_removed/data/validation_08x08_9.csv'
VALIDATING10 = homedir + '/data/smooth_removed/data/validation_08x08_10.csv'
VALIDATING11 = homedir + '/data/smooth_removed/data/validation_08x08_11.csv'
VALIDATING12 = homedir + '/data/smooth_removed/data/validation_08x08_12.csv'
VALIDATING13 = homedir + '/data/smooth_removed/data/validation_08x08_13.csv'
VALIDATING14 = homedir + '/data/smooth_removed/data/validation_08x08_14.csv'
VALIDATING15 = homedir + '/data/smooth_removed/data/validation_08x08_15.csv'
VALIDATING16 = homedir + '/data/smooth_removed/data/validation_08x08_16.csv'
VALIDATING17 = homedir + '/data/smooth_removed/data/validation_08x08_17.csv'
VALIDATING18 = homedir + '/data/smooth_removed/data/validation_08x08_18.csv'
VALIDATING19 = homedir + '/data/smooth_removed/data/validation_08x08_19.csv'
VALIDATING20 = homedir + '/data/smooth_removed/data/validation_08x08_20.csv'
VALIDATING21 = homedir + '/data/smooth_removed/data/validation_08x08_21.csv'
VALIDATING22 = homedir + '/data/smooth_removed/data/validation_08x08_22.csv'


def data_generator(ORIG, TRAINING, VALIDATING, TESTING,
									 VALIDATING0,
									 VALIDATING1,
									 VALIDATING2,
									 # VALIDATING3,
									 # VALIDATING4,
									 # VALIDATING5,
									 # VALIDATING6,
									 # VALIDATING7,
									 # VALIDATING8,
									 # VALIDATING9,
									 # VALIDATING10,
									 # VALIDATING11,
									 # VALIDATING12,
									 # VALIDATING13,
									 # VALIDATING14,
									 # VALIDATING15,
									 # VALIDATING16,
									 # VALIDATING17,
									 # VALIDATING18,
									 VALIDATING19,
									 VALIDATING20,
									 VALIDATING21,
									 VALIDATING22,
									 # VALIDATING23,
									 # VALIDATING24,
									 # VALIDATING25,
									 # VALIDATING26,
									 # VALIDATING27,
									 ):
	start_timestamp = datetime.datetime.now()
	print('=================================================')
	print('start at: ')
	print(start_timestamp)
	with open(ORIG, 'r') as orig_data, open(TRAINING, 'w') as training_data, \
		open(TESTING, 'w') as testing_data, \
		open(VALIDATING, 'w') as validating_data, \
		open(VALIDATING0, 'w') as validating_data0, \
		open(VALIDATING1, 'w') as validating_data1, \
		open(VALIDATING2, 'w') as validating_data2, \
		open(VALIDATING19, 'w') as validating_data19, \
		open(VALIDATING20, 'w') as validating_data20, \
		open(VALIDATING21, 'w') as validating_data21, \
		open(VALIDATING22, 'w') as validating_data22:
		# open(VALIDATING23, 'w') as validating_data23:
		# open(VALIDATING24, 'w') as validating_data24, \
		# open(VALIDATING25, 'w') as validating_data25:
		# open(VALIDATING24, 'w') as validating_data24, \
		# open(VALIDATING25, 'w') as validating_data25, \
		# open(VALIDATING26, 'w') as validating_data26, \
		# open(VALIDATING27, 'w') as validating_data27, \
		# open(VALIDATING28, 'w') as validating_data28, \
		# open(VALIDATING29, 'w') as validating_data29, \
		# open(VALIDATING3, 'w') as validating_data3, \
		# open(VALIDATING4, 'w') as validating_data4, \
		# open(VALIDATING5, 'w') as validating_data5, \
		# open(VALIDATING6, 'w') as validating_data6, \
		# open(VALIDATING7, 'w') as validating_data7, \
		# open(VALIDATING8, 'w') as validating_data8, \
		# open(VALIDATING9, 'w') as validating_data9, \
		# open(VALIDATING10, 'w') as validating_data10, \
		# open(VALIDATING11, 'w') as validating_data11, \
		# open(VALIDATING12, 'w') as validating_data12, \
		# open(VALIDATING13, 'w') as validating_data13, \
		# open(VALIDATING14, 'w') as validating_data14, \
		# open(VALIDATING15, 'w') as validating_data15, \
		# open(VALIDATING16, 'w') as validating_data16, \
		# open(VALIDATING17, 'w') as validating_data17, \
		# open(VALIDATING18, 'w') as validating_data18, \
		# open(VALIDATING19, 'w') as validating_data19, \
		# open(VALIDATING20, 'w') as validating_data20, \
		# open(VALIDATING21, 'w') as validating_data21, \
		# open(VALIDATING22, 'w') as validating_data22, \
		# open(VALIDATING23, 'w') as validating_data23, \
		
		mode_0 = 0
		mode_1 = 0
		mode_2 = 0
		mode_3 = 0
		mode_4 = 0
		mode_5 = 0
		mode_6 = 0
		mode_7 = 0
		mode_8 = 0
		mode_9 = 0
		mode_10 = 0
		mode_11 = 0
		mode_12 = 0
		mode_13 = 0
		mode_14 = 0
		mode_15 = 0
		mode_16 = 0
		mode_17 = 0
		mode_18 = 0
		mode_19 = 0
		mode_20 = 0
		mode_21 = 0
		mode_22 = 0
		# mode_23 = 0
		# mode_24 = 0
		# mode_25 = 0
		# mode_26 = 0
		# mode_27 = 0
		
		for line in orig_data:
			
			if line[-3:-2] == ',':
				# print("yes, it is a comma.")
				last_char_in_line = int(line[-2:-1])
			else:
				last_char_in_line = int(line[-3:-1])
			
			mode = last_char_in_line
			
			if mode == 0:
				mode_0 += 1
				if mode_0 <= 9000:
					training_data.write(line)
				elif 9000 < mode_0 <= 10000:
					validating_data.write(line)
					validating_data0.write(line)
				elif 10000 < mode_0 <= 11000:
					testing_data.write(line)
			
			elif mode == 1:
				mode_1 += 1
				if mode_1 <= 9000:
					training_data.write(line)
				elif 9000 < mode_1 <= 10000:
					validating_data.write(line)
					validating_data1.write(line)
				elif 10000 < mode_1 <= 11000:
					testing_data.write(line)
			
			elif mode == 2:
				mode_2 += 1
				if mode_2 <= 9000:
					training_data.write(line)
				elif 9000 < mode_2 <= 10000:
					validating_data.write(line)
					validating_data2.write(line)
				elif 10000 < mode_2 <= 11000:
					testing_data.write(line)
			
			elif mode == 3:
				mode_3 += 1
				if mode_3 <= 9000:
					training_data.write(line)
				elif 9000 < mode_3 <= 10000:
					validating_data.write(line)
				# validating_data3.write(line)
				elif 10000 < mode_3 <= 11000:
					testing_data.write(line)
			
			elif mode == 4:
				mode_4 += 1
				if mode_4 <= 9000:
					training_data.write(line)
				elif 9000 < mode_4 <= 10000:
					validating_data.write(line)
				# validating_data3.write(line)
				elif 10000 < mode_4 <= 11000:
					testing_data.write(line)
			
			elif mode == 5:
				mode_5 += 1
				if mode_5 <= 9000:
					training_data.write(line)
				elif 9000 < mode_5 <= 10000:
					validating_data.write(line)
				# validating_data3.write(line)
				elif 10000 < mode_5 <= 11000:
					testing_data.write(line)
			
			elif mode == 6:
				mode_6 += 1
				if mode_6 <= 9000:
					training_data.write(line)
				elif 9000 < mode_6 <= 10000:
					validating_data.write(line)
				# validating_data3.write(line)
				elif 10000 < mode_6 <= 11000:
					testing_data.write(line)
			
			elif mode == 7:
				mode_7 += 1
				if mode_7 <= 9000:
					training_data.write(line)
				elif 9000 < mode_7 <= 10000:
					validating_data.write(line)
				# validating_data3.write(line)
				elif 10000 < mode_7 <= 11000:
					testing_data.write(line)
			
			elif mode == 8:
				mode_8 += 1
				if mode_8 <= 9000:
					training_data.write(line)
				elif 9000 < mode_8 <= 10000:
					validating_data.write(line)
				# validating_data3.write(line)
				elif 10000 < mode_8 <= 11000:
					testing_data.write(line)
			
			elif mode == 9:
				mode_9 += 1
				if mode_9 <= 9000:
					training_data.write(line)
				elif 9000 < mode_9 <= 10000:
					validating_data.write(line)
				# validating_data3.write(line)
				elif 10000 < mode_9 <= 11000:
					testing_data.write(line)
			
			elif mode == 10:
				mode_10 += 1
				if mode_10 <= 9000:
					training_data.write(line)
				elif 9000 < mode_10 <= 10000:
					validating_data.write(line)
				# validating_data3.write(line)
				elif 10000 < mode_10 <= 11000:
					testing_data.write(line)
			
			elif mode == 11:
				mode_11 += 1
				if mode_11 <= 9000:
					training_data.write(line)
				elif 9000 < mode_11 <= 10000:
					validating_data.write(line)
				# validating_data3.write(line)
				elif 10000 < mode_11 <= 11000:
					testing_data.write(line)
			
			elif mode == 12:
				mode_12 += 1
				if mode_12 <= 9000:
					training_data.write(line)
				elif 9000 < mode_12 <= 10000:
					validating_data.write(line)
				# validating_data3.write(line)
				elif 10000 < mode_12 <= 11000:
					testing_data.write(line)
			
			elif mode == 13:
				mode_13 += 1
				if mode_13 <= 9000:
					training_data.write(line)
				elif 9000 < mode_13 <= 10000:
					validating_data.write(line)
				# validating_data3.write(line)
				elif 10000 < mode_13 <= 11000:
					testing_data.write(line)
			
			elif mode == 14:
				mode_14 += 1
				if mode_14 <= 9000:
					training_data.write(line)
				elif 9000 < mode_14 <= 10000:
					validating_data.write(line)
				# validating_data3.write(line)
				elif 10000 < mode_14 <= 11000:
					testing_data.write(line)
			
			elif mode == 15:
				mode_15 += 1
				if mode_15 <= 9000:
					training_data.write(line)
				elif 9000 < mode_15 <= 10000:
					validating_data.write(line)
				# validating_data3.write(line)
				elif 10000 < mode_15 <= 11000:
					testing_data.write(line)
			
			elif mode == 16:
				mode_16 += 1
				if mode_16 <= 9000:
					training_data.write(line)
				elif 9000 < mode_16 <= 10000:
					validating_data.write(line)
				# validating_data3.write(line)
				elif 10000 < mode_16 <= 11000:
					testing_data.write(line)
			
			elif mode == 17:
				mode_17 += 1
				if mode_17 <= 9000:
					training_data.write(line)
				elif 9000 < mode_17 <= 10000:
					validating_data.write(line)
				# validating_data3.write(line)
				elif 10000 < mode_17 <= 11000:
					testing_data.write(line)
			
			elif mode == 18:
				mode_18 += 1
				if mode_18 <= 9000:
					training_data.write(line)
				elif 9000 < mode_18 <= 10000:
					validating_data.write(line)
				# validating_data3.write(line)
				elif 10000 < mode_18 <= 11000:
					testing_data.write(line)
			
			elif mode == 19:
				mode_19 += 1
				if mode_19 <= 9000:
					training_data.write(line)
				elif 9000 < mode_19 <= 10000:
					validating_data.write(line)
					validating_data19.write(line)
				elif 10000 < mode_19 <= 11000:
					testing_data.write(line)
			
			elif mode == 20:
				mode_20 += 1
				if mode_20 <= 9000:
					training_data.write(line)
				elif 9000 < mode_20 <= 10000:
					validating_data.write(line)
					validating_data20.write(line)
				elif 10000 < mode_20 <= 11000:
					testing_data.write(line)
			
			elif mode == 21:
				mode_21 += 1
				if mode_21 <= 9000:
					training_data.write(line)
				elif 9000 < mode_21 <= 10000:
					validating_data.write(line)
					validating_data21.write(line)
				elif 10000 < mode_21 <= 11000:
					testing_data.write(line)
			
			elif mode == 22:
				mode_22 += 1
				if mode_22 <= 9000:
					training_data.write(line)
				elif 9000 < mode_22 <= 10000:
					validating_data.write(line)
					validating_data22.write(line)
				elif 10000 < mode_22 <= 11000:
					testing_data.write(line)

	print('=================================================')
	end_timestamp = datetime.datetime.now()
	time_duration = end_timestamp - start_timestamp
	print('end at: ')
	print(end_timestamp)
	print('The time spent is:')
	print(time_duration)
	print('++++++++++++++++++++')


data_generator(ORIG=ORIG, TRAINING=TRAINING, VALIDATING=VALIDATING,
							 TESTING=TESTING,
							 VALIDATING0=VALIDATING0,
							 VALIDATING1=VALIDATING1,
							 VALIDATING2=VALIDATING2,
							 # VALIDATING3=VALIDATING3,
							 # VALIDATING4=VALIDATING4,
							 # VALIDATING5=VALIDATING5,
							 # VALIDATING6=VALIDATING6,
							 # VALIDATING7=VALIDATING7,
							 # VALIDATING8=VALIDATING8,
							 # VALIDATING9=VALIDATING9,
							 # VALIDATING10=VALIDATING10,
							 # VALIDATING11=VALIDATING11,
							 # VALIDATING12=VALIDATING12,
							 # VALIDATING13=VALIDATING13,
							 # VALIDATING14=VALIDATING14,
							 # VALIDATING15=VALIDATING15,
							 # VALIDATING16=VALIDATING16,
							 # VALIDATING17=VALIDATING17,
							 # VALIDATING18=VALIDATING18,
							 VALIDATING19=VALIDATING19,
							 VALIDATING20=VALIDATING20,
							 VALIDATING21=VALIDATING21,
							 VALIDATING22=VALIDATING22,
							 # VALIDATING26=VALIDATING26,
							 # VALIDATING27=VALIDATING27,
							 )
