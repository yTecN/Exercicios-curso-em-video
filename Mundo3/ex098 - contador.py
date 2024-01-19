from time import sleep
import QoL
QoL.Linha(11)
def contador(i, f, p):
    if p == 0:
        p = 1
    elif p < 0:
        print(f'Contagem de {i} até {f}, de {p*-1} em {p*-1}')
        while i >= f:
            print(i, end=' ', flush=True)
            sleep(0.5)
            i += p
    else:
        print(f'Contagem de {i} até {f}, de {p} em {p}')
        while i <= f:
            print(i, end=' ', flush=True)
            sleep(0.5)
            i += p
    print('FIM!')
    QoL.Linha(11)


contador(1, 10, 1)
contador(10, 0, -2)
print('Agora é sua vez de personalizar a contagem!')
ini = int(input('Início: '))
fim =int(input('Fim: '))
pas =int(input('Passo: '))
QoL.Linha(11)
contador(ini, fim, pas)
