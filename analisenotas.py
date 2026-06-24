def notas(*n, sit=False):
    """
    -> Função para analisar notas e situações de vários alunos.
    :param n: uma ou mais notas dos alunos.
    :param sit: valor opcional, indicando se deve adicionar ou não a situação
    :return: dicionário com várias informações sobre a situação da turma.
    """

    ns = dict()
    ns['total'] = len(n)
    ns['maior'] = ns['menor'] = cont = soma = 0
    for nota in n:
        if cont == 0:
            ns['maior'] = ns['menor'] = nota
        else:
            if nota > ns['maior']:
                ns['maior'] = nota
            if nota < ns['menor']:
                ns['menor'] = nota
        soma += nota
        cont += 1
    ns['média'] = soma / len(n)
    if sit:
        if ns['média'] < 6:
            ns['situação'] = 'RUIM'
        elif 6 <= ns['média'] < 7:
            ns['situação'] = 'REGULAR'
        elif ns['média'] >= 7:
            ns['situação'] = 'BOA'
    return ns


resp = notas(5.5, 9.5, 10, 6.5, sit=True)
print(resp)
