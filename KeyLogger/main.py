import keyboard

def main():
    show_menu()


def key_reader():
    keyboard.on_press(pressedKeys)
    keyboard.wait()


def show_menu():
    print('""""""""""""""""')
    print('Welcome To KeyMap')
    print('""""""""""""""""')
    print('1. Start KeyMap')
    print('2. Read File')
    print('3. Reset File')
    print(f'4. Exit\n')

    option = int(input(f'Select(1-3):\n\n '))

    if option == 1:
        print('Listening...(Stop with Crt+C)')
        key_reader()
    elif option == 2:
        text_reader()
        print(f'\n')
        main()
    elif option == 3:
        reset_file()
        main()


def reset_file():
    with open("data.txt", "w") as file:
        file.write("")


def text_reader():
    file = open('data.txt', 'r').read()
    print(f'\n\nThis is what I listen homie:\n {file}')


def pressedKeys(key):
    with open('data.txt', 'a') as file:

        if key.name == 'space':
            file.write(' ')
        else:
            file.write(key.name)

if __name__ == '__main__':
    main()

