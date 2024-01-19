print('Digite o comprimento de cada reta: ')
r1 = float(input('Primeira: '))
r2 = float(input('Segunda: '))
r3 = float(input('Terceira: '))
if r1 < (r2 + r3) and r2 < (r1 + r3) and r3 < (r1 + r2):
    if r1 == r2 == r3:
        tipo = 'Equilátero'
    elif r1 != r2 != r3 != r1:
        tipo = 'Escaleno'
    else:
        tipo = 'Isósceles'
    print(f'Com essas retas é possível formar um triângulo {tipo}')
else:
    print('Não podemos formar um triângulos com essas retas')