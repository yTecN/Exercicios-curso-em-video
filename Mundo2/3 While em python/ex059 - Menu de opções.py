from time import sleep
sep = '-=-' * 30
n1 = float(input('Primeiro valor: '))
n2 = float(input('Segundo valor: '))
print(sep)
while True:
    sleep(1)
    print(f"""[ 1 ] somar
[ 2 ] multiplicar
[ 3 ] maior
[ 4 ] novos números
[ 5 ] sair do programa
{sep}""")
    esc = input('>>>> Sua opção: ')
    if esc == '1':
        print(f'A soma entre {n1} e {n2} é: {n1+n2}')
        print(sep)
    elif esc == '2':
        print(f'O produto de {n1} x {n2} é: {n1*n2}')
        print(sep)
    elif esc == '3':
        if n1 > n2:
            print(f'{n1} é maior que {n2}')
        elif  n1 == n2:
            print(f'{n2} é igual à {n1}')
        else:
            print(f'{n2} é maior que {n1}')
        print(sep)
    elif esc == '4':
        n1 = float(input('Primerio valor: '))
        n2 = float(input('Segundo valor: '))
    elif esc == '5':
        break
    else:
        print('Opção inválida')
        print(sep)