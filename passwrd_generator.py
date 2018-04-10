import random


def passw_gen(count_char):
    sym_base = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
                'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
                'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M',
                'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z',
                '1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
    passwrd = []

    for i in range(count_char):
        passwrd.append(random.choice(sym_base))

    return "".join(passwrd)


while True:
    user_input = input('Ввдеите количество симоволов пароля:\n'
                       'Для выхода введите "e"\n')

    if user_input == 'e':
        break
    else:
        passw = passw_gen(int(user_input))

        print(passw)
