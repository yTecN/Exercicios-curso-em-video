import random as rd
n1 = input('Digite o primeiro nome: ')
n2 = input('Digite o segundo nome: ')
n3 = input('Digite o terceiro nome: ')
n4 = input('Digite o quarto nome: ')
n = [ n1, n2, n3, n4]
rd.shuffle(n)
print(f'A ordem de apresentação dos trabalhos será:\n'
      f'{n}')