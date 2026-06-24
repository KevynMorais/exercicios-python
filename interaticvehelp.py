def ajuda():
    while True:
        print('\033[1;30;42m-' * 30)
        print(f'{"Sistema de Ajuda PyHELP":^28}')
        print('-' * 30)
        c = str(input('\033[mFunção ou Biblioteca > ')).strip().lower()
        if c == 'fim':
            print('\033[1;37;41m~'*30)
            print(f'{"ATÉ LOGO!":^29}')
            print('~'*30)
            break
        else:
            print('\033[1;30;44m~'*50)
            print(f'Acessando o comando de manual do "{c}"')
            print('~'*50)
            print('\033[m', end = '')
            print(f'\033[7;37;40m')
            help(f'{c}')
            print(f'\033[m', end = '')


ajuda()
