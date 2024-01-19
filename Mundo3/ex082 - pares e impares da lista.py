import QoL
lista = []
pares = []
impares = []
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
for i in lista:
    if i % 2 == 0:
        pares.append(i)
    else:
        impares.append(i)
QoL.Linha(15)
print(f'Os valores digitados foram {lista}')
print(f'Os valores pares digitados foram {pares}')
print(f'Os valores impares digitados foram {impares}')