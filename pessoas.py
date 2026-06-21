pessoas = list()
dados = dict()
mulheres = list()
tot = 0
while True:
    dados.clear()
    dados['nome'] = str(input('Nome: '))
    dados['sexo'] = ' '
    while dados['sexo'] not in 'MF':
        dados['sexo'] = str(input('Sexo [M/F]: ')).strip().upper()[0]
        if dados['sexo'] not in 'MF':
            print('ERRO! Por favor, digite apenas M ou F.')
        if dados['sexo'] == 'F':
            mulheres.append(dados['nome'])
    dados['idade'] = int(input('Idade: '))
    tot += dados['idade']
    pessoas.append(dados.copy())
    q = ' '
    while q not in 'SN':
        q = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
        if q not in 'SN':
            print('ERRO! Responda apenas S ou N.')
    if q == 'N':
        break
quant = len(pessoas)
media = tot/quant
print('-='*30)
print(f'A) Ao todo temos {quant} pessoas cadastradas.')
print(f'B) A média de idade é {media:.2f} anos.')
print(f'C) As mulheres cadastradas foram {mulheres}.')
print('D) Lista de pessoas que estão acima da média:')
for pessoa in pessoas:
    if pessoa['idade'] >= media:
        print('    ')
        for k, v in pessoa.items():
            print(f' {k} = {v} ', end='')
        print()
print('\n<< ENCERRADO >>')
