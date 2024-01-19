from random import randint
n = randint(0, 5)
c = int(input('Digite qual número você acha que foi sorteado: '))
if c == n:
    print('Parabéns! Você acertou!!')
else:
    print(f'Você perdeu!, o número era {n}')