def leiaInt(msg):
    while True:
        try:
            valor = int(input(msg))
        except KeyboardInterrupt:
            print('\n\033[0;33mO usuário preferiu não informar o número inteiro.\033[m')
            return 0
        except (ValueError, TypeError):
            print('\033[0;31mERRO! Por favor, digite um número inteiro válido.\033[m')
            continue
        else:
            return valor



def leiaFloat(msg):
    while True:
        try:
            valor = float(input(msg))
        except KeyboardInterrupt:
            print('\n\033[0;33mO usuário preferiu não informar o número real.\033[m')
            return 0
        except (ValueError, TypeError):
            print('\033[0;31mERRO! Por favor, digite um número real válido.\033[m')
            continue
        else:
            return valor


x = leiaInt('Digite um Inteiro: ')
y = leiaFloat('Digite um Real: ')
print(f'O valor inteiro digitado foi {x} e o real foi {y}')