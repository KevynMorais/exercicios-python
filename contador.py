from time import sleep


def contagem(inicio, fim, passo):
    print('-=' * 30)
    print(f'Contagem de {inicio} até {fim} de {passo} em {passo}.')
    sleep(0.7)
    if inicio < fim:
        for c in range(inicio, fim + 1, passo):
            print(c, end = ' ')
            sleep(0.3)
    elif inicio > fim:
        if passo > 0:
            for c in range(inicio, fim - 1, passo * (-1)):
                print(c, end=' ')
                sleep(0.3)
        elif passo < 0:
            for c in range(inicio, fim - 1, passo):
                print(c, end=' ')
                sleep(0.5)
    else:
        print('ERRO! Início e fim iguais!')
    print('FIM!')


contagem(1, 10, 1)
contagem(10, 0, 2)

print('-='*30)
print('Agora é a sua vez de personalizar a contagem!')
i = int(input('Início: '))
f = int(input('Fim:    '))
p = int(input('Passo:  '))
if p == 0:
    p = 1
contagem(i, f, p)
