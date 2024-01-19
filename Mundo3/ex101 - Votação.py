import QoL


def verifica(ano):
    from datetime import date
    age = date.today().year - ano
    if age >= 65 or age >= 16 and age < 18:
        return f'Com {age}, Voto OPCIONAL'
    elif age >= 18:
        return f'Com`{age}, Voto OBRIGATÓRIO'
    else:
        return f'Com {age}, Voto NEGADO'


print(verifica(int(input('Em que ano você nasceu? '))))