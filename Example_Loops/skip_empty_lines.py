# Reading lines from a file and skipping empty lines
with open('file.txt') as f:
    for line in f:
        if line.strip() == '':
            continue
        print(line.strip())