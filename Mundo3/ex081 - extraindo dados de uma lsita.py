'''Exercício Python 081: Crie um programa que vai ler vários números e colocar em uma lista.
Depois disso, mostre:                                                                                                                                               
A) Quantos números foram digitados.                                                                                                                    
B) A lista de valores, ordenada de forma decrescente.
C) Se o valor 5 foi digitado e está ou não na lista.'''

lista = []

while True:
    numero = int(input('Digite um valor: '))
    lista.append(numero)
    opc = input('Quer continuar? [S/N] ').strip().lower()
    while opc not in 'sn':
        opc = input('Tente novamente seu porra: ')
    if opc == 's':
        continue
    elif opc == 'n':
        print('Entendido, finalizando programa...')
        break
print(f'Foram digitado(s) {len(lista)} número(s)')
print(f'Os números digitados em ordem decrescente foram: {sorted(lista, reverse=True)}')
if 5 in lista:
    print('O número 5 está presente na lista')
else:
    print('O número 5 não está presente na lista')