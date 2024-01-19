from math import sqrt, pow
cato = float(input('Digite o comprimento do cateto oposto: '))
cata = float(input('Digite o comprimento do cateto adjacente: '))
hip = sqrt(pow(cato, 2) + pow(cata, 2))
print(f'O comprimento da hipotenusa é: {hip:.3f}')
print('O comprimento da hipotenusa é: {:.3f}'.format(hip))