# Reading lines from a file and skipping lines that start with #
with open('file.txt') as f:
    for line in f:
        if line.startswith('#'):
            continue
        print(line.strip())