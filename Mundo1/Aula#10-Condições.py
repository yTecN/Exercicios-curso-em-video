i = int(input('Quantos anos têm seu carro?'))
# primeira forma de usar if
if i <= 3:
    print('carro novo')
else:
    print('carro velho')
# segunda forma mais simples de usar if
print('carro novo' if i <= 3 else 'carro velho')
