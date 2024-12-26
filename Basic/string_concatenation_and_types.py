# String concatenation
greeting = 'hello' + ' there'
print(greeting)  # hello there

# Attempting to add an integer to a string (will raise an error)
try:
    greeting = greeting + 1
except TypeError as e:
    print(e)  # Can't convert 'int' object to str implicitly

# Checking types
print(type(greeting))  # <class 'str'>
print(type('hello'))  # <class 'str'>
print(type(1))  # <class 'int'>