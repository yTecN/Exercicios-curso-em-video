n1 = int(input('Digite um número inteiro: '))
print('''
Escolha uma opção para a conversão:
[ 1 ] Binário
[ 2 ] Octal
{ 3 } Hexadecimal
''')
opc = input('Sua escolha: ')
if opc == '1':
    print(f'{n1} em Binário é igual à {bin(n1)[2:]}')
elif opc == '2':
    print(f'{n1} em Octal é igual à {oct(n1)[2:]}')
elif opc == '3':
    print(f'{n1} em Hexadecimal é igual à {hex(n1)[2:]}')
else:
    print('Opção inválida')