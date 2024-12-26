# String Assignment and Type Checking
sval = '123'
print(type(sval))  # <class 'str'>

# Attempting to Add a String and an Integer (will raise an error)
try:
    print(sval + 1)
except TypeError as e:
    print(e)  # Can't convert 'int' object to str implicitly

# Converting String to Integer
ival = int(sval)
print(type(ival))  # <class 'int'>

# Adding an Integer to Another Integer
print(ival + 1)  # 124

# Error When Converting Non-Numeric String to Integer
nsv = 'hello bob'
try:
    niv = int(nsv)
except ValueError as e:
    print(e)  # invalid literal for int() with base 10: 'hello bob'

# Using the input() Function
nam = input('Who are you? ')

# Printing the User's Input
print('Welcome', nam)