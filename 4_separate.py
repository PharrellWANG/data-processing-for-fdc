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

# ===========for size 08x08=========== START
# Question  : why try 08x08 first?
# Answer    :
#   1. It has far more data samples than 08x08;
#   2. It seems 8x8 is just too small.)

# ======>> calculation start (we have to find integer after division)
# >>> 13837 * 0.6
# 8302.199999999999
# >>> 13836 * 0.6
# 710.6
# >>> 3000 * 0.6
# 710.0
# >>> 3000 * 0.2
# 2767.0
# >>> 3000 * 0.2
# 2767.0
# >>>
# ======>> calculation end

# Based on the above calculation, i decided to choose the size as below:

# total 3000, we drop 2 samples for dividing
# ---> divided into
# train:(0,710];
# test:(710, 710+2767 = 1420];
# validation: (710+2767 = 1420, 710+2767+2767 = 3000]
# ===========for size 08x08=========== END

# notes: 3 things need to be changed for different block sizes:
# 1. the three border values for dividing data into three sets
# 2. 'ORIG = homedir + '/data/step2_output/size_16_files.csv';---> "16" need to be changed accordingly
# 3. search all '08x08', replace them all accordingly
# then you should be good to go

import os

homedir = os.environ['HOME']
# ORIG = homedir + '/data/last_trial/step2_output/size_08_files.csv'
ORIG = '/Users/pharrell_wang/data/last_trial/kendo/step2_output/size_08_files.csv'

TRAINING = homedir + '/data/last_trial/kendo/train_08x08.csv'
TESTING = homedir + '/data/last_trial/kendo/test_08x08.csv'
VALIDATING = homedir + '/data/last_trial/kendo/validate_08x08.csv'

VALIDATING0 = homedir + '/data/last_trial/kendo/validate_08x08_0.csv'
VALIDATING1 = homedir + '/data/last_trial/kendo/validate_08x08_1.csv'
VALIDATING2 = homedir + '/data/last_trial/kendo/validate_08x08_2.csv'
VALIDATING3 = homedir + '/data/last_trial/kendo/validate_08x08_3.csv'
VALIDATING4 = homedir + '/data/last_trial/kendo/validate_08x08_4.csv'
VALIDATING5 = homedir + '/data/last_trial/kendo/validate_08x08_5.csv'
VALIDATING6 = homedir + '/data/last_trial/kendo/validate_08x08_6.csv'
VALIDATING7 = homedir + '/data/last_trial/kendo/validate_08x08_7.csv'
VALIDATING8 = homedir + '/data/last_trial/kendo/validate_08x08_8.csv'
VALIDATING9 = homedir + '/data/last_trial/kendo/validate_08x08_9.csv'
VALIDATING10 = homedir + '/data/last_trial/kendo/validate_08x08_10.csv'
VALIDATING11 = homedir + '/data/last_trial/kendo/validate_08x08_11.csv'
VALIDATING12 = homedir + '/data/last_trial/kendo/validate_08x08_12.csv'
VALIDATING13 = homedir + '/data/last_trial/kendo/validate_08x08_13.csv'
VALIDATING14 = homedir + '/data/last_trial/kendo/validate_08x08_14.csv'
VALIDATING15 = homedir + '/data/last_trial/kendo/validate_08x08_15.csv'
VALIDATING16 = homedir + '/data/last_trial/kendo/validate_08x08_16.csv'
VALIDATING17 = homedir + '/data/last_trial/kendo/validate_08x08_17.csv'
VALIDATING18 = homedir + '/data/last_trial/kendo/validate_08x08_18.csv'
VALIDATING19 = homedir + '/data/last_trial/kendo/validate_08x08_19.csv'
VALIDATING20 = homedir + '/data/last_trial/kendo/validate_08x08_20.csv'
VALIDATING21 = homedir + '/data/last_trial/kendo/validate_08x08_21.csv'
VALIDATING22 = homedir + '/data/last_trial/kendo/validate_08x08_22.csv'
VALIDATING23 = homedir + '/data/last_trial/kendo/validate_08x08_23.csv'
VALIDATING24 = homedir + '/data/last_trial/kendo/validate_08x08_24.csv'
VALIDATING25 = homedir + '/data/last_trial/kendo/validate_08x08_25.csv'
VALIDATING26 = homedir + '/data/last_trial/kendo/validate_08x08_26.csv'
VALIDATING27 = homedir + '/data/last_trial/kendo/validate_08x08_27.csv'
VALIDATING28 = homedir + '/data/last_trial/kendo/validate_08x08_28.csv'
VALIDATING29 = homedir + '/data/last_trial/kendo/validate_08x08_29.csv'
VALIDATING30 = homedir + '/data/last_trial/kendo/validate_08x08_30.csv'
VALIDATING31 = homedir + '/data/last_trial/kendo/validate_08x08_31.csv'
VALIDATING32 = homedir + '/data/last_trial/kendo/validate_08x08_32.csv'
VALIDATING33 = homedir + '/data/last_trial/kendo/validate_08x08_33.csv'
VALIDATING34 = homedir + '/data/last_trial/kendo/validate_08x08_34.csv'
VALIDATING35 = homedir + '/data/last_trial/kendo/validate_08x08_35.csv'
VALIDATING36 = homedir + '/data/last_trial/kendo/validate_08x08_36.csv'


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
                if mode_0 <= 710:
                    training_data.write(line)
                elif 710 < mode_0 <= 1420:
                    validating_data.write(line)
                    validating_data0.write(line)
                elif 1420 < mode_0 <= 3000:
                    testing_data.write(line)

            elif mode == 1:
                mode_1 += 1
                if mode_1 <= 710:
                    training_data.write(line)
                elif 710 < mode_1 <= 1420:
                    validating_data.write(line)
                    validating_data1.write(line)
                elif 1420 < mode_1 <= 3000:
                    testing_data.write(line)

            elif mode == 2:
                mode_2 += 1
                if mode_2 <= 710:
                    training_data.write(line)
                elif 710 < mode_2 <= 1420:
                    validating_data.write(line)
                    validating_data2.write(line)
                elif 1420 < mode_2 <= 3000:
                    testing_data.write(line)

            elif mode == 3:
                mode_3 += 1
                if mode_3 <= 710:
                    training_data.write(line)
                elif 710 < mode_3 <= 1420:
                    validating_data.write(line)
                    # validating_data3.write(line)
                elif 1420 < mode_3 <= 3000:
                    testing_data.write(line)

            elif mode == 4:
                mode_4 += 1
                if mode_4 <= 710:
                    training_data.write(line)
                elif 710 < mode_4 <= 1420:
                    validating_data.write(line)
                    # validating_data3.write(line)
                elif 1420 < mode_4 <= 3000:
                    testing_data.write(line)

            elif mode == 5:
                mode_5 += 1
                if mode_5 <= 710:
                    training_data.write(line)
                elif 710 < mode_5 <= 1420:
                    validating_data.write(line)
                    # validating_data3.write(line)
                elif 1420 < mode_5 <= 3000:
                    testing_data.write(line)

            elif mode == 6:
                mode_6 += 1
                if mode_6 <= 710:
                    training_data.write(line)
                elif 710 < mode_6 <= 1420:
                    validating_data.write(line)
                    # validating_data3.write(line)
                elif 1420 < mode_6 <= 3000:
                    testing_data.write(line)

            elif mode == 7:
                mode_7 += 1
                if mode_7 <= 710:
                    training_data.write(line)
                elif 710 < mode_7 <= 1420:
                    validating_data.write(line)
                    # validating_data3.write(line)
                elif 1420 < mode_7 <= 3000:
                    testing_data.write(line)

            elif mode == 8:
                mode_8 += 1
                if mode_8 <= 710:
                    training_data.write(line)
                elif 710 < mode_8 <= 1420:
                    validating_data.write(line)
                    # validating_data3.write(line)
                elif 1420 < mode_8 <= 3000:
                    testing_data.write(line)

            elif mode == 9:
                mode_9 += 1
                if mode_9 <= 710:
                    training_data.write(line)
                elif 710 < mode_9 <= 1420:
                    validating_data.write(line)
                    # validating_data3.write(line)
                elif 1420 < mode_9 <= 3000:
                    testing_data.write(line)

            elif mode == 10:
                mode_10 += 1
                if mode_10 <= 710:
                    training_data.write(line)
                elif 710 < mode_10 <= 1420:
                    validating_data.write(line)
                    # validating_data3.write(line)
                elif 1420 < mode_10 <= 3000:
                    testing_data.write(line)

            elif mode == 11:
                mode_11 += 1
                if mode_11 <= 710:
                    training_data.write(line)
                elif 710 < mode_11 <= 1420:
                    validating_data.write(line)
                    # validating_data3.write(line)
                elif 1420 < mode_11 <= 3000:
                    testing_data.write(line)

            elif mode == 12:
                mode_12 += 1
                if mode_12 <= 710:
                    training_data.write(line)
                elif 710 < mode_12 <= 1420:
                    validating_data.write(line)
                    # validating_data3.write(line)
                elif 1420 < mode_12 <= 3000:
                    testing_data.write(line)

            elif mode == 13:
                mode_13 += 1
                if mode_13 <= 710:
                    training_data.write(line)
                elif 710 < mode_13 <= 1420:
                    validating_data.write(line)
                    # validating_data3.write(line)
                elif 1420 < mode_13 <= 3000:
                    testing_data.write(line)

            elif mode == 14:
                mode_14 += 1
                if mode_14 <= 710:
                    training_data.write(line)
                elif 710 < mode_14 <= 1420:
                    validating_data.write(line)
                    # validating_data3.write(line)
                elif 1420 < mode_14 <= 3000:
                    testing_data.write(line)

            elif mode == 15:
                mode_15 += 1
                if mode_15 <= 710:
                    training_data.write(line)
                elif 710 < mode_15 <= 1420:
                    validating_data.write(line)
                    # validating_data3.write(line)
                elif 1420 < mode_15 <= 3000:
                    testing_data.write(line)

            elif mode == 16:
                mode_16 += 1
                if mode_16 <= 710:
                    training_data.write(line)
                elif 710 < mode_16 <= 1420:
                    validating_data.write(line)
                    # validating_data3.write(line)
                elif 1420 < mode_16 <= 3000:
                    testing_data.write(line)

            elif mode == 17:
                mode_17 += 1
                if mode_17 <= 710:
                    training_data.write(line)
                elif 710 < mode_17 <= 1420:
                    validating_data.write(line)
                    # validating_data3.write(line)
                elif 1420 < mode_17 <= 3000:
                    testing_data.write(line)

            elif mode == 18:
                mode_18 += 1
                if mode_18 <= 710:
                    training_data.write(line)
                elif 710 < mode_18 <= 1420:
                    validating_data.write(line)
                    # validating_data3.write(line)
                elif 1420 < mode_18 <= 3000:
                    testing_data.write(line)

            elif mode == 19:
                mode_19 += 1
                if mode_19 <= 710:
                    training_data.write(line)
                elif 710 < mode_19 <= 1420:
                    validating_data.write(line)
                    # validating_data3.write(line)
                elif 1420 < mode_19 <= 3000:
                    testing_data.write(line)

            elif mode == 20:
                mode_20 += 1
                if mode_20 <= 710:
                    training_data.write(line)
                elif 710 < mode_20 <= 1420:
                    validating_data.write(line)
                    # validating_data3.write(line)
                elif 1420 < mode_20 <= 3000:
                    testing_data.write(line)

            elif mode == 21:
                mode_21 += 1
                if mode_21 <= 710:
                    training_data.write(line)
                elif 710 < mode_21 <= 1420:
                    validating_data.write(line)
                    # validating_data3.write(line)
                elif 1420 < mode_21 <= 3000:
                    testing_data.write(line)

            elif mode == 22:
                mode_22 += 1
                if mode_22 <= 710:
                    training_data.write(line)
                elif 710 < mode_22 <= 1420:
                    validating_data.write(line)
                    # validating_data3.write(line)
                elif 1420 < mode_22 <= 3000:
                    testing_data.write(line)

            elif mode == 23:
                mode_23 += 1
                if mode_23 <= 710:
                    training_data.write(line)
                elif 710 < mode_23 <= 1420:
                    validating_data.write(line)
                    # validating_data3.write(line)
                elif 1420 < mode_23 <= 3000:
                    testing_data.write(line)

            elif mode == 24:
                mode_24 += 1
                if mode_24 <= 710:
                    training_data.write(line)
                elif 710 < mode_24 <= 1420:
                    validating_data.write(line)
                    # validating_data3.write(line)
                elif 1420 < mode_24 <= 3000:
                    testing_data.write(line)

            elif mode == 25:
                mode_25 += 1
                if mode_25 <= 710:
                    training_data.write(line)
                elif 710 < mode_25 <= 1420:
                    validating_data.write(line)
                    # validating_data3.write(line)
                elif 1420 < mode_25 <= 3000:
                    testing_data.write(line)

            elif mode == 26:
                mode_26 += 1
                if mode_26 <= 710:
                    training_data.write(line)
                elif 710 < mode_26 <= 1420:
                    validating_data.write(line)
                    # validating_data3.write(line)
                elif 1420 < mode_26 <= 3000:
                    testing_data.write(line)

            elif mode == 27:
                mode_27 += 1
                if mode_27 <= 710:
                    training_data.write(line)
                elif 710 < mode_27 <= 1420:
                    validating_data.write(line)
                    # validating_data3.write(line)
                elif 1420 < mode_27 <= 3000:
                    testing_data.write(line)

            elif mode == 28:
                mode_28 += 1
                if mode_28 <= 710:
                    training_data.write(line)
                elif 710 < mode_28 <= 1420:
                    validating_data.write(line)
                    # validating_data3.write(line)
                elif 1420 < mode_28 <= 3000:
                    testing_data.write(line)

            elif mode == 29:
                mode_29 += 1
                if mode_29 <= 710:
                    training_data.write(line)
                elif 710 < mode_29 <= 1420:
                    validating_data.write(line)
                    # validating_data3.write(line)
                elif 1420 < mode_29 <= 3000:
                    testing_data.write(line)

            elif mode == 30:
                mode_30 += 1
                if mode_30 <= 710:
                    training_data.write(line)
                elif 710 < mode_30 <= 1420:
                    validating_data.write(line)
                    validating_data30.write(line)
                elif 1420 < mode_30 <= 3000:
                    testing_data.write(line)

            elif mode == 31:
                mode_31 += 1
                if mode_31 <= 710:
                    training_data.write(line)
                elif 710 < mode_31 <= 1420:
                    validating_data.write(line)
                    validating_data31.write(line)
                elif 1420 < mode_31 <= 3000:
                    testing_data.write(line)

            elif mode == 32:
                mode_32 += 1
                if mode_32 <= 710:
                    training_data.write(line)
                elif 710 < mode_32 <= 1420:
                    validating_data.write(line)
                    validating_data32.write(line)
                elif 1420 < mode_32 <= 3000:
                    testing_data.write(line)

            elif mode == 33:
                mode_33 += 1
                if mode_33 <= 710:
                    training_data.write(line)
                elif 710 < mode_33 <= 1420:
                    validating_data.write(line)
                    validating_data33.write(line)
                elif 1420 < mode_33 <= 3000:
                    testing_data.write(line)

            elif mode == 34:
                mode_34 += 1
                if mode_34 <= 710:
                    training_data.write(line)
                elif 710 < mode_34 <= 1420:
                    validating_data.write(line)
                    validating_data34.write(line)
                elif 1420 < mode_34 <= 3000:
                    testing_data.write(line)

            elif mode == 35:
                mode_35 += 1
                if mode_35 <= 710:
                    training_data.write(line)
                elif 710 < mode_35 <= 1420:
                    validating_data.write(line)
                    validating_data35.write(line)
                elif 1420 < mode_35 <= 3000:
                    testing_data.write(line)

            elif mode == 36:
                mode_36 += 1
                if mode_36 <= 710:
                    training_data.write(line)
                elif 710 < mode_36 <= 1420:
                    validating_data.write(line)
                    validating_data36.write(line)
                elif 1420 < mode_36 <= 3000:
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
