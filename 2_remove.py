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


list_of_input_files = ['/Users/Pharrell_WANG/PycharmProjects/fdc-tf-data-preprocessing/data_after_step1_concat/merged_from_three_sequences_size_16.csv']
list_of_output_files = ['/Users/Pharrell_WANG/PycharmProjects/fdc-tf-data-preprocessing/data_after_step2_remove/comma_removed_size_16.csv']

for x in range(len(list_of_input_files)):
    comma_remover(list_of_input_files[x], list_of_output_files[x])
