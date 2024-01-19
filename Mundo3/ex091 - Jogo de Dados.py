import random
from operator import itemgetter
jogadas = {}
for c in range(1,5):
    jogada = random.randint(1,6)
    jogadas['jogador '+str(c)] = jogada
for k, v in jogadas.items():
    print(f'{k} tirou {v}')
print('-='*15)
placar = sorted(jogadas.items(), key=itemgetter(1), reverse=True)
for i, (k, v) in enumerate(placar, start=1):
    print(f'{i}° lugar: {k}, com {v}')