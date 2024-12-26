# A simple game loop that continues until the player types 'quit'
while True:
    command = input('Enter command: ')
    if command == 'quit':
        break
    print(f'Executing {command}')
