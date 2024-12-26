# Processing files in a directory and skipping files with a specific extension
import os

for filename in os.listdir('.'):
    if filename.endswith('.tmp'):
        continue
    print(f'Processing {filename}')