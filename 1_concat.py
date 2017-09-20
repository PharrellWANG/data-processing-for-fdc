# ==============================================================================
# Author: Pharrell_WANG
# Date: 2017/6/28
# ==============================================================================
import os

homedir = os.environ['HOME']

size_64_files = [
    homedir + '/data_collecting/ghost_fly/data_exporting/mix_data_0.csv',
    homedir + '/data_collecting/newspaper/data_exporting/mix_data_0.csv',
    homedir + '/data_collecting/poznan_hall_1920x1088/data_exporting/mix_data_0.csv',
    homedir + '/data_collecting/shark_1920x1088/data_exporting/mix_data_0.csv',
]

size_32_files = [
    homedir + '/data_collecting/ghost_fly/data_exporting/mix_data_1.csv',
    homedir + '/data_collecting/newspaper/data_exporting/mix_data_1.csv',
    homedir + '/data_collecting/poznan_hall_1920x1088/data_exporting/mix_data_1.csv',
    homedir + '/data_collecting/shark_1920x1088/data_exporting/mix_data_1.csv',
]

size_16_files = [
    homedir + '/data_collecting/ghost_fly/data_exporting/mix_data_2.csv',
    homedir + '/data_collecting/newspaper/data_exporting/mix_data_2.csv',
    homedir + '/data_collecting/poznan_hall_1920x1088/data_exporting/mix_data_2.csv',
    homedir + '/data_collecting/shark_1920x1088/data_exporting/mix_data_2.csv',
]

size_08_files = [
    homedir + '/data_collecting/ghost_fly/data_exporting/mix_data_3.csv',
    homedir + '/data_collecting/newspaper/data_exporting/mix_data_3.csv',
    homedir + '/data_collecting/poznan_hall_1920x1088/data_exporting/mix_data_3.csv',
    homedir + '/data_collecting/shark_1920x1088/data_exporting/mix_data_3.csv',
]

size_04_files = [
    homedir + '/data_collecting/ghost_fly/data_exporting/mix_data_4.csv',
    homedir + '/data_collecting/newspaper/data_exporting/mix_data_4.csv',
    homedir + '/data_collecting/poznan_hall_1920x1088/data_exporting/mix_data_4.csv',
    homedir + '/data_collecting/shark_1920x1088/data_exporting/mix_data_4.csv',
]

INPUT_LIST = [size_04_files, size_08_files, size_16_files, size_32_files, size_64_files]
for INPUT_FILE in INPUT_LIST:
    # for avoiding the type checking errors, here we create a new var
    INPUT_FILE_ = INPUT_FILE
    name_of_input_file = [k for k, v in locals().items() if v is INPUT_FILE_][0]
    print(name_of_input_file)
    OUTPUT_FILE = homedir + '/data/pure_eval/step1_output/' + name_of_input_file + '.csv'
    with open(OUTPUT_FILE, 'w') as w:
        for input_file in INPUT_FILE:
            with open(input_file, 'r') as r:
                for num, line in enumerate(r):
                    w.write(line)
