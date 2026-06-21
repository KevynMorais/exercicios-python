jogador = dict()
gol = list()
jogador['nome'] = str(input('Nome do Jogador: '))
p = int(input(f'Quantas partidas {jogador["nome"]} jogou? '))
for c in range (0, p):
    g = int(input(f'Quantos gols na partida {c}? '))
    gol.append(g)
jogador['gols'] = gol[:]
jogador['total'] = sum(gol)
print('-='*30)
print(jogador)
print('-='*30)
for k, v in jogador.items():
    print(f'O campo {k} tem o valor {v}')
print('-='*30)
print(f'O jogador {jogador["nome"]} jogou {p} partidas.')
for c in range (0, p):
    print(f' => Na partida {c}, fez {jogador["gols"][c]} gols.')
print(f'Foi um total de {jogador["total"]} gols.')
