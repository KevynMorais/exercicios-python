from time import sleep


def maior(*n):
    pos = mai = 0
    while pos < len(n):
        if pos == 0:
            mai = n[pos]
        else:
            if n[pos] > mai:
                mai = n[pos]
        pos += 1
    print('-='*30)
    print('Analisando os valores passados...')
    sleep(0.1)
    for numero in n:
        print(numero, end=' ')
        sleep(0.33)
    print(f'Foram informados {len(n)} valores ao todo.')
    print(f'O maior valor informado foi {mai}.')


maior(2, 9, 4, 5, 7, 1)
maior(4, 7, 0)
maior(1, 2)
maior(6)
maior()
