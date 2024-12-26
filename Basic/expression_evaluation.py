# Let's break down the expression:
# x = 1 + 2 * 3 - 4 / 5 ** 6

# Exponentiation (**)
exp_result = 5 ** 6  # 15625
# Expression: 1 + 2 * 3 - 4 / 15625

# Multiplication (*)
mul_result = 2 * 3  # 6
# Expression: 1 + 6 - 4 / 15625

# Division (/)
div_result = 4 / exp_result  # 0.000256
# Expression: 1 + 6 - 0.000256

# Addition (+)
add_result = 1 + mul_result  # 7
# Expression: 7 - 0.000256

# Subtraction (-)
x = add_result - div_result  # 6.999744

# Final value of x
print(x)  # 6.999744