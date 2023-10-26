def encode(pass_str):
    return ''.join(str(int(element)+3)[-1] for element in pass_str)

def decode(password):
    return ''.join(str(int(x)+7)[-1] for x in password)

def main():
    menu_num = 'not three!'
    encoded_str = ''
    while menu_num != 3:
        print('Menu')
        print('-------------')
        print('1. Encode')
        print('2. Decode')
        print('3. Quit')
        print()
        menu_num = int(input('Please enter an option: '))
        if menu_num == 1:
            pass_str = input('Please enter your password to encode: ')
            encoded_str = encode(pass_str)
            print('Your password has been encoded and stored!')
            print()
        elif menu_num == 2:
            print(f'The encoded password is {encoded_str}, and the original password is {decode(encoded_str)}.')
            print()

if __name__ == '__main__':
    main()
