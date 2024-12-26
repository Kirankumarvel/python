# Addition with Integers
a = 10
b = 5
result = a + b
print(result)  # 15

# Concatenation with Strings
first_name = 'John'
last_name = 'Doe'
full_name = first_name + ' ' + last_name
print(full_name)  # John Doe

# Mixing Types (Error)
num = 10
text = ' apples'
# result = num + text  # This will raise a TypeError
result = str(num) + text  # Correct way to concatenate
print(result)  # 10 apples