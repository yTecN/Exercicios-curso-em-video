sep = '-=-' * 15
print(f'''{sep}
Progressão aritmética de 10 termos
{sep}''')
a1 = int(input('Primeiro termo: '))
r = int(input('Razão: '))
x = 0
while x != 10:
    print(f'{a1} > ', end='')
    a1 += r
    x += 1
print('Acabou')