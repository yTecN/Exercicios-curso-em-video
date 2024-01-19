import random

palpites = []
lista = []
numero_jogos = int(input('Quantos jogos vc vai querer perd... digo, fazer? '))
for x in range(numero_jogos+1):
    for n in range(6):
        numero_sorteado = random.randint(1, 60)
        while numero_sorteado in palpites:
            numero_sorteado = random.randint(1, 60)
        palpites.append(numero_sorteado)
    lista.append(palpites[:])
    palpites.clear()
for i, l in enumerate(lista):
    print(f'Jogo de número {i}: {l}')

