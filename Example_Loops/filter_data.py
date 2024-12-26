# Filtering out specific items from a list
items = ['apple', 'banana', 'cherry', 'date']
for item in items:
    if item == 'banana':
        continue
    print(item)