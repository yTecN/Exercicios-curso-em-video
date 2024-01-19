# pacotes
from random import randint
# variaveis
vit = 0
# código
while True:
    pc = randint(1,10)
    jogador = int(input('\033[34mDigite um número: '))
    pi = ' '
    s = jogador + pc
    while not pi in 'piPI':
        pi = input('Par ou ímpar? (P/I) ').strip().lower()[0]
    print(f'\033[33mVocê jogou {jogador} e o computador jogou {pc}. Total: {s}')
    print('Deu PAR' if s % 2 == 0 else 'Deu IMPAR')
    if pi == 'p':
        if s % 2 == 0:
            vit += 1
            print(f'\033[32mVocê venceu!!, Pontos atuais {vit}')
        else:
            print('\033[31mVocê perdeu!!')
            break
    elif pi == 'i':
        if s % 2 == 1:
            vit += 1
            print(f'\033[32mVocê venceu!!, Pontos atuais {vit}')
        else:
            print('\033[31mVocê perdeu!!')
            break
if vit > 1:
    print(f'\033[36mVocê teve {vit} consecutivas')
elif vit == 1:
    print('\033[36mVocê teve 1 vitória consecutiva')
else:
    print('\033[36mVocê não teve vitórias')