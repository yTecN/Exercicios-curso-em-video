print('-'*25)
print(f'{"CAIXA ELETRÕNICO":^27}')
print('-'*25)
tot50 = tot20 = tot10 = tot1 = 0
saque = int(input('Quanto você quer sacar? R$'))
ced = 50
tot = 0
while True:
    if saque >= ced:
        saque -= ced
        tot += 1
    else:
        if tot > 0:
            print(f'Total de {tot} cédulas de R${ced}')
        if ced == 50:
            ced = 20
        elif ced == 20:
            ced = 10
        elif ced == 10:
            ced = 1
        tot = 0
        if saque == 0:
            break
'''while True:
    if saque - 50 >= 0:
        tot50 += 1
        saque -= 50
    elif saque - 20 >= 0:
        tot20 += 1
        saque -= 20
    elif saque - 10 >= 0:
        tot10 += 1
        saque -= 10
    elif saque - 1 >= 0:
        tot1 += 1
        saque -= 1
    else:
        break
print(f'O total de notas de R$50.00 foi {tot50}')
print(f'O total de notas de R$20.00 foi {tot20}')
print(f'O total de notas de R$10.00 foi {tot10}')
print(f'O total de notas de R$1.00 foi {tot1}')'''
'''while saque - 50 >= 0:
    saque -= 50
    tot50 += 1
while saque - 20 >= 0:
    saque -= 20
    tot20 += 1
while saque - 10 >= 0:
    saque -= 10
    tot10 += 1
while saque - 1 >= 0:
    saque -= 1
    tot1 += 1
print(saque)

print('-'*25)
print(f'O total de notas de R$50.00 foi {tot50}')
print(f'O total de notas de R$20.00 foi {tot20}')
print(f'O total de notas de R$10.00 foi {tot10}')
print(f'O total de notas de R$1.00 foi {tot1}')'''