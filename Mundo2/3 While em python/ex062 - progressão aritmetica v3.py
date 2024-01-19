sep = '-=-' * 15
print(f'''{sep}
Gerador de Pa
{sep}''')
n = int(input('Primeiro termo: '))
r = int(input('Razão: '))
o = 10
cont = 0
tot = 0
while o != 0:
    tot += o
    while cont != tot:
        print(f'{n} > ', end='')
        n += r
        cont += 1
    print('Pausa')
    o = int(input('\nQuantos termos você quer a mais? '))
print(f'Foram mostrados {tot} termos')

