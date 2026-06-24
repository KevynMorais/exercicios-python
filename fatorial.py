def fatorial(n=1, show=False):
    """
    -> Calcula o Fatorial de um número
    :param n: O número a ser calculado
    :param show: (opcional) Mostrar ou não a conta
    :return: O valor do fatorial
    """
    num = 1
    print('-'*10)
    for c in range(n, 0, -1):
        if show:
            print(f'{c}', end = ' ')
            if c > 1:
                print(f'x', end = ' ')
            else:
                print(f'= ', end = '')
        num *= c
    return num


print(fatorial())
