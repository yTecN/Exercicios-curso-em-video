# Crie um programa que leia dois nomes e duas notas de vários alunos e guarde tudo em uma lista composta.
# No final, mostre um boletim contendo a média de cada um e permita que o usuário possa mostrar as notas de cada aluno individualmente.
import QoL
QoL.Titulo('Boletim')
Lista = []
while True:
    nome = input('Nome: ')
    n1 = float(input('Nota 1: '))
    n2 = float(input('Nota 2: '))
    Lista.append([nome, [n1, n2]])
    r = input('Quer continuar? [S/N] ')[0].lower()
    while r not in 'sn':
        r = input('BURRO DO CARILHO É S OU N ANIMAL: ')[0].lower()
    if r == 'n':
        break
QoL.Linha(15)
print(f'{"No.":<4}{"NOME":<10}{"MÉDIA":>8}')
for i, c in enumerate(Lista):
    print(f'{i:<4}{c[0]}{(c[1][0]+c[1][1])/2:>8}')
print()
while True:
    QoL.Linha(15)
    aluno = int(input('Mostrar a nota de qual aluno? [999 interrompe] '))
    if aluno >= 999:
        break
    print(f'Notas de {Lista[aluno][0]} são {Lista[aluno][1]}')


