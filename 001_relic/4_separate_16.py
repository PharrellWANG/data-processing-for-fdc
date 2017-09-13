# ==============================================================================
# Author: Pharrell_WANG
# Date: 2017/6/28
# ==============================================================================
# from csv_mode_counter import csv_mode_preprocessing
TRAINING_DATA_PERCENT = 0.6
TESTING_DATA_PERCENT = 0.2
VALIDATING_DATA_PERCENT = 0.2
assert (
    TRAINING_DATA_PERCENT + TESTING_DATA_PERCENT + VALIDATING_DATA_PERCENT == 1)

# ===========for size 16x16=========== START
# Question  : why try 16x16 first?
# Answer    :
#   1. It has far more data samples than 16x16;
#   2. It seems 8x8 is just too small.)

# ======>> calculation start (we have to find integer after division)
# >>> 13837 * 0.6
# 8302.199999999999
# >>> 13836 * 0.6
# 5815.6
# >>> 6299 * 0.6
# 5815.0
# >>> 6299 * 0.2
# 2767.0
# >>> 6299 * 0.2
# 2767.0
# >>>
# ======>> calculation end

# Based on the above calculation, i decided to choose the size as below:

# total 6299, we drop 2 samples for dividing
# ---> divided into
# train:(0,5815];
# test:(5815, 5815+2767 = 6057];
# validation: (5815+2767 = 6057, 5815+2767+2767 = 6299]
# ===========for size 16x16=========== END

# notes: 3 things need to be changed for different block sizes:
# 1. the three border values for dividing data into three sets
# 2. 'ORIG = homedir + '/data/step2_output/size_16_files.csv';---> "16" need to be changed accordingly
# 3. search all '16x16', replace them all accordingly
# then you should be good to go

import os

homedir = os.environ['HOME']
ORIG = homedir + '/data/step2_output/size_16_files.csv'
TRAINING = homedir + '/data/two_classes/separate_classes/train_16x16.csv'
TESTING = homedir + '/data/two_classes/separate_classes/test_16x16.csv'
VALIDATING = homedir + '/data/two_classes/separate_classes/validate_16x16.csv'

VALIDATING0 = homedir + '/data/two_classes/separate_classes/validate_16x16_0.csv'
VALIDATING1 = homedir + '/data/two_classes/separate_classes/validate_16x16_1.csv'
VALIDATING2 = homedir + '/data/two_classes/separate_classes/validate_16x16_2.csv'
VALIDATING3 = homedir + '/data/two_classes/separate_classes/validate_16x16_3.csv'
VALIDATING4 = homedir + '/data/two_classes/separate_classes/validate_16x16_4.csv'
VALIDATING5 = homedir + '/data/two_classes/separate_classes/validate_16x16_5.csv'
VALIDATING6 = homedir + '/data/two_classes/separate_classes/validate_16x16_6.csv'
VALIDATING7 = homedir + '/data/two_classes/separate_classes/validate_16x16_7.csv'
VALIDATING8 = homedir + '/data/two_classes/separate_classes/validate_16x16_8.csv'
VALIDATING9 = homedir + '/data/two_classes/separate_classes/validate_16x16_9.csv'
VALIDATING10 = homedir + '/data/two_classes/separate_classes/validate_16x16_10.csv'
VALIDATING11 = homedir + '/data/two_classes/separate_classes/validate_16x16_11.csv'
VALIDATING12 = homedir + '/data/two_classes/separate_classes/validate_16x16_12.csv'
VALIDATING13 = homedir + '/data/two_classes/separate_classes/validate_16x16_13.csv'
VALIDATING14 = homedir + '/data/two_classes/separate_classes/validate_16x16_14.csv'
VALIDATING15 = homedir + '/data/two_classes/separate_classes/validate_16x16_15.csv'
VALIDATING16 = homedir + '/data/two_classes/separate_classes/validate_16x16_16.csv'
VALIDATING17 = homedir + '/data/two_classes/separate_classes/validate_16x16_17.csv'
VALIDATING18 = homedir + '/data/two_classes/separate_classes/validate_16x16_18.csv'
VALIDATING19 = homedir + '/data/two_classes/separate_classes/validate_16x16_19.csv'
VALIDATING20 = homedir + '/data/two_classes/separate_classes/validate_16x16_20.csv'
VALIDATING21 = homedir + '/data/two_classes/separate_classes/validate_16x16_21.csv'
VALIDATING22 = homedir + '/data/two_classes/separate_classes/validate_16x16_22.csv'
VALIDATING23 = homedir + '/data/two_classes/separate_classes/validate_16x16_23.csv'
VALIDATING24 = homedir + '/data/two_classes/separate_classes/validate_16x16_24.csv'
VALIDATING25 = homedir + '/data/two_classes/separate_classes/validate_16x16_25.csv'
VALIDATING26 = homedir + '/data/two_classes/separate_classes/validate_16x16_26.csv'
VALIDATING27 = homedir + '/data/two_classes/separate_classes/validate_16x16_27.csv'
VALIDATING28 = homedir + '/data/two_classes/separate_classes/validate_16x16_28.csv'
VALIDATING29 = homedir + '/data/two_classes/separate_classes/validate_16x16_29.csv'
VALIDATING30 = homedir + '/data/two_classes/separate_classes/validate_16x16_30.csv'
VALIDATING31 = homedir + '/data/two_classes/separate_classes/validate_16x16_31.csv'
VALIDATING32 = homedir + '/data/two_classes/separate_classes/validate_16x16_32.csv'
VALIDATING33 = homedir + '/data/two_classes/separate_classes/validate_16x16_33.csv'
VALIDATING34 = homedir + '/data/two_classes/separate_classes/validate_16x16_34.csv'
VALIDATING35 = homedir + '/data/two_classes/separate_classes/validate_16x16_35.csv'
VALIDATING36 = homedir + '/data/two_classes/separate_classes/validate_16x16_36.csv'


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
        mode_32 = 0
        mode_33 = 0
        mode_34 = 0
        mode_35 = 0
        mode_36 = 0

        for line in orig_data:

            if line[-3:-2] == ',':
                # print("yes, it is a comma.")
                last_char_in_line = int(line[-2:-1])
            else:
                last_char_in_line = int(line[-3:-1])

            mode = last_char_in_line

            if mode == 0:
                mode_0 += 1
                if mode_0 <= 775885:
                    training_data.write(line)
                elif 775885 < mode_0 <= 780885:
                    validating_data.write(line)
                    validating_data0.write(line)
                elif 780885 < mode_0 <= 785885:
                    testing_data.write(line)

            elif mode == 1:
                mode_1 += 1
                if mode_1 <= 268221:
                    training_data.write(line)
                elif 268221 < mode_1 <= 273221:
                    validating_data.write(line)
                    validating_data1.write(line)
                elif 273221 < mode_1 <= 278221:
                    testing_data.write(line)

            elif mode == 2:
                mode_2 += 1
                if mode_2 <= 5815:
                    training_data.write(line)
                elif 5815 < mode_2 <= 6057:
                    validating_data.write(line)
                    validating_data2.write(line)
                elif 6057 < mode_2 <= 6299:
                    testing_data.write(line)

            elif mode == 3:
                mode_3 += 1
                if mode_3 <= 5815:
                    training_data.write(line)
                elif 5815 < mode_3 <= 6057:
                    validating_data.write(line)
                    # validating_data3.write(line)
                elif 6057 < mode_3 <= 6299:
                    testing_data.write(line)

            elif mode == 4:
                mode_4 += 1
                if mode_4 <= 5815:
                    training_data.write(line)
                elif 5815 < mode_4 <= 6057:
                    validating_data.write(line)
                    # validating_data3.write(line)
                elif 6057 < mode_4 <= 6299:
                    testing_data.write(line)

            elif mode == 5:
                mode_5 += 1
                if mode_5 <= 5815:
                    training_data.write(line)
                elif 5815 < mode_5 <= 6057:
                    validating_data.write(line)
                    # validating_data3.write(line)
                elif 6057 < mode_5 <= 6299:
                    testing_data.write(line)

            elif mode == 6:
                mode_6 += 1
                if mode_6 <= 5815:
                    training_data.write(line)
                elif 5815 < mode_6 <= 6057:
                    validating_data.write(line)
                    # validating_data3.write(line)
                elif 6057 < mode_6 <= 6299:
                    testing_data.write(line)

            elif mode == 7:
                mode_7 += 1
                if mode_7 <= 5815:
                    training_data.write(line)
                elif 5815 < mode_7 <= 6057:
                    validating_data.write(line)
                    # validating_data3.write(line)
                elif 6057 < mode_7 <= 6299:
                    testing_data.write(line)

            elif mode == 8:
                mode_8 += 1
                if mode_8 <= 5815:
                    training_data.write(line)
                elif 5815 < mode_8 <= 6057:
                    validating_data.write(line)
                    # validating_data3.write(line)
                elif 6057 < mode_8 <= 6299:
                    testing_data.write(line)

            elif mode == 9:
                mode_9 += 1
                if mode_9 <= 5815:
                    training_data.write(line)
                elif 5815 < mode_9 <= 6057:
                    validating_data.write(line)
                    # validating_data3.write(line)
                elif 6057 < mode_9 <= 6299:
                    testing_data.write(line)

            elif mode == 10:
                mode_10 += 1
                if mode_10 <= 5815:
                    training_data.write(line)
                elif 5815 < mode_10 <= 6057:
                    validating_data.write(line)
                    # validating_data3.write(line)
                elif 6057 < mode_10 <= 6299:
                    testing_data.write(line)

            elif mode == 11:
                mode_11 += 1
                if mode_11 <= 5815:
                    training_data.write(line)
                elif 5815 < mode_11 <= 6057:
                    validating_data.write(line)
                    # validating_data3.write(line)
                elif 6057 < mode_11 <= 6299:
                    testing_data.write(line)

            elif mode == 12:
                mode_12 += 1
                if mode_12 <= 5815:
                    training_data.write(line)
                elif 5815 < mode_12 <= 6057:
                    validating_data.write(line)
                    # validating_data3.write(line)
                elif 6057 < mode_12 <= 6299:
                    testing_data.write(line)

            elif mode == 13:
                mode_13 += 1
                if mode_13 <= 5815:
                    training_data.write(line)
                elif 5815 < mode_13 <= 6057:
                    validating_data.write(line)
                    # validating_data3.write(line)
                elif 6057 < mode_13 <= 6299:
                    testing_data.write(line)

            elif mode == 14:
                mode_14 += 1
                if mode_14 <= 5815:
                    training_data.write(line)
                elif 5815 < mode_14 <= 6057:
                    validating_data.write(line)
                    # validating_data3.write(line)
                elif 6057 < mode_14 <= 6299:
                    testing_data.write(line)

            elif mode == 15:
                mode_15 += 1
                if mode_15 <= 5815:
                    training_data.write(line)
                elif 5815 < mode_15 <= 6057:
                    validating_data.write(line)
                    # validating_data3.write(line)
                elif 6057 < mode_15 <= 6299:
                    testing_data.write(line)

            elif mode == 16:
                mode_16 += 1
                if mode_16 <= 5815:
                    training_data.write(line)
                elif 5815 < mode_16 <= 6057:
                    validating_data.write(line)
                    # validating_data3.write(line)
                elif 6057 < mode_16 <= 6299:
                    testing_data.write(line)

            elif mode == 17:
                mode_17 += 1
                if mode_17 <= 5815:
                    training_data.write(line)
                elif 5815 < mode_17 <= 6057:
                    validating_data.write(line)
                    # validating_data3.write(line)
                elif 6057 < mode_17 <= 6299:
                    testing_data.write(line)

            elif mode == 18:
                mode_18 += 1
                if mode_18 <= 5815:
                    training_data.write(line)
                elif 5815 < mode_18 <= 6057:
                    validating_data.write(line)
                    # validating_data3.write(line)
                elif 6057 < mode_18 <= 6299:
                    testing_data.write(line)

            elif mode == 19:
                mode_19 += 1
                if mode_19 <= 5815:
                    training_data.write(line)
                elif 5815 < mode_19 <= 6057:
                    validating_data.write(line)
                    # validating_data3.write(line)
                elif 6057 < mode_19 <= 6299:
                    testing_data.write(line)

            elif mode == 20:
                mode_20 += 1
                if mode_20 <= 5815:
                    training_data.write(line)
                elif 5815 < mode_20 <= 6057:
                    validating_data.write(line)
                    # validating_data3.write(line)
                elif 6057 < mode_20 <= 6299:
                    testing_data.write(line)

            elif mode == 21:
                mode_21 += 1
                if mode_21 <= 5815:
                    training_data.write(line)
                elif 5815 < mode_21 <= 6057:
                    validating_data.write(line)
                    # validating_data3.write(line)
                elif 6057 < mode_21 <= 6299:
                    testing_data.write(line)

            elif mode == 22:
                mode_22 += 1
                if mode_22 <= 5815:
                    training_data.write(line)
                elif 5815 < mode_22 <= 6057:
                    validating_data.write(line)
                    # validating_data3.write(line)
                elif 6057 < mode_22 <= 6299:
                    testing_data.write(line)

            elif mode == 23:
                mode_23 += 1
                if mode_23 <= 5815:
                    training_data.write(line)
                elif 5815 < mode_23 <= 6057:
                    validating_data.write(line)
                    # validating_data3.write(line)
                elif 6057 < mode_23 <= 6299:
                    testing_data.write(line)

            elif mode == 24:
                mode_24 += 1
                if mode_24 <= 5815:
                    training_data.write(line)
                elif 5815 < mode_24 <= 6057:
                    validating_data.write(line)
                    # validating_data3.write(line)
                elif 6057 < mode_24 <= 6299:
                    testing_data.write(line)

            elif mode == 25:
                mode_25 += 1
                if mode_25 <= 5815:
                    training_data.write(line)
                elif 5815 < mode_25 <= 6057:
                    validating_data.write(line)
                    # validating_data3.write(line)
                elif 6057 < mode_25 <= 6299:
                    testing_data.write(line)

            elif mode == 26:
                mode_26 += 1
                if mode_26 <= 5815:
                    training_data.write(line)
                elif 5815 < mode_26 <= 6057:
                    validating_data.write(line)
                    # validating_data3.write(line)
                elif 6057 < mode_26 <= 6299:
                    testing_data.write(line)

            elif mode == 27:
                mode_27 += 1
                if mode_27 <= 5815:
                    training_data.write(line)
                elif 5815 < mode_27 <= 6057:
                    validating_data.write(line)
                    # validating_data3.write(line)
                elif 6057 < mode_27 <= 6299:
                    testing_data.write(line)

            elif mode == 28:
                mode_28 += 1
                if mode_28 <= 5815:
                    training_data.write(line)
                elif 5815 < mode_28 <= 6057:
                    validating_data.write(line)
                    # validating_data3.write(line)
                elif 6057 < mode_28 <= 6299:
                    testing_data.write(line)

            elif mode == 29:
                mode_29 += 1
                if mode_29 <= 5815:
                    training_data.write(line)
                elif 5815 < mode_29 <= 6057:
                    validating_data.write(line)
                    # validating_data3.write(line)
                elif 6057 < mode_29 <= 6299:
                    testing_data.write(line)

            elif mode == 30:
                mode_30 += 1
                if mode_30 <= 5815:
                    training_data.write(line)
                elif 5815 < mode_30 <= 6057:
                    validating_data.write(line)
                    validating_data30.write(line)
                elif 6057 < mode_30 <= 6299:
                    testing_data.write(line)

            elif mode == 31:
                mode_31 += 1
                if mode_31 <= 5815:
                    training_data.write(line)
                elif 5815 < mode_31 <= 6057:
                    validating_data.write(line)
                    validating_data31.write(line)
                elif 6057 < mode_31 <= 6299:
                    testing_data.write(line)

            elif mode == 32:
                mode_32 += 1
                if mode_32 <= 5815:
                    training_data.write(line)
                elif 5815 < mode_32 <= 6057:
                    validating_data.write(line)
                    validating_data32.write(line)
                elif 6057 < mode_32 <= 6299:
                    testing_data.write(line)

            elif mode == 33:
                mode_33 += 1
                if mode_33 <= 5815:
                    training_data.write(line)
                elif 5815 < mode_33 <= 6057:
                    validating_data.write(line)
                    validating_data33.write(line)
                elif 6057 < mode_33 <= 6299:
                    testing_data.write(line)

            elif mode == 34:
                mode_34 += 1
                if mode_34 <= 5815:
                    training_data.write(line)
                elif 5815 < mode_34 <= 6057:
                    validating_data.write(line)
                    validating_data34.write(line)
                elif 6057 < mode_34 <= 6299:
                    testing_data.write(line)

            elif mode == 35:
                mode_35 += 1
                if mode_35 <= 599457:
                    training_data.write(line)
                elif 599457 < mode_35 <= 601457:
                    validating_data.write(line)
                    validating_data35.write(line)
                elif 601457 < mode_35 <= 603457:
                    testing_data.write(line)

            elif mode == 36:
                mode_36 += 1
                if mode_36 <= 252754:
                    training_data.write(line)
                elif 252754 < mode_36 <= 254754:
                    validating_data.write(line)
                    validating_data36.write(line)
                elif 254754 < mode_36 <= 256754:
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
