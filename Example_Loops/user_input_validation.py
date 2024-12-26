# Continuously asking for user input until a valid input is provided
while True:
    user_input = input('Enter a number: ')
    if not user_input.isdigit():
        print('Invalid input, try again.')
        continue
    print(f'You entered: {user_input}')
    break