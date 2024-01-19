# Exercício Python 54: Crie um programa que leia o ano de nascimento de sete pessoas. No final, mostre quantas
# pessoas ainda não atingiram a maioridade e quantas já são maiore
from datetime import date
ano = date.today().year
c1 = 0
c2 = 0
nomes = [ ]
for x in range(1,8):
    n = int(input(f'Digite o ano de nascimento da {x}° pessoa: '))
    nomes.append(n)
print(nomes)
for y in range(0, 7):
    i = ano - nomes[y]
    if i < 18:
        m = 'menor de idade'
        c1 += 1
    else:
        m = 'maior de idade'
        c2 += 1
print(f'{c1} pessoas são menores de idade')
print(f'{c2} pessoas são maiores de idade')