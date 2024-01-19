n = int(input('Digite um número inteiro que você deseja saber o fatorial: '))
c = n
fat = 1
print(f'Calculando {n}! = ', end='')
while c > 0:
    print(c, end='')
    print(' x ' if c > 1 else ' = ', end='')
    fat *= c
    c -= 1
'''for x in range(1,n+1):
    fat *= x'''
print(fat)