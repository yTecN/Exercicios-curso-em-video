numeros = []
while True:
    numero = int(input('Digite um número: '))
    if numero not in numeros:
        numeros.append(numero)
        print('Valor adicionado...')
    else:
        print('Esse número já foi digitadom, portanto não será adicionado...')
    resposta = input('Continuar? [S/N] ')[0].lower()
    while resposta not in 'sn':
        print('tente novamente')
        resposta = input('Continuar? [S/N] ')[0].lower()
    if resposta == 's':
        continue
    else:
        break
print(f'Os valores digitados foram: {sorted(numeros)}')