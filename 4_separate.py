# ------------------------------------------------------------------------------
# Author: Pharrell_WANG
#   Date: 2017/6/28
# ------------------------------------------------------------------------------
# from csv_mode_counter import csv_mode_preprocessing

NUM_MODES = 480

ORIG = '/Users/Pharrell_WANG/PycharmProjects/fdc-tf-data-preprocessing/data_after_step2_remove/comma_removed_size_16.csv'

TRAINING = '/Users/Pharrell_WANG/PycharmProjects/fdc-tf-data-preprocessing/train_data/training_data_16x16.csv'
TESTING = '/Users/Pharrell_WANG/PycharmProjects/fdc-tf-data-preprocessing/test_data/testing_data_16x16.csv'
VALIDATING = '/Users/Pharrell_WANG/PycharmProjects/fdc-tf-data-preprocessing/validate_data/validating_data_16x16.csv'

VALIDATING0 = '/Users/Pharrell_WANG/PycharmProjects/fdc-tf-data-preprocessing/validate_data/validating_16x16_0.csv'
VALIDATING1 = '/Users/Pharrell_WANG/PycharmProjects/fdc-tf-data-preprocessing/validate_data/validating_16x16_1.csv'
VALIDATING2 = '/Users/Pharrell_WANG/PycharmProjects/fdc-tf-data-preprocessing/validate_data/validating_16x16_2.csv'
VALIDATING3 = '/Users/Pharrell_WANG/PycharmProjects/fdc-tf-data-preprocessing/validate_data/validating_16x16_3.csv'
VALIDATING4 = '/Users/Pharrell_WANG/PycharmProjects/fdc-tf-data-preprocessing/validate_data/validating_16x16_4.csv'
VALIDATING5 = '/Users/Pharrell_WANG/PycharmProjects/fdc-tf-data-preprocessing/validate_data/validating_16x16_5.csv'
VALIDATING6 = '/Users/Pharrell_WANG/PycharmProjects/fdc-tf-data-preprocessing/validate_data/validating_16x16_6.csv'
VALIDATING7 = '/Users/Pharrell_WANG/PycharmProjects/fdc-tf-data-preprocessing/validate_data/validating_16x16_7.csv'
VALIDATING8 = '/Users/Pharrell_WANG/PycharmProjects/fdc-tf-data-preprocessing/validate_data/validating_16x16_8.csv'
VALIDATING9 = '/Users/Pharrell_WANG/PycharmProjects/fdc-tf-data-preprocessing/validate_data/validating_16x16_9.csv'
VALIDATING10 = '/Users/Pharrell_WANG/PycharmProjects/fdc-tf-data-preprocessing/validate_data/validating_16x16_10.csv'
VALIDATING11 = '/Users/Pharrell_WANG/PycharmProjects/fdc-tf-data-preprocessing/validate_data/validating_16x16_11.csv'
VALIDATING12 = '/Users/Pharrell_WANG/PycharmProjects/fdc-tf-data-preprocessing/validate_data/validating_16x16_12.csv'
VALIDATING13 = '/Users/Pharrell_WANG/PycharmProjects/fdc-tf-data-preprocessing/validate_data/validating_16x16_13.csv'
VALIDATING14 = '/Users/Pharrell_WANG/PycharmProjects/fdc-tf-data-preprocessing/validate_data/validating_16x16_14.csv'
VALIDATING15 = '/Users/Pharrell_WANG/PycharmProjects/fdc-tf-data-preprocessing/validate_data/validating_16x16_15.csv'
VALIDATING16 = '/Users/Pharrell_WANG/PycharmProjects/fdc-tf-data-preprocessing/validate_data/validating_16x16_16.csv'
VALIDATING17 = '/Users/Pharrell_WANG/PycharmProjects/fdc-tf-data-preprocessing/validate_data/validating_16x16_17.csv'
VALIDATING18 = '/Users/Pharrell_WANG/PycharmProjects/fdc-tf-data-preprocessing/validate_data/validating_16x16_18.csv'
VALIDATING19 = '/Users/Pharrell_WANG/PycharmProjects/fdc-tf-data-preprocessing/validate_data/validating_16x16_19.csv'
VALIDATING20 = '/Users/Pharrell_WANG/PycharmProjects/fdc-tf-data-preprocessing/validate_data/validating_16x16_20.csv'
VALIDATING21 = '/Users/Pharrell_WANG/PycharmProjects/fdc-tf-data-preprocessing/validate_data/validating_16x16_21.csv'
VALIDATING22 = '/Users/Pharrell_WANG/PycharmProjects/fdc-tf-data-preprocessing/validate_data/validating_16x16_22.csv'
VALIDATING23 = '/Users/Pharrell_WANG/PycharmProjects/fdc-tf-data-preprocessing/validate_data/validating_16x16_23.csv'
VALIDATING24 = '/Users/Pharrell_WANG/PycharmProjects/fdc-tf-data-preprocessing/validate_data/validating_16x16_24.csv'
VALIDATING25 = '/Users/Pharrell_WANG/PycharmProjects/fdc-tf-data-preprocessing/validate_data/validating_16x16_25.csv'
VALIDATING26 = '/Users/Pharrell_WANG/PycharmProjects/fdc-tf-data-preprocessing/validate_data/validating_16x16_26.csv'
VALIDATING27 = '/Users/Pharrell_WANG/PycharmProjects/fdc-tf-data-preprocessing/validate_data/validating_16x16_27.csv'
VALIDATING28 = '/Users/Pharrell_WANG/PycharmProjects/fdc-tf-data-preprocessing/validate_data/validating_16x16_28.csv'
VALIDATING29 = '/Users/Pharrell_WANG/PycharmProjects/fdc-tf-data-preprocessing/validate_data/validating_16x16_29.csv'
VALIDATING30 = '/Users/Pharrell_WANG/PycharmProjects/fdc-tf-data-preprocessing/validate_data/validating_16x16_30.csv'
VALIDATING31 = '/Users/Pharrell_WANG/PycharmProjects/fdc-tf-data-preprocessing/validate_data/validating_16x16_31.csv'
VALIDATING32 = '/Users/Pharrell_WANG/PycharmProjects/fdc-tf-data-preprocessing/validate_data/validating_16x16_32.csv'
VALIDATING33 = '/Users/Pharrell_WANG/PycharmProjects/fdc-tf-data-preprocessing/validate_data/validating_16x16_33.csv'
VALIDATING34 = '/Users/Pharrell_WANG/PycharmProjects/fdc-tf-data-preprocessing/validate_data/validating_16x16_34.csv'
VALIDATING35 = '/Users/Pharrell_WANG/PycharmProjects/fdc-tf-data-preprocessing/validate_data/validating_16x16_35.csv'
VALIDATING36 = '/Users/Pharrell_WANG/PycharmProjects/fdc-tf-data-preprocessing/validate_data/validating_16x16_36.csv'


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
                if mode_0 <= 3360:
                    training_data.write(line)
                elif 3360 < mode_0 <= 4480:
                    validating_data.write(line)
                    validating_data0.write(line)
                elif 4480 < mode_0 <= 5600:
                    testing_data.write(line)

            elif mode == 1:
                mode_1 += 1
                if mode_1 <= 3360:
                    training_data.write(line)
                elif 3360 < mode_1 <= 4480:
                    validating_data.write(line)
                    validating_data1.write(line)
                elif 4480 < mode_1 <= 5600:
                    testing_data.write(line)

            elif mode == 2:
                mode_2 += 1
                if mode_2 <= 3360:
                    training_data.write(line)
                elif 3360 < mode_2 <= 4480:
                    validating_data.write(line)
                    validating_data2.write(line)
                elif 4480 < mode_2 <= 5600:
                    testing_data.write(line)

            elif mode == 3:
                mode_3 += 1
                if mode_3 <= 3360:
                    training_data.write(line)
                elif 3360 < mode_3 <= 4480:
                    validating_data.write(line)
                    # validating_data3.write(line)
                elif 4480 < mode_3 <= 5600:
                    testing_data.write(line)

            elif mode == 4:
                mode_4 += 1
                if mode_4 <= 3360:
                    training_data.write(line)
                elif 3360 < mode_4 <= 4480:
                    validating_data.write(line)
                    # validating_data3.write(line)
                elif 4480 < mode_4 <= 5600:
                    testing_data.write(line)

            elif mode == 5:
                mode_5 += 1
                if mode_5 <= 3360:
                    training_data.write(line)
                elif 3360 < mode_5 <= 4480:
                    validating_data.write(line)
                    # validating_data3.write(line)
                elif 4480 < mode_5 <= 5600:
                    testing_data.write(line)

            elif mode == 6:
                mode_6 += 1
                if mode_6 <= 3360:
                    training_data.write(line)
                elif 3360 < mode_6 <= 4480:
                    validating_data.write(line)
                    # validating_data3.write(line)
                elif 4480 < mode_6 <= 5600:
                    testing_data.write(line)

            elif mode == 7:
                mode_7 += 1
                if mode_7 <= 3360:
                    training_data.write(line)
                elif 3360 < mode_7 <= 4480:
                    validating_data.write(line)
                    # validating_data3.write(line)
                elif 4480 < mode_7 <= 5600:
                    testing_data.write(line)

            elif mode == 8:
                mode_8 += 1
                if mode_8 <= 3360:
                    training_data.write(line)
                elif 3360 < mode_8 <= 4480:
                    validating_data.write(line)
                    # validating_data3.write(line)
                elif 4480 < mode_8 <= 5600:
                    testing_data.write(line)

            elif mode == 9:
                mode_9 += 1
                if mode_9 <= 3360:
                    training_data.write(line)
                elif 3360 < mode_9 <= 4480:
                    validating_data.write(line)
                    # validating_data3.write(line)
                elif 4480 < mode_9 <= 5600:
                    testing_data.write(line)

            elif mode == 10:
                mode_10 += 1
                if mode_10 <= 3360:
                    training_data.write(line)
                elif 3360 < mode_10 <= 4480:
                    validating_data.write(line)
                    # validating_data3.write(line)
                elif 4480 < mode_10 <= 5600:
                    testing_data.write(line)

            elif mode == 11:
                mode_11 += 1
                if mode_11 <= 3360:
                    training_data.write(line)
                elif 3360 < mode_11 <= 4480:
                    validating_data.write(line)
                    # validating_data3.write(line)
                elif 4480 < mode_11 <= 5600:
                    testing_data.write(line)

            elif mode == 12:
                mode_12 += 1
                if mode_12 <= 3360:
                    training_data.write(line)
                elif 3360 < mode_12 <= 4480:
                    validating_data.write(line)
                    # validating_data3.write(line)
                elif 4480 < mode_12 <= 5600:
                    testing_data.write(line)

            elif mode == 13:
                mode_13 += 1
                if mode_13 <= 3360:
                    training_data.write(line)
                elif 3360 < mode_13 <= 4480:
                    validating_data.write(line)
                    # validating_data3.write(line)
                elif 4480 < mode_13 <= 5600:
                    testing_data.write(line)

            elif mode == 14:
                mode_14 += 1
                if mode_14 <= 3360:
                    training_data.write(line)
                elif 3360 < mode_14 <= 4480:
                    validating_data.write(line)
                    # validating_data3.write(line)
                elif 4480 < mode_14 <= 5600:
                    testing_data.write(line)

            elif mode == 15:
                mode_15 += 1
                if mode_15 <= 3360:
                    training_data.write(line)
                elif 3360 < mode_15 <= 4480:
                    validating_data.write(line)
                    # validating_data3.write(line)
                elif 4480 < mode_15 <= 5600:
                    testing_data.write(line)

            elif mode == 16:
                mode_16 += 1
                if mode_16 <= 3360:
                    training_data.write(line)
                elif 3360 < mode_16 <= 4480:
                    validating_data.write(line)
                    # validating_data3.write(line)
                elif 4480 < mode_16 <= 5600:
                    testing_data.write(line)

            elif mode == 17:
                mode_17 += 1
                if mode_17 <= 3360:
                    training_data.write(line)
                elif 3360 < mode_17 <= 4480:
                    validating_data.write(line)
                    # validating_data3.write(line)
                elif 4480 < mode_17 <= 5600:
                    testing_data.write(line)

            elif mode == 18:
                mode_18 += 1
                if mode_18 <= 3360:
                    training_data.write(line)
                elif 3360 < mode_18 <= 4480:
                    validating_data.write(line)
                    # validating_data3.write(line)
                elif 4480 < mode_18 <= 5600:
                    testing_data.write(line)

            elif mode == 19:
                mode_19 += 1
                if mode_19 <= 3360:
                    training_data.write(line)
                elif 3360 < mode_19 <= 4480:
                    validating_data.write(line)
                    # validating_data3.write(line)
                elif 4480 < mode_19 <= 5600:
                    testing_data.write(line)

            elif mode == 20:
                mode_20 += 1
                if mode_20 <= 3360:
                    training_data.write(line)
                elif 3360 < mode_20 <= 4480:
                    validating_data.write(line)
                    # validating_data3.write(line)
                elif 4480 < mode_20 <= 5600:
                    testing_data.write(line)

            elif mode == 21:
                mode_21 += 1
                if mode_21 <= 3360:
                    training_data.write(line)
                elif 3360 < mode_21 <= 4480:
                    validating_data.write(line)
                    # validating_data3.write(line)
                elif 4480 < mode_21 <= 5600:
                    testing_data.write(line)

            elif mode == 22:
                mode_22 += 1
                if mode_22 <= 3360:
                    training_data.write(line)
                elif 3360 < mode_22 <= 4480:
                    validating_data.write(line)
                    # validating_data3.write(line)
                elif 4480 < mode_22 <= 5600:
                    testing_data.write(line)

            elif mode == 23:
                mode_23 += 1
                if mode_23 <= 3360:
                    training_data.write(line)
                elif 3360 < mode_23 <= 4480:
                    validating_data.write(line)
                    # validating_data3.write(line)
                elif 4480 < mode_23 <= 5600:
                    testing_data.write(line)

            elif mode == 24:
                mode_24 += 1
                if mode_24 <= 3360:
                    training_data.write(line)
                elif 3360 < mode_24 <= 4480:
                    validating_data.write(line)
                    # validating_data3.write(line)
                elif 4480 < mode_24 <= 5600:
                    testing_data.write(line)

            elif mode == 25:
                mode_25 += 1
                if mode_25 <= 3360:
                    training_data.write(line)
                elif 3360 < mode_25 <= 4480:
                    validating_data.write(line)
                    # validating_data3.write(line)
                elif 4480 < mode_25 <= 5600:
                    testing_data.write(line)

            elif mode == 26:
                mode_26 += 1
                if mode_26 <= 3360:
                    training_data.write(line)
                elif 3360 < mode_26 <= 4480:
                    validating_data.write(line)
                    # validating_data3.write(line)
                elif 4480 < mode_26 <= 5600:
                    testing_data.write(line)

            elif mode == 27:
                mode_27 += 1
                if mode_27 <= 3360:
                    training_data.write(line)
                elif 3360 < mode_27 <= 4480:
                    validating_data.write(line)
                    # validating_data3.write(line)
                elif 4480 < mode_27 <= 5600:
                    testing_data.write(line)

            elif mode == 28:
                mode_28 += 1
                if mode_28 <= 3360:
                    training_data.write(line)
                elif 3360 < mode_20 <= 4480:
                    validating_data.write(line)
                    # validating_data3.write(line)
                elif 4480 < mode_20 <= 5600:
                    testing_data.write(line)

            elif mode == 29:
                mode_29 += 1
                if mode_29 <= 3360:
                    training_data.write(line)
                elif 3360 < mode_29 <= 4480:
                    validating_data.write(line)
                    # validating_data3.write(line)
                elif 4480 < mode_29 <= 5600:
                    testing_data.write(line)

            elif mode == 30:
                mode_30 += 1
                if mode_30 <= 3360:
                    training_data.write(line)
                elif 3360 < mode_30 <= 4480:
                    validating_data.write(line)
                    validating_data30.write(line)
                elif 4480 < mode_30 <= 5600:
                    testing_data.write(line)

            elif mode == 31:
                mode_31 += 1
                if mode_31 <= 3360:
                    training_data.write(line)
                elif 3360 < mode_31 <= 4480:
                    validating_data.write(line)
                    validating_data31.write(line)
                elif 4480 < mode_31 <= 5600:
                    testing_data.write(line)

            elif mode == 32:
                mode_32 += 1
                if mode_32 <= 3360:
                    training_data.write(line)
                elif 3360 < mode_32 <= 4480:
                    validating_data.write(line)
                    validating_data32.write(line)
                elif 4480 < mode_32 <= 5600:
                    testing_data.write(line)

            elif mode == 33:
                mode_33 += 1
                if mode_33 <= 3360:
                    training_data.write(line)
                elif 3360 < mode_33 <= 4480:
                    validating_data.write(line)
                    validating_data33.write(line)
                elif 4480 < mode_33 <= 5600:
                    testing_data.write(line)

            elif mode == 34:
                mode_34 += 1
                if mode_34 <= 3360:
                    training_data.write(line)
                elif 3360 < mode_34 <= 4480:
                    validating_data.write(line)
                    validating_data34.write(line)
                elif 4480 < mode_34 <= 5600:
                    testing_data.write(line)

            elif mode == 35:
                mode_35 += 1
                if mode_35 <= 3360:
                    training_data.write(line)
                elif 3360 < mode_35 <= 4480:
                    validating_data.write(line)
                    validating_data35.write(line)
                elif 4480 < mode_35 <= 5600:
                    testing_data.write(line)

            elif mode == 36:
                mode_36 += 1
                if mode_36 <= 3360:
                    training_data.write(line)
                elif 3360 < mode_36 <= 4480:
                    validating_data.write(line)
                    validating_data36.write(line)
                elif 4480 < mode_36 <= 5600:
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
