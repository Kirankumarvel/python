# Implicit Type Conversion
print(float(99) + 100)  # 199.0

# Explicit Type Conversion
i = 42
print(type(i))  # <class 'int'>

# Converting Integer to Float
f = float(i)
print(f)  # 42.0
print(type(f))  # <class 'float'>

# Using int() and float() Functions
float_value = 3.14
int_value = int(float_value)
print(int_value)  # 3
print(type(int_value))  # <class 'int'>

int_value = 7
float_value = float(int_value)
print(float_value)  # 7.0
print(type(float_value))  # <class 'float'>

# Practical Examples
# Implicit Conversion
result = 10 + 2.5
print(result)  # 12.5
print(type(result))  # <class 'float'>

# Explicit Conversion
a = 5
b = 2.8
c = a + int(b)
print(c)  # 7
print(type(c))  # <class 'int'>