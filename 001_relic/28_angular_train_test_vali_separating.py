# ==============================================================================
# Author: Pharrell_WANG
# Date: 2017/6/28
# ==============================================================================
"""
Functionality:

	For getting angular modes 2, 3, 4, ..., 33. i.e., [2, 33]. Notice mode 34
	is not considered. Since i believe that angular 34 got the same dir as
	angular 2.

Grouping:
	only [9, 10, 11], [25, 26, 27] are grouped. Hence we have 28 (33-1-4=28) classes.

Sizes of data sets:
	Training data size: 9000 for each class
	Testing data size: 1000 for each class
	Validating data size: 1000 for each class

Notes:
	The sizes are determined from the consideration that after removing smooth blocks
	where ave < 90, the minimum number of samples of each class is a little more
	than 11000 (refer to
	'statistics/smooth_removed_AVE90_08x08_counting_results.txt') for details.
"""
# notes: 3 things need to be changed for different block sizes:
# 1. the three border values for dividing data into three sets
# 2. 'ORIG = homedir + '/data/step2_output/size_16_files.csv';---> "16" need to be changed accordingly
# 3. search all '08x08', replace them all accordingly
# then you should be good to go

import os

homedir = os.environ['HOME']
ORIG = homedir + '/data/smooth_removed/ave_90_size_08_files.csv'
TRAINING = homedir + '/data/thirty_two_angular_classes/train_08x08.csv'
TESTING = homedir + '/data/thirty_two_angular_classes/test_08x08.csv'
VALIDATING = homedir + '/data/thirty_two_angular_classes/validate_08x08.csv'

VALIDATING0 = homedir + '/data/thirty_two_angular_classes/validate_08x08_0.csv'
VALIDATING1 = homedir + '/data/thirty_two_angular_classes/validate_08x08_1.csv'
VALIDATING2 = homedir + '/data/thirty_two_angular_classes/validate_08x08_2.csv'
VALIDATING3 = homedir + '/data/thirty_two_angular_classes/validate_08x08_3.csv'
VALIDATING4 = homedir + '/data/thirty_two_angular_classes/validate_08x08_4.csv'
VALIDATING5 = homedir + '/data/thirty_two_angular_classes/validate_08x08_5.csv'
VALIDATING6 = homedir + '/data/thirty_two_angular_classes/validate_08x08_6.csv'
VALIDATING7 = homedir + '/data/thirty_two_angular_classes/validate_08x08_7.csv'
VALIDATING8 = homedir + '/data/thirty_two_angular_classes/validate_08x08_8.csv'
VALIDATING9 = homedir + '/data/thirty_two_angular_classes/validate_08x08_9.csv'
VALIDATING10 = homedir + '/data/thirty_two_angular_classes/validate_08x08_10.csv'
VALIDATING11 = homedir + '/data/thirty_two_angular_classes/validate_08x08_11.csv'
VALIDATING12 = homedir + '/data/thirty_two_angular_classes/validate_08x08_12.csv'
VALIDATING13 = homedir + '/data/thirty_two_angular_classes/validate_08x08_13.csv'
VALIDATING14 = homedir + '/data/thirty_two_angular_classes/validate_08x08_14.csv'
VALIDATING15 = homedir + '/data/thirty_two_angular_classes/validate_08x08_15.csv'
VALIDATING16 = homedir + '/data/thirty_two_angular_classes/validate_08x08_16.csv'
VALIDATING17 = homedir + '/data/thirty_two_angular_classes/validate_08x08_17.csv'
VALIDATING18 = homedir + '/data/thirty_two_angular_classes/validate_08x08_18.csv'
VALIDATING19 = homedir + '/data/thirty_two_angular_classes/validate_08x08_19.csv'
VALIDATING20 = homedir + '/data/thirty_two_angular_classes/validate_08x08_20.csv'
VALIDATING21 = homedir + '/data/thirty_two_angular_classes/validate_08x08_21.csv'
VALIDATING22 = homedir + '/data/thirty_two_angular_classes/validate_08x08_22.csv'
VALIDATING23 = homedir + '/data/thirty_two_angular_classes/validate_08x08_23.csv'
VALIDATING24 = homedir + '/data/thirty_two_angular_classes/validate_08x08_24.csv'
VALIDATING25 = homedir + '/data/thirty_two_angular_classes/validate_08x08_25.csv'
VALIDATING26 = homedir + '/data/thirty_two_angular_classes/validate_08x08_26.csv'
VALIDATING27 = homedir + '/data/thirty_two_angular_classes/validate_08x08_27.csv'


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
									 # VALIDATING19,
									 # VALIDATING20,
									 # VALIDATING21,
									 # VALIDATING22,
									 # VALIDATING23,
									 # VALIDATING24,
									 # VALIDATING25,
									 # VALIDATING26,
									 # VALIDATING27,
									 # VALIDATING28,
									 # VALIDATING29,
									 VALIDATING30,
									 VALIDATING31,
									 VALIDATING32,
									 VALIDATING33,
									 VALIDATING34,
									 VALIDATING35,
									 VALIDATING36):
	with open(ORIG, 'r') as orig_data, open(TRAINING, 'w') as training_data, \
		open(TESTING, 'w') as testing_data, \
		open(VALIDATING, 'w') as validating_data, \
		open(VALIDATING0, 'w') as validating_data0, \
		open(VALIDATING1, 'w') as validating_data1, \
		open(VALIDATING2, 'w') as validating_data2, \
		open(VALIDATING30, 'w') as validating_data30, \
		open(VALIDATING31, 'w') as validating_data31, \
		open(VALIDATING32, 'w') as validating_data32, \
		open(VALIDATING33, 'w') as validating_data33, \
		open(VALIDATING34, 'w') as validating_data34, \
		open(VALIDATING35, 'w') as validating_data35, \
		open(VALIDATING36, 'w') as validating_data36:
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
		mode_23 = 0
		mode_24 = 0
		mode_25 = 0
		mode_26 = 0
		mode_27 = 0
		mode_28 = 0
		mode_29 = 0
		mode_30 = 0
		mode_31 = 0
		
		for line in orig_data:
			
			if line[-3:-2] == ',':
				# print("yes, it is a comma.")
				last_char_in_line = int(line[-2:-1])
			else:
				last_char_in_line = int(line[-3:-1])
			
			mode = last_char_in_line
			
			if mode == 0:
				mode_0 += 1
				if mode_0 <= 309255:
					training_data.write(line)
				elif 309255 < mode_0 <= 312755:
					validating_data.write(line)
					validating_data0.write(line)
				elif 312755 < mode_0 <= 316255:
					testing_data.write(line)
			
			elif mode == 1:
				mode_1 += 1
				if mode_1 <= 101883:
					training_data.write(line)
				elif 101883 < mode_1 <= 105383:
					validating_data.write(line)
					validating_data1.write(line)
				elif 105383 < mode_1 <= 108883:
					testing_data.write(line)
			
			elif mode == 2:
				mode_2 += 1
				if mode_2 <= 2085:
					training_data.write(line)
				elif 2085 < mode_2 <= 2285:
					validating_data.write(line)
					validating_data2.write(line)
				elif 2285 < mode_2 <= 2485:
					testing_data.write(line)
			
			elif mode == 3:
				mode_3 += 1
				if mode_3 <= 2085:
					training_data.write(line)
				elif 2085 < mode_3 <= 2285:
					validating_data.write(line)
					# validating_data3.write(line)
				elif 2285 < mode_3 <= 2485:
					testing_data.write(line)
			
			elif mode == 4:
				mode_4 += 1
				if mode_4 <= 2085:
					training_data.write(line)
				elif 2085 < mode_4 <= 2285:
					validating_data.write(line)
					# validating_data3.write(line)
				elif 2285 < mode_4 <= 2485:
					testing_data.write(line)
			
			elif mode == 5:
				mode_5 += 1
				if mode_5 <= 2085:
					training_data.write(line)
				elif 2085 < mode_5 <= 2285:
					validating_data.write(line)
					# validating_data3.write(line)
				elif 2285 < mode_5 <= 2485:
					testing_data.write(line)
			
			elif mode == 6:
				mode_6 += 1
				if mode_6 <= 2085:
					training_data.write(line)
				elif 2085 < mode_6 <= 2285:
					validating_data.write(line)
					# validating_data3.write(line)
				elif 2285 < mode_6 <= 2485:
					testing_data.write(line)
			
			elif mode == 7:
				mode_7 += 1
				if mode_7 <= 2085:
					training_data.write(line)
				elif 2085 < mode_7 <= 2285:
					validating_data.write(line)
					# validating_data3.write(line)
				elif 2285 < mode_7 <= 2485:
					testing_data.write(line)
			
			elif mode == 8:
				mode_8 += 1
				if mode_8 <= 2085:
					training_data.write(line)
				elif 2085 < mode_8 <= 2285:
					validating_data.write(line)
					# validating_data3.write(line)
				elif 2285 < mode_8 <= 2485:
					testing_data.write(line)
			
			elif mode == 9:
				mode_9 += 1
				if mode_9 <= 2085:
					training_data.write(line)
				elif 2085 < mode_9 <= 2285:
					validating_data.write(line)
					# validating_data3.write(line)
				elif 2285 < mode_9 <= 2485:
					testing_data.write(line)
			
			elif mode == 10:
				mode_10 += 1
				if mode_10 <= 2085:
					training_data.write(line)
				elif 2085 < mode_10 <= 2285:
					validating_data.write(line)
					# validating_data3.write(line)
				elif 2285 < mode_10 <= 2485:
					testing_data.write(line)
			
			elif mode == 11:
				mode_11 += 1
				if mode_11 <= 2085:
					training_data.write(line)
				elif 2085 < mode_11 <= 2285:
					validating_data.write(line)
					# validating_data3.write(line)
				elif 2285 < mode_11 <= 2485:
					testing_data.write(line)
			
			elif mode == 12:
				mode_12 += 1
				if mode_12 <= 2085:
					training_data.write(line)
				elif 2085 < mode_12 <= 2285:
					validating_data.write(line)
					# validating_data3.write(line)
				elif 2285 < mode_12 <= 2485:
					testing_data.write(line)
			
			elif mode == 13:
				mode_13 += 1
				if mode_13 <= 2085:
					training_data.write(line)
				elif 2085 < mode_13 <= 2285:
					validating_data.write(line)
					# validating_data3.write(line)
				elif 2285 < mode_13 <= 2485:
					testing_data.write(line)
			
			elif mode == 14:
				mode_14 += 1
				if mode_14 <= 2085:
					training_data.write(line)
				elif 2085 < mode_14 <= 2285:
					validating_data.write(line)
					# validating_data3.write(line)
				elif 2285 < mode_14 <= 2485:
					testing_data.write(line)
			
			elif mode == 15:
				mode_15 += 1
				if mode_15 <= 2085:
					training_data.write(line)
				elif 2085 < mode_15 <= 2285:
					validating_data.write(line)
					# validating_data3.write(line)
				elif 2285 < mode_15 <= 2485:
					testing_data.write(line)
			
			elif mode == 16:
				mode_16 += 1
				if mode_16 <= 2085:
					training_data.write(line)
				elif 2085 < mode_16 <= 2285:
					validating_data.write(line)
					# validating_data3.write(line)
				elif 2285 < mode_16 <= 2485:
					testing_data.write(line)
			
			elif mode == 17:
				mode_17 += 1
				if mode_17 <= 2085:
					training_data.write(line)
				elif 2085 < mode_17 <= 2285:
					validating_data.write(line)
					# validating_data3.write(line)
				elif 2285 < mode_17 <= 2485:
					testing_data.write(line)
			
			elif mode == 18:
				mode_18 += 1
				if mode_18 <= 2085:
					training_data.write(line)
				elif 2085 < mode_18 <= 2285:
					validating_data.write(line)
					# validating_data3.write(line)
				elif 2285 < mode_18 <= 2485:
					testing_data.write(line)
			
			elif mode == 19:
				mode_19 += 1
				if mode_19 <= 2085:
					training_data.write(line)
				elif 2085 < mode_19 <= 2285:
					validating_data.write(line)
					# validating_data3.write(line)
				elif 2285 < mode_19 <= 2485:
					testing_data.write(line)
			
			elif mode == 20:
				mode_20 += 1
				if mode_20 <= 2085:
					training_data.write(line)
				elif 2085 < mode_20 <= 2285:
					validating_data.write(line)
					# validating_data3.write(line)
				elif 2285 < mode_20 <= 2485:
					testing_data.write(line)
			
			elif mode == 21:
				mode_21 += 1
				if mode_21 <= 2085:
					training_data.write(line)
				elif 2085 < mode_21 <= 2285:
					validating_data.write(line)
					# validating_data3.write(line)
				elif 2285 < mode_21 <= 2485:
					testing_data.write(line)
			
			elif mode == 22:
				mode_22 += 1
				if mode_22 <= 2085:
					training_data.write(line)
				elif 2085 < mode_22 <= 2285:
					validating_data.write(line)
					# validating_data3.write(line)
				elif 2285 < mode_22 <= 2485:
					testing_data.write(line)
			
			elif mode == 23:
				mode_23 += 1
				if mode_23 <= 2085:
					training_data.write(line)
				elif 2085 < mode_23 <= 2285:
					validating_data.write(line)
					# validating_data3.write(line)
				elif 2285 < mode_23 <= 2485:
					testing_data.write(line)
			
			elif mode == 24:
				mode_24 += 1
				if mode_24 <= 2085:
					training_data.write(line)
				elif 2085 < mode_24 <= 2285:
					validating_data.write(line)
					# validating_data3.write(line)
				elif 2285 < mode_24 <= 2485:
					testing_data.write(line)
			
			elif mode == 25:
				mode_25 += 1
				if mode_25 <= 2085:
					training_data.write(line)
				elif 2085 < mode_25 <= 2285:
					validating_data.write(line)
					# validating_data3.write(line)
				elif 2285 < mode_25 <= 2485:
					testing_data.write(line)
			
			elif mode == 26:
				mode_26 += 1
				if mode_26 <= 2085:
					training_data.write(line)
				elif 2085 < mode_26 <= 2285:
					validating_data.write(line)
					# validating_data3.write(line)
				elif 2285 < mode_26 <= 2485:
					testing_data.write(line)
			
			elif mode == 27:
				mode_27 += 1
				if mode_27 <= 2085:
					training_data.write(line)
				elif 2085 < mode_27 <= 2285:
					validating_data.write(line)
					# validating_data3.write(line)
				elif 2285 < mode_27 <= 2485:
					testing_data.write(line)
			
			elif mode == 28:
				mode_28 += 1
				if mode_28 <= 2085:
					training_data.write(line)
				elif 2085 < mode_28 <= 2285:
					validating_data.write(line)
					# validating_data3.write(line)
				elif 2285 < mode_28 <= 2485:
					testing_data.write(line)
			
			elif mode == 29:
				mode_29 += 1
				if mode_29 <= 2085:
					training_data.write(line)
				elif 2085 < mode_29 <= 2285:
					validating_data.write(line)
					# validating_data3.write(line)
				elif 2285 < mode_29 <= 2485:
					testing_data.write(line)
			
			elif mode == 30:
				mode_30 += 1
				if mode_30 <= 2085:
					training_data.write(line)
				elif 2085 < mode_30 <= 2285:
					validating_data.write(line)
					validating_data30.write(line)
				elif 2285 < mode_30 <= 2485:
					testing_data.write(line)
			
			elif mode == 31:
				mode_31 += 1
				if mode_31 <= 2085:
					training_data.write(line)
				elif 2085 < mode_31 <= 2285:
					validating_data.write(line)
					validating_data31.write(line)
				elif 2285 < mode_31 <= 2485:
					testing_data.write(line)


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
							 # VALIDATING19=VALIDATING19,
							 # VALIDATING20=VALIDATING20,
							 # VALIDATING21=VALIDATING21,
							 # VALIDATING22=VALIDATING22,
							 # VALIDATING23=VALIDATING23,
							 # VALIDATING24=VALIDATING24,
							 # VALIDATING25=VALIDATING25,
							 # VALIDATING26=VALIDATING26,
							 # VALIDATING27=VALIDATING27,
							 # VALIDATING28=VALIDATING28,
							 # VALIDATING29=VALIDATING29,
							 VALIDATING30=VALIDATING30,
							 VALIDATING31=VALIDATING31,
							 VALIDATING32=VALIDATING32,
							 VALIDATING33=VALIDATING33,
							 VALIDATING34=VALIDATING34,
							 VALIDATING35=VALIDATING35,
							 VALIDATING36=VALIDATING36,
							 )
