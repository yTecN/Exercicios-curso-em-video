from random import randint
import QoL

def sorteia(lst):
    for i in range(5):
        lst.append(randint(0, 10))
    print('Os números sorteados foram: ', end='')
    for v in lst:
        print(v, end=' ')
    print('Fim')

def somaPar(lst):
    s = 0
    for v in lst:
        if v % 2 == 0:
            s += v
    print(f'A soma dos valores pares dessa lista é {s}')


QoL.Titulo('Sorteio e soma')
lista = []
sorteia(lista)
somaPar(lista)
