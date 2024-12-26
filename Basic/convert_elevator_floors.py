# Author: Jane Doe
# Date: 2024-12-25
# This script converts European elevator floors to US floors

# Prompt the user for the European floor number
inp = input('Europe floor? ')

# Convert the input to an integer and add 1 to get the US floor number
usf = int(inp) + 1

# Print the US floor number
print('US floor', usf)

# The following line is for debugging purposes
# print('Debug: inp =', inp, 'usf =', usf)