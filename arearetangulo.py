def area(a, b):
    area = a * b
    print(f'A área de um terreno de {a:.1f}x{b:.1f} é de {area:.2f}m².')


print(f'{"Controle de Terrenos":^20}')
print('-'*25)
a = float(input('LARGURA (m): '))
b = float(input('COMPRIMENTO (m): '))
area(a, b)
