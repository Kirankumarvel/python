# The general syntax of an assignment statement is:
# variable = expression

# variable: The name of the variable where the result will be stored.
# expression: A combination of values, variables, and operators that Python evaluates to produce a result.

# Example of an Assignment Statement
# Let's break down the example provided:
# x = 3.9 * x * (1 - x)

# Variable:
# x: This is the variable where the result of the expression will be stored.

# Expression:
# 3.9 * x * (1 - x): This is the expression that will be evaluated. It involves multiplication and subtraction operations.

# Step-by-Step Evaluation
# Let's assume x initially has a value of 0.5. Here's how the assignment statement would be evaluated step-by-step:

# Initial Value:
x = 0.5

# Evaluate the Expression:
# Substitute the value of x into the expression:
# 3.9 * 0.5 * (1 - 0.5)

# Perform the subtraction inside the parentheses:
# 1 - 0.5 = 0.5

# Multiply the results:
# 3.9 * 0.5 * 0.5 = 3.9 * 0.25 = 0.975

# Assign the Result:
# The result of the expression 0.975 is assigned to the variable x:
x = 3.9 * x * (1 - x)

# Print the updated value of x
print(x)  # Output: 0.975

# Key Points to Remember
# Order of Operations: Python follows the standard mathematical order of operations (parentheses, exponents, multiplication and division, addition and subtraction) when evaluating expressions.
# Variable Update: The value of the variable on the left-hand side is updated with the result of the expression on the right-hand side.
# Reassignment: Variables can be reassigned new values multiple times throughout a program.

# Practical Example
# Here's a practical example to illustrate assignment statements:

# Initial assignment
x = 2

# Update x using an expression
x = 3.9 * x * (1 - x)

# Print the updated value of x
print(x)  # Output: -7.8

# Initial Assignment: x is initially assigned the value 2.
# Update: The expression 3.9 * x * (1 - x) is evaluated with x = 2, and the result is assigned back to x.
# Output: The updated value of x is printed.
