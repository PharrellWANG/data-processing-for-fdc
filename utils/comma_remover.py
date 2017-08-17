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