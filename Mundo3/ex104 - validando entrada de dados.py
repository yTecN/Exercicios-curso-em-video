def leiaint(msg):
    global n
    n = input(msg)
    if n.isnumeric():
        n = int(n)
    else:
        while not n.isnumeric():
            print('\033[0;31mERRO! Digite um número inteiro válido.\033[m')
            n = input(msg)
    return n


n = leiaint('Digite um número inteiro: ')
print(f'Você digitou o número {n}')