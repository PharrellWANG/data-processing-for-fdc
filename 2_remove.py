# ------------------------------------------------------------------------------
# Author: Pharrell_WANG
#   Date: 2017/6/28
# ------------------------------------------------------------------------------


def comma_remover(INPUT_FILE, OUTPUT_FILE):
    with open(INPUT_FILE, 'r') as r, \
            open(OUTPUT_FILE, 'w') as w:
        cnt = 0
        for num, line in enumerate(r):
            cnt += 1
            if num >= 0:
                newline = line[:-2] + "\n" if "\n" in line else line[:-1]
            else:
                newline = line
            w.write(newline)

        print("total lines of " + INPUT_FILE + str(" :      ") + str(cnt))

import os
homedir = os.environ['HOME']
list_of_input_files = [homedir + '/data/step1_output/size_08_files.csv',
                       homedir + '/data/step1_output/size_16_files.csv',
                       homedir + '/data/step1_output/size_32_files.csv',
                       homedir + '/data/step1_output/size_64_files.csv'
                       ]
list_of_output_files = [homedir + '/data/step2_output/size_08_files.csv',
                        homedir + '/data/step2_output/size_16_files.csv',
                        homedir + '/data/step2_output/size_32_files.csv',
                        homedir + '/data/step2_output/size_64_files.csv'
                        ]

for x in range(len(list_of_input_files)):
    comma_remover(list_of_input_files[x], list_of_output_files[x])
