# User input for age
user_input = input("Enter your age: ")

# Validate and convert the input to an integer
try:
    age = int(user_input)
    print(f"Next year, you will be {age + 1} years old.")
except ValueError:
    print("Please enter a valid integer for your age.")