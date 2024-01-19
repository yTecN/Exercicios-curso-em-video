from time import sleep
import QoL
lista = []
pessoas = []
while True:
    nome = input('Digite o nome: ')
    peso = float(input('Digite o peso: (Kg) '))
    pessoas.append(nome)
    pessoas.append(peso)
    lista.append(pessoas[:])
    pessoas.clear()
    r = input('Quer continuar? [S/N] ')[0].lower().strip()
    if r == 's':
        continue
    else:
        print('Finalizando..')
        sleep(1)
        break
QoL.Linha(15)
print(f'Foram cadastradas {len(lista)} pessoas')
for i, x in enumerate(lista):
    if i == 0:
        maior = x[:]
        menor = x[:]
    else:
        if maior[1] < x[1]:
            maior.clear()
            maior = x[:]
        elif maior[1] == x[1]:
            maior = maior[:]+x[:]
        if menor[1] > x[1]:
            menor.clear()
            menor = x[:]
        elif menor[1] == x[1]:
            menor = menor[:]+x[:]
QoL.Linha(15)
print(f'Os mais pesados são {maior[0::2]}, com {maior[1::2]} Kg')
print(f'Os mais leves são {menor[0::2]}, com {menor[1::2]} Kg')