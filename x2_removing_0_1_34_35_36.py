"""
for removing mode 0, 1, 34, 35, 36
"""
import os
import sys

homedir = os.environ['HOME']
inFile = homedir + '/data/smooth_removed/ave_90_size_08_files.csv'
outFile = homedir + '/data/smooth_removed/32_classes__ave_90_size_08_files.csv'


def processing(a, b):
    with open(a, 'r') as in_file, open(b, 'w') as out_file:
        cnt = 0
        wri_line = 0
        for line in in_file:
            cnt += 1
            if ((line[-3:-2] == ',' and
                         int(line[-2:-1]) != 0 and
                         int(line[-2:-1]) != 1)) or \
                    (line[-4:-3] == ',' and
                             int(line[-3:-1]) != 34 and
                             int(line[-3:-1]) != 35 and
                             int(line[-3:-1]) != 36):
                wri_line += 1
                sys.stdout.write(
                    '\r>> processing line: %d ; and now writing line: %d' %
                    (cnt, wri_line))
                out_file.write(line)


processing(inFile, outFile)
