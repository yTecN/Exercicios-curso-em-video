# Exercício Python 53: Crie um programa que leia uma frase qualquer e diga se ela é um palíndromo, desconsiderando os
# espaços.
from unidecode import unidecode
fra = input('Digite uma frase: ').strip().lower()
fra = unidecode(fra)
fra = fra.replace(' ','')
if fra == fra[::-1]:
    print('Essa frase é um palíndromo')
else:
    print('Essa frase não é um palíndromo')