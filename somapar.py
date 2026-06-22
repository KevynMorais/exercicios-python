from time import sleep
from random import randint
sorteados = []


def sorteia():
    sorteados.clear()
    for c in range (1, 6):
        sorteados.append(randint(1, 10))
    print('Sorteando os valores da lista:', end = ' ')
    for n in sorteados:
        print(n, end = ' ')
        sleep(0.4)
    print('PRONTO!')


def soma_par():
    soma = 0
    for num in sorteados:
        if num % 2 == 0:
            soma += num
    print(f'Somando os valores pares de {sorteados}, temos {soma}.')

sorteia()
soma_par()
sorteia()
soma_par()
