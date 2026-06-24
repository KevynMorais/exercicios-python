from datetime import datetime


def voto(n=0):
    if 0 <= n < 16:
        return f"Com {n} anos: NÃO VOTA."
    elif 16 <= n < 18 or n >= 65:
        return f"Com {n} anos: VOTO OPCIONAL."
    elif 18 <= n < 65:
        return f"Com {n} anos: VOTO OBRIGATÓRIO."
    else:
        return "Dado inválido."

nasc = int(input('Em que ano você nasceu? '))
idade = datetime.now().year - nasc
print(voto(idade))
