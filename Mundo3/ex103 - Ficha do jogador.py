# Faça um programa que tenha uma função chamada ficha(), que receba dois parâmetros opcionais:
# o nome de um jogador e quantos gols ele marcou. 
# O programa deverá ser capaz de mostrar a ficha do jogador, mesmo que algum dado não tenha sido informado corretamente.

def ficha(jogador='<desconhecido>', gols=0):
    return f'O {jogador} marcou {gols} gols'


nome = input('Qual o nomedo do jogador? ')
gols = input('Quantos gols ele fez? ')
if gols.isnumeric():
    gols = int(gols)
    if nome.strip() == '':
        print(ficha(gols=gols))
    else:
        print(ficha(jogador=nome, gols=gols))
else:
    if nome.strip() == '':
        print(ficha())
    else:
        print(ficha(jogador=nome))

