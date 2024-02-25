numeros = (
    int(input('Primeiro valor: ')),
    int(input('Segundo valor: ')),
    int(input('Terceiro valor: ')),
    int(input('Quarto valor: '))
)

print('~'*45)
print(f'Foram digitados {numeros.count(9)} números 9' if 9 in numeros else 'Não foi digitado nenhum número 9')
print(f'O número 3 aparece pela primeira vez na posição {numeros.index(3)+1}' if 3 in numeros else 'O número 3 não foi digitado')
print('Os números pares digitados foram: ', end='')
for i in numeros:
    if i % 2 == 0:
        print(i, end=' ')
print('\n'+'~'*45)