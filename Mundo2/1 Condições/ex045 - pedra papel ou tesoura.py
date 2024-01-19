from random import randint
tupla = ('pedra', 'papel', 'tesoura')
pc = randint(0, 2)
print('''[ 0 ] pedra
[ 1 ] papel
[ 2 ] tesoura''')
j = int(input('Sua jogada: '))
while j > 2 or j < 0:
    j = int(input('Sua jogada: '))
print('-='*15)
print(f'O computador jogou {tupla[pc]}')
print(f'O jogador jogou {tupla[j]}')
print('-='*15)
if pc == 0:
    if j == 0:
        print('Empate')
    if j == 1:
        print('O jogador venceu')
    if j == 2:
        print('O computador venceu')
elif pc == 1:
    if j == 0:
        print('O computador vendeu')
    if j == 1:
        print('Empate')
    if j == 2:
        print('O jogador venceu')
elif pc == 2:
    if j == 0:
        print('O jogador venceu')
    if j == 1:
        print('O computador venceu')
    if j == 2:
        print('Empate')