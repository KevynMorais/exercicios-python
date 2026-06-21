jogadores = list()
jogador = dict()
gol = list()
while True:
    jogador.clear()
    gol.clear()
    jogador['nome'] = str(input('Nome do Jogador: '))
    p = int(input(f'Quantas partidas {jogador["nome"]} jogou? '))
    for c in range (0, p):
        g = int(input(f'Quantos gols na partida {c}? '))
        gol.append(g)
    jogador['gols'] = gol[:]
    jogador['total'] = sum(gol)
    jogadores.append(jogador.copy())
    q = ' '
    while q not in 'SN':
        q = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if q == 'N':
        break
print('-='*30)
print(f'{"cod"} {"nome":>10} {"gols":>14} {"total":>15}')
for k, v in enumerate(jogadores):
    print(f'{k:<10}', end = '')
    for d in v.values():
        print(f'{str(d):<15}', end = '')
    print()
print('-='*30)
while True:
    b = int(input('Mostrar dados de qual jogador? (999 para parar) '))
    if b == 999:
        break
    if b >= len(jogadores):
        print(f'ERRO! Não existe jogador com o código {b}')
    else:
        print(f' - LEVANTAMENTO DO JOGADOR {jogadores[b]["nome"]}')
        for i, g in enumerate(jogadores[b]['gols']):
            print(f'    No jogo {i+1} fez {g} gols.')
    print('-='*30)
print('<< VOLTE SEMPRE >>')
