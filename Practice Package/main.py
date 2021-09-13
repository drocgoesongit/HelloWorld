command = ('')
is_started = False
while True:
    command = input('> ').lower()
    if command == 'start':
        if is_started:
            print('Car has already started.')
        else:
            is_started = True
            print('Car started. Car is ready to go.')
    elif command == 'stop':
        if not is_started:
            print('Car is already stopped.')
        else:
            is_started = False
            print('Car stopped.')
    elif command == 'help':
        print('''Type :
Start - To start the race.
Stop - To stop the race.
Quit - To quit the game.''')
    elif command == 'quit':
        print('Quitting the game.')
        break
    else:
        print('Command not known.')
