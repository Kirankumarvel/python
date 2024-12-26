# Continuously asking for a password until the correct one is entered
correct_password = 'secret'
while True:
    password = input('Enter password: ')
    if password == correct_password:
        break
    print('Incorrect password, try again.')
print('Access granted.')