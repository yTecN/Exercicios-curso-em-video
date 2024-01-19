import random as rd
n1 = input('Digite o primeiro nome: ')
n2 = input('Digite o segundo nome: ')
n3 = input('Digite o terceiro nome: ')
n4 = input('Digite o quarto nome: ')
nomes = [ n1, n2, n3, n4 ]
print(f'O sorteado para apagar o quadro foi: {rd.choice(nomes)}')