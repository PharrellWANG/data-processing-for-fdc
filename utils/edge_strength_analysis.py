# ==============================================================================
# Author: Pharrell_WANG
# Date: 2017/6/28
# ==============================================================================

import sys
import pandas
import datetime

from collections import OrderedDict


def edge_analyzer(INPUT_FILE):
    start_timestamp = datetime.datetime.now()
    print('=================================================')
    print('++++++++++++++++++++')
    print('start at: ')
    print(start_timestamp)
    print('++++++++++++++++++++')
    print('Name of the data file: ' + str(INPUT_FILE))
    x = OrderedDict()
    strength_dict = OrderedDict()

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
    edge_strength_of_mode_0 = 0
    edge_strength_of_mode_1 = 0
    edge_strength_of_mode_2 = 0
    edge_strength_of_mode_3 = 0
    edge_strength_of_mode_4 = 0
    edge_strength_of_mode_5 = 0
    edge_strength_of_mode_6 = 0
    edge_strength_of_mode_7 = 0
    edge_strength_of_mode_8 = 0
    edge_strength_of_mode_9 = 0
    edge_strength_of_mode_10 = 0
    edge_strength_of_mode_11 = 0
    edge_strength_of_mode_12 = 0
    edge_strength_of_mode_13 = 0
    edge_strength_of_mode_14 = 0
    edge_strength_of_mode_15 = 0
    edge_strength_of_mode_16 = 0
    edge_strength_of_mode_17 = 0
    edge_strength_of_mode_18 = 0
    edge_strength_of_mode_19 = 0
    edge_strength_of_mode_20 = 0
    edge_strength_of_mode_21 = 0
    edge_strength_of_mode_22 = 0
    edge_strength_of_mode_23 = 0
    edge_strength_of_mode_24 = 0
    edge_strength_of_mode_25 = 0
    edge_strength_of_mode_26 = 0
    edge_strength_of_mode_27 = 0
    edge_strength_of_mode_28 = 0
    edge_strength_of_mode_29 = 0
    edge_strength_of_mode_30 = 0
    edge_strength_of_mode_31 = 0
    edge_strength_of_mode_32 = 0
    edge_strength_of_mode_33 = 0
    edge_strength_of_mode_34 = 0
    edge_strength_of_mode_35 = 0
    edge_strength_of_mode_36 = 0

    RESHAPE = 0  # INIT
    csv = pandas.read_csv(INPUT_FILE, header=None).values
    print('total num of rows in csv file:')
    print(csv.shape[0])

    if csv.shape[1] == 257:
        RESHAPE = 16
    elif csv.shape[1] == 1025:
        RESHAPE = 32
    assert (csv.shape[1] == RESHAPE * RESHAPE + 1)

    with open(INPUT_FILE, 'r') as r:
        cnt = 0
        for num, line in enumerate(r):
            cnt += 1
            sys.stdout.write(
                '\r>> processing line: %d / %d' % (cnt, csv.shape[0]))
            if line[-3:-2] == ',':
                # print("yes, it is a comma.===============!!~~~~~~~~")
                last_char_in_line = int(line[-2:-1])
            else:
                # print("no, not comma.-------------~~~~~~~~`")
                last_char_in_line = int(line[-3:-1])

            mode = last_char_in_line

            # edge strength analysis
            # read one line every time
            total_strength = 0

            row = csv[cnt-1]
            # local_counter = 0
            features, label = row[:-1], row[-1]
            features = features.reshape(RESHAPE, RESHAPE)
            for i in range(RESHAPE - 1):
                for j in range(RESHAPE - 1):
                    # local_counter += 1
                    # sys.stdout.write(
                    #     '\r>> processing %d/%d' % (local_counter,
                    #                                RESHAPE ** 2))
                    horizontal_strength = \
                        features[i][j] + \
                        features[i + 1][j] - \
                        features[i][j + 1] - \
                        features[i + 1][j + 1]
                    vertical_strength = \
                        features[i][j] + \
                        features[i][j + 1] - \
                        features[i + 1][j] - \
                        features[i + 1][j + 1]
                    strength = horizontal_strength ** 2 + vertical_strength ** 2
                    total_strength += strength

            if mode == 0:
                mode_0 += 1
                edge_strength_of_mode_0 += total_strength
            elif mode == 1:
                mode_1 += 1
                edge_strength_of_mode_1 += total_strength
            elif mode == 2:
                mode_2 += 1
                edge_strength_of_mode_2 += total_strength
            elif mode == 3:
                mode_3 += 1
                edge_strength_of_mode_3 += total_strength
            elif mode == 4:
                mode_4 += 1
                edge_strength_of_mode_4 += total_strength
            elif mode == 5:
                mode_5 += 1
                edge_strength_of_mode_5 += total_strength
            elif mode == 6:
                mode_6 += 1
                edge_strength_of_mode_6 += total_strength
            elif mode == 7:
                mode_7 += 1
                edge_strength_of_mode_7 += total_strength
            elif mode == 8:
                mode_8 += 1
                edge_strength_of_mode_8 += total_strength
            elif mode == 9:
                mode_9 += 1
                edge_strength_of_mode_9 += total_strength
            elif mode == 10:
                mode_10 += 1
                edge_strength_of_mode_10 += total_strength
            elif mode == 11:
                mode_11 += 1
                edge_strength_of_mode_11 += total_strength
            elif mode == 12:
                mode_12 += 1
                edge_strength_of_mode_12 += total_strength
            elif mode == 13:
                mode_13 += 1
                edge_strength_of_mode_13 += total_strength
            elif mode == 14:
                mode_14 += 1
                edge_strength_of_mode_14 += total_strength
            elif mode == 15:
                mode_15 += 1
                edge_strength_of_mode_15 += total_strength
            elif mode == 16:
                mode_16 += 1
                edge_strength_of_mode_16 += total_strength
            elif mode == 17:
                mode_17 += 1
                edge_strength_of_mode_17 += total_strength
            elif mode == 18:
                mode_18 += 1
                edge_strength_of_mode_18 += total_strength
            elif mode == 19:
                mode_19 += 1
                edge_strength_of_mode_19 += total_strength
            elif mode == 20:
                mode_20 += 1
                edge_strength_of_mode_20 += total_strength
            elif mode == 21:
                mode_21 += 1
                edge_strength_of_mode_21 += total_strength
            elif mode == 22:
                mode_22 += 1
                edge_strength_of_mode_22 += total_strength
            elif mode == 23:
                mode_23 += 1
                edge_strength_of_mode_23 += total_strength
            elif mode == 24:
                mode_24 += 1
                edge_strength_of_mode_24 += total_strength
            elif mode == 25:
                mode_25 += 1
                edge_strength_of_mode_25 += total_strength
            elif mode == 26:
                mode_26 += 1
                edge_strength_of_mode_26 += total_strength
            elif mode == 27:
                mode_27 += 1
                edge_strength_of_mode_27 += total_strength
            elif mode == 28:
                mode_28 += 1
                edge_strength_of_mode_28 += total_strength
            elif mode == 29:
                mode_29 += 1
                edge_strength_of_mode_29 += total_strength
            elif mode == 30:
                mode_30 += 1
                edge_strength_of_mode_30 += total_strength
            elif mode == 31:
                mode_31 += 1
                edge_strength_of_mode_31 += total_strength
            elif mode == 32:
                mode_32 += 1
                edge_strength_of_mode_32 += total_strength
            elif mode == 33:
                mode_33 += 1
                edge_strength_of_mode_33 += total_strength
            elif mode == 34:
                mode_34 += 1
                edge_strength_of_mode_34 += total_strength
            elif mode == 35:
                mode_35 += 1
                edge_strength_of_mode_35 += total_strength
            elif mode == 36:
                mode_36 += 1
                edge_strength_of_mode_36 += total_strength

                # print("last char in line: " + str(last_char_in_line))
                # print("type : " + str(type(last_char_in_line)))
                # print('')
        # x["mode_0"] = mode_0
        x['mode__0'] = mode_0
        x['mode__1'] = mode_1
        x['mode__2'] = mode_2
        x['mode__3'] = mode_3
        x['mode__4'] = mode_4
        x['mode__5'] = mode_5
        x['mode__6'] = mode_6
        x['mode__7'] = mode_7
        x['mode__8'] = mode_8
        x['mode__9'] = mode_9
        x['mode_10'] = mode_10
        x['mode_11'] = mode_11
        x['mode_12'] = mode_12
        x['mode_13'] = mode_13
        x['mode_14'] = mode_14
        x['mode_15'] = mode_15
        x['mode_16'] = mode_16
        x['mode_17'] = mode_17
        x['mode_18'] = mode_18
        x['mode_19'] = mode_19
        x['mode_20'] = mode_20
        x['mode_21'] = mode_21
        x['mode_22'] = mode_22
        x['mode_23'] = mode_23
        x['mode_24'] = mode_24
        x['mode_25'] = mode_25
        x['mode_26'] = mode_26
        x['mode_27'] = mode_27
        x['mode_28'] = mode_28
        x['mode_29'] = mode_29
        x['mode_30'] = mode_30
        x['mode_31'] = mode_31
        x['mode_32'] = mode_32
        x['mode_33'] = mode_33
        x['mode_34'] = mode_34
        x['mode_35'] = mode_35
        x['mode_36'] = mode_36

        veri_1 = 0
        print('=================================================')
        print("COUNTING START...")
        for m, n in x.items():
            print(str(m) + " :   " + str(
                n) + '   <<------ ||-------->>      ' + str(
                m) + " / total (%) :   " + str(
                float(n) / float(cnt)))
            veri_1 += float(n) / float(cnt)

        print('*** Verification ***')
        print(
            "Sum of the percentages (output should be nearly equal to 1 or 0.999999..) : " + str(
                veri_1))

        sorted_x = OrderedDict(sorted(x.items(), key=lambda t: t[1]))

        print("")
        print('Below are the sorted list of all the modes (smallest first)')
        veri_2 = 0
        for m, n in sorted_x.items():
            print(str(m) + " :   " + str(n) + '  <<------ ||-------->> ' + str(
                m) + " / total (%) :   " + str(
                float(n) / float(cnt)))
            veri_2 += float(n) / float(cnt)

        print('===================')
        print('*** Verification ***')
        print(
            "Sum of the percentages (output should be nearly equal to 1 or 0.999999..) : " + str(
                veri_2))
        print("total lines/records in the csv file : " + str(cnt))
        print("COUNTING END...")
        print('=================================================')

        strength_dict[
            'edge_strength_of_mode__0'] = edge_strength_of_mode_0 / mode_0
        strength_dict[
            'edge_strength_of_mode__1'] = edge_strength_of_mode_1 / mode_1
        strength_dict[
            'edge_strength_of_mode__2'] = edge_strength_of_mode_2 / mode_2
        strength_dict[
            'edge_strength_of_mode__3'] = edge_strength_of_mode_3 / mode_3
        strength_dict[
            'edge_strength_of_mode__4'] = edge_strength_of_mode_4 / mode_4
        strength_dict[
            'edge_strength_of_mode__5'] = edge_strength_of_mode_5 / mode_5
        strength_dict[
            'edge_strength_of_mode__6'] = edge_strength_of_mode_6 / mode_6
        strength_dict[
            'edge_strength_of_mode__7'] = edge_strength_of_mode_7 / mode_7
        strength_dict[
            'edge_strength_of_mode__8'] = edge_strength_of_mode_8 / mode_8
        strength_dict[
            'edge_strength_of_mode__9'] = edge_strength_of_mode_9 / mode_9
        strength_dict[
            'edge_strength_of_mode_10'] = edge_strength_of_mode_10 / mode_10
        strength_dict[
            'edge_strength_of_mode_11'] = edge_strength_of_mode_11 / mode_11
        strength_dict[
            'edge_strength_of_mode_12'] = edge_strength_of_mode_12 / mode_12
        strength_dict[
            'edge_strength_of_mode_13'] = edge_strength_of_mode_13 / mode_13
        strength_dict[
            'edge_strength_of_mode_14'] = edge_strength_of_mode_14 / mode_14
        strength_dict[
            'edge_strength_of_mode_15'] = edge_strength_of_mode_15 / mode_15
        strength_dict[
            'edge_strength_of_mode_16'] = edge_strength_of_mode_16 / mode_16
        strength_dict[
            'edge_strength_of_mode_17'] = edge_strength_of_mode_17 / mode_17
        strength_dict[
            'edge_strength_of_mode_18'] = edge_strength_of_mode_18 / mode_18
        strength_dict[
            'edge_strength_of_mode_19'] = edge_strength_of_mode_19 / mode_19
        strength_dict[
            'edge_strength_of_mode_20'] = edge_strength_of_mode_20 / mode_20
        strength_dict[
            'edge_strength_of_mode_21'] = edge_strength_of_mode_21 / mode_21
        strength_dict[
            'edge_strength_of_mode_22'] = edge_strength_of_mode_22 / mode_22
        strength_dict[
            'edge_strength_of_mode_23'] = edge_strength_of_mode_23 / mode_23
        strength_dict[
            'edge_strength_of_mode_24'] = edge_strength_of_mode_24 / mode_24
        strength_dict[
            'edge_strength_of_mode_25'] = edge_strength_of_mode_25 / mode_25
        strength_dict[
            'edge_strength_of_mode_26'] = edge_strength_of_mode_26 / mode_26
        strength_dict[
            'edge_strength_of_mode_27'] = edge_strength_of_mode_27 / mode_27
        strength_dict[
            'edge_strength_of_mode_28'] = edge_strength_of_mode_28 / mode_28
        strength_dict[
            'edge_strength_of_mode_29'] = edge_strength_of_mode_29 / mode_29
        strength_dict[
            'edge_strength_of_mode_30'] = edge_strength_of_mode_30 / mode_30
        strength_dict[
            'edge_strength_of_mode_31'] = edge_strength_of_mode_31 / mode_31
        strength_dict[
            'edge_strength_of_mode_32'] = edge_strength_of_mode_32 / mode_32
        strength_dict[
            'edge_strength_of_mode_33'] = edge_strength_of_mode_33 / mode_33
        strength_dict[
            'edge_strength_of_mode_34'] = edge_strength_of_mode_34 / mode_34
        strength_dict[
            'edge_strength_of_mode_35'] = edge_strength_of_mode_35 / mode_35
        strength_dict[
            'edge_strength_of_mode_36'] = edge_strength_of_mode_36 / mode_36

        print('=================================================')
        print("COUNTING START...")
        for m, n in strength_dict.items():
            print(str(m) + " :   " + str(n))
        sorted_x = OrderedDict(
            sorted(strength_dict.items(), key=lambda t: t[1]))

        print('Below are the sorted list of all the modes (smallest first)')
        for m, n in sorted_x.items():
            print(str(m) + " :   " + str(n))
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

        return x, strength_dict