# Looping through a range of numbers and skipping multiples of 3
for i in range(10):
    if i % 3 == 0:
        continue
    print(i)