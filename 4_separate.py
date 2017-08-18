# ------------------------------------------------------------------------------
# Author: Pharrell_WANG
#   Date: 2017/6/28
# ------------------------------------------------------------------------------
# from csv_mode_counter import csv_mode_preprocessing
TRAINING_DATA_PERCENT = 0.6
TESTING_DATA_PERCENT = 0.2
VALIDATING_DATA_PERCENT = 0.2
assert (
    TRAINING_DATA_PERCENT + TESTING_DATA_PERCENT + VALIDATING_DATA_PERCENT == 1)

# ===========for size 32x32:
# total 1180,
# ---> divided into
# train:(0,708];
# test:(708, 944];
# validation: (944, 1180]
import os

homedir = os.environ['HOME']
ORIG = homedir + '/data/step2_output/size_32_files.csv'
TRAINING = homedir + '/data/step3_output/32x32/data_for_training/train_32x32.csv'
TESTING = homedir + '/data/step3_output/32x32/data_for_testing/test_32x32.csv'
VALIDATING = homedir + '/data/step3_output/32x32/data_for_validating/validate_32x32.csv'

VALIDATING0 = homedir + '/data/step3_output/32x32/data_for_validating/validate_32x32_0.csv'
VALIDATING1 = homedir + '/data/step3_output/32x32/data_for_validating/validate_32x32_1.csv'
VALIDATING2 = homedir + '/data/step3_output/32x32/data_for_validating/validate_32x32_2.csv'
VALIDATING3 = homedir + '/data/step3_output/32x32/data_for_validating/validate_32x32_3.csv'
VALIDATING4 = homedir + '/data/step3_output/32x32/data_for_validating/validate_32x32_4.csv'
VALIDATING5 = homedir + '/data/step3_output/32x32/data_for_validating/validate_32x32_5.csv'
VALIDATING6 = homedir + '/data/step3_output/32x32/data_for_validating/validate_32x32_6.csv'
VALIDATING7 = homedir + '/data/step3_output/32x32/data_for_validating/validate_32x32_7.csv'
VALIDATING8 = homedir + '/data/step3_output/32x32/data_for_validating/validate_32x32_8.csv'
VALIDATING9 = homedir + '/data/step3_output/32x32/data_for_validating/validate_32x32_9.csv'
VALIDATING10 = homedir + '/data/step3_output/32x32/data_for_validating/validate_32x32_10.csv'
VALIDATING11 = homedir + '/data/step3_output/32x32/data_for_validating/validate_32x32_11.csv'
VALIDATING12 = homedir + '/data/step3_output/32x32/data_for_validating/validate_32x32_12.csv'
VALIDATING13 = homedir + '/data/step3_output/32x32/data_for_validating/validate_32x32_13.csv'
VALIDATING14 = homedir + '/data/step3_output/32x32/data_for_validating/validate_32x32_14.csv'
VALIDATING15 = homedir + '/data/step3_output/32x32/data_for_validating/validate_32x32_15.csv'
VALIDATING16 = homedir + '/data/step3_output/32x32/data_for_validating/validate_32x32_16.csv'
VALIDATING17 = homedir + '/data/step3_output/32x32/data_for_validating/validate_32x32_17.csv'
VALIDATING18 = homedir + '/data/step3_output/32x32/data_for_validating/validate_32x32_18.csv'
VALIDATING19 = homedir + '/data/step3_output/32x32/data_for_validating/validate_32x32_19.csv'
VALIDATING20 = homedir + '/data/step3_output/32x32/data_for_validating/validate_32x32_20.csv'
VALIDATING21 = homedir + '/data/step3_output/32x32/data_for_validating/validate_32x32_21.csv'
VALIDATING22 = homedir + '/data/step3_output/32x32/data_for_validating/validate_32x32_22.csv'
VALIDATING23 = homedir + '/data/step3_output/32x32/data_for_validating/validate_32x32_23.csv'
VALIDATING24 = homedir + '/data/step3_output/32x32/data_for_validating/validate_32x32_24.csv'
VALIDATING25 = homedir + '/data/step3_output/32x32/data_for_validating/validate_32x32_25.csv'
VALIDATING26 = homedir + '/data/step3_output/32x32/data_for_validating/validate_32x32_26.csv'
VALIDATING27 = homedir + '/data/step3_output/32x32/data_for_validating/validate_32x32_27.csv'
VALIDATING28 = homedir + '/data/step3_output/32x32/data_for_validating/validate_32x32_28.csv'
VALIDATING29 = homedir + '/data/step3_output/32x32/data_for_validating/validate_32x32_29.csv'
VALIDATING30 = homedir + '/data/step3_output/32x32/data_for_validating/validate_32x32_30.csv'
VALIDATING31 = homedir + '/data/step3_output/32x32/data_for_validating/validate_32x32_31.csv'
VALIDATING32 = homedir + '/data/step3_output/32x32/data_for_validating/validate_32x32_32.csv'
VALIDATING33 = homedir + '/data/step3_output/32x32/data_for_validating/validate_32x32_33.csv'
VALIDATING34 = homedir + '/data/step3_output/32x32/data_for_validating/validate_32x32_34.csv'
VALIDATING35 = homedir + '/data/step3_output/32x32/data_for_validating/validate_32x32_35.csv'
VALIDATING36 = homedir + '/data/step3_output/32x32/data_for_validating/validate_32x32_36.csv'


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
                if mode_0 <= 708:
                    training_data.write(line)
                elif 708 < mode_0 <= 944:
                    validating_data.write(line)
                    validating_data0.write(line)
                elif 944 < mode_0 <= 1180:
                    testing_data.write(line)

            elif mode == 1:
                mode_1 += 1
                if mode_1 <= 708:
                    training_data.write(line)
                elif 708 < mode_1 <= 944:
                    validating_data.write(line)
                    validating_data1.write(line)
                elif 944 < mode_1 <= 1180:
                    testing_data.write(line)

            elif mode == 2:
                mode_2 += 1
                if mode_2 <= 708:
                    training_data.write(line)
                elif 708 < mode_2 <= 944:
                    validating_data.write(line)
                    validating_data2.write(line)
                elif 944 < mode_2 <= 1180:
                    testing_data.write(line)

            elif mode == 3:
                mode_3 += 1
                if mode_3 <= 708:
                    training_data.write(line)
                elif 708 < mode_3 <= 944:
                    validating_data.write(line)
                    # validating_data3.write(line)
                elif 944 < mode_3 <= 1180:
                    testing_data.write(line)

            elif mode == 4:
                mode_4 += 1
                if mode_4 <= 708:
                    training_data.write(line)
                elif 708 < mode_4 <= 944:
                    validating_data.write(line)
                    # validating_data3.write(line)
                elif 944 < mode_4 <= 1180:
                    testing_data.write(line)

            elif mode == 5:
                mode_5 += 1
                if mode_5 <= 708:
                    training_data.write(line)
                elif 708 < mode_5 <= 944:
                    validating_data.write(line)
                    # validating_data3.write(line)
                elif 944 < mode_5 <= 1180:
                    testing_data.write(line)

            elif mode == 6:
                mode_6 += 1
                if mode_6 <= 708:
                    training_data.write(line)
                elif 708 < mode_6 <= 944:
                    validating_data.write(line)
                    # validating_data3.write(line)
                elif 944 < mode_6 <= 1180:
                    testing_data.write(line)

            elif mode == 7:
                mode_7 += 1
                if mode_7 <= 708:
                    training_data.write(line)
                elif 708 < mode_7 <= 944:
                    validating_data.write(line)
                    # validating_data3.write(line)
                elif 944 < mode_7 <= 1180:
                    testing_data.write(line)

            elif mode == 8:
                mode_8 += 1
                if mode_8 <= 708:
                    training_data.write(line)
                elif 708 < mode_8 <= 944:
                    validating_data.write(line)
                    # validating_data3.write(line)
                elif 944 < mode_8 <= 1180:
                    testing_data.write(line)

            elif mode == 9:
                mode_9 += 1
                if mode_9 <= 708:
                    training_data.write(line)
                elif 708 < mode_9 <= 944:
                    validating_data.write(line)
                    # validating_data3.write(line)
                elif 944 < mode_9 <= 1180:
                    testing_data.write(line)

            elif mode == 10:
                mode_10 += 1
                if mode_10 <= 708:
                    training_data.write(line)
                elif 708 < mode_10 <= 944:
                    validating_data.write(line)
                    # validating_data3.write(line)
                elif 944 < mode_10 <= 1180:
                    testing_data.write(line)

            elif mode == 11:
                mode_11 += 1
                if mode_11 <= 708:
                    training_data.write(line)
                elif 708 < mode_11 <= 944:
                    validating_data.write(line)
                    # validating_data3.write(line)
                elif 944 < mode_11 <= 1180:
                    testing_data.write(line)

            elif mode == 12:
                mode_12 += 1
                if mode_12 <= 708:
                    training_data.write(line)
                elif 708 < mode_12 <= 944:
                    validating_data.write(line)
                    # validating_data3.write(line)
                elif 944 < mode_12 <= 1180:
                    testing_data.write(line)

            elif mode == 13:
                mode_13 += 1
                if mode_13 <= 708:
                    training_data.write(line)
                elif 708 < mode_13 <= 944:
                    validating_data.write(line)
                    # validating_data3.write(line)
                elif 944 < mode_13 <= 1180:
                    testing_data.write(line)

            elif mode == 14:
                mode_14 += 1
                if mode_14 <= 708:
                    training_data.write(line)
                elif 708 < mode_14 <= 944:
                    validating_data.write(line)
                    # validating_data3.write(line)
                elif 944 < mode_14 <= 1180:
                    testing_data.write(line)

            elif mode == 15:
                mode_15 += 1
                if mode_15 <= 708:
                    training_data.write(line)
                elif 708 < mode_15 <= 944:
                    validating_data.write(line)
                    # validating_data3.write(line)
                elif 944 < mode_15 <= 1180:
                    testing_data.write(line)

            elif mode == 16:
                mode_16 += 1
                if mode_16 <= 708:
                    training_data.write(line)
                elif 708 < mode_16 <= 944:
                    validating_data.write(line)
                    # validating_data3.write(line)
                elif 944 < mode_16 <= 1180:
                    testing_data.write(line)

            elif mode == 17:
                mode_17 += 1
                if mode_17 <= 708:
                    training_data.write(line)
                elif 708 < mode_17 <= 944:
                    validating_data.write(line)
                    # validating_data3.write(line)
                elif 944 < mode_17 <= 1180:
                    testing_data.write(line)

            elif mode == 18:
                mode_18 += 1
                if mode_18 <= 708:
                    training_data.write(line)
                elif 708 < mode_18 <= 944:
                    validating_data.write(line)
                    # validating_data3.write(line)
                elif 944 < mode_18 <= 1180:
                    testing_data.write(line)

            elif mode == 19:
                mode_19 += 1
                if mode_19 <= 708:
                    training_data.write(line)
                elif 708 < mode_19 <= 944:
                    validating_data.write(line)
                    # validating_data3.write(line)
                elif 944 < mode_19 <= 1180:
                    testing_data.write(line)

            elif mode == 20:
                mode_20 += 1
                if mode_20 <= 708:
                    training_data.write(line)
                elif 708 < mode_20 <= 944:
                    validating_data.write(line)
                    # validating_data3.write(line)
                elif 944 < mode_20 <= 1180:
                    testing_data.write(line)

            elif mode == 21:
                mode_21 += 1
                if mode_21 <= 708:
                    training_data.write(line)
                elif 708 < mode_21 <= 944:
                    validating_data.write(line)
                    # validating_data3.write(line)
                elif 944 < mode_21 <= 1180:
                    testing_data.write(line)

            elif mode == 22:
                mode_22 += 1
                if mode_22 <= 708:
                    training_data.write(line)
                elif 708 < mode_22 <= 944:
                    validating_data.write(line)
                    # validating_data3.write(line)
                elif 944 < mode_22 <= 1180:
                    testing_data.write(line)

            elif mode == 23:
                mode_23 += 1
                if mode_23 <= 708:
                    training_data.write(line)
                elif 708 < mode_23 <= 944:
                    validating_data.write(line)
                    # validating_data3.write(line)
                elif 944 < mode_23 <= 1180:
                    testing_data.write(line)

            elif mode == 24:
                mode_24 += 1
                if mode_24 <= 708:
                    training_data.write(line)
                elif 708 < mode_24 <= 944:
                    validating_data.write(line)
                    # validating_data3.write(line)
                elif 944 < mode_24 <= 1180:
                    testing_data.write(line)

            elif mode == 25:
                mode_25 += 1
                if mode_25 <= 708:
                    training_data.write(line)
                elif 708 < mode_25 <= 944:
                    validating_data.write(line)
                    # validating_data3.write(line)
                elif 944 < mode_25 <= 1180:
                    testing_data.write(line)

            elif mode == 26:
                mode_26 += 1
                if mode_26 <= 708:
                    training_data.write(line)
                elif 708 < mode_26 <= 944:
                    validating_data.write(line)
                    # validating_data3.write(line)
                elif 944 < mode_26 <= 1180:
                    testing_data.write(line)

            elif mode == 27:
                mode_27 += 1
                if mode_27 <= 708:
                    training_data.write(line)
                elif 708 < mode_27 <= 944:
                    validating_data.write(line)
                    # validating_data3.write(line)
                elif 944 < mode_27 <= 1180:
                    testing_data.write(line)

            elif mode == 28:
                mode_28 += 1
                if mode_28 <= 708:
                    training_data.write(line)
                elif 708 < mode_20 <= 944:
                    validating_data.write(line)
                    # validating_data3.write(line)
                elif 944 < mode_20 <= 1180:
                    testing_data.write(line)

            elif mode == 29:
                mode_29 += 1
                if mode_29 <= 708:
                    training_data.write(line)
                elif 708 < mode_29 <= 944:
                    validating_data.write(line)
                    # validating_data3.write(line)
                elif 944 < mode_29 <= 1180:
                    testing_data.write(line)

            elif mode == 30:
                mode_30 += 1
                if mode_30 <= 708:
                    training_data.write(line)
                elif 708 < mode_30 <= 944:
                    validating_data.write(line)
                    validating_data30.write(line)
                elif 944 < mode_30 <= 1180:
                    testing_data.write(line)

            elif mode == 31:
                mode_31 += 1
                if mode_31 <= 708:
                    training_data.write(line)
                elif 708 < mode_31 <= 944:
                    validating_data.write(line)
                    validating_data31.write(line)
                elif 944 < mode_31 <= 1180:
                    testing_data.write(line)

            elif mode == 32:
                mode_32 += 1
                if mode_32 <= 708:
                    training_data.write(line)
                elif 708 < mode_32 <= 944:
                    validating_data.write(line)
                    validating_data32.write(line)
                elif 944 < mode_32 <= 1180:
                    testing_data.write(line)

            elif mode == 33:
                mode_33 += 1
                if mode_33 <= 708:
                    training_data.write(line)
                elif 708 < mode_33 <= 944:
                    validating_data.write(line)
                    validating_data33.write(line)
                elif 944 < mode_33 <= 1180:
                    testing_data.write(line)

            elif mode == 34:
                mode_34 += 1
                if mode_34 <= 708:
                    training_data.write(line)
                elif 708 < mode_34 <= 944:
                    validating_data.write(line)
                    validating_data34.write(line)
                elif 944 < mode_34 <= 1180:
                    testing_data.write(line)

            elif mode == 35:
                mode_35 += 1
                if mode_35 <= 708:
                    training_data.write(line)
                elif 708 < mode_35 <= 944:
                    validating_data.write(line)
                    validating_data35.write(line)
                elif 944 < mode_35 <= 1180:
                    testing_data.write(line)

            elif mode == 36:
                mode_36 += 1
                if mode_36 <= 708:
                    training_data.write(line)
                elif 708 < mode_36 <= 944:
                    validating_data.write(line)
                    validating_data36.write(line)
                elif 944 < mode_36 <= 1180:
                    testing_data.write(line)


# x_ordered_dict = csv_mode_preprocessing(OUTPUT_FILE=ORIG)
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
