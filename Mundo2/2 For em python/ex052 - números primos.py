# Exercício Python 52: Faça um programa que leia um número inteiro e diga se ele é ou não um número primo
n = int(input('\033[35mDigite um número inteiro: '))
t = 0
for x in range(1, n + 1):
    if n % x == 0:
        print(f'\033[34m{x}', end=' ')
        t += 1
    else:
        print(f'\033[33m{x}', end=' ')
if t == 2:
    print(f'\n\033[32m{n} é um número primo')
else:
    print(f'\n\033[31m{n} não é um número primo')