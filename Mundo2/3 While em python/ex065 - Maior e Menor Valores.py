sep = '-' * 25
# variaveis
n = 'Ss'
cont = maior = soma = 0
# enfeite :p
print(sep)
print('Maior e Menor valores')
print(sep)
# código
while n in 'Ss':
    num = int(input('Digite um valor: '))
    cont += 1
    soma += num
    if cont == 1:
        maior = num
        menor = num
    else:
        if num > maior:
            maior = num
        if num < menor:
            menor = num
    n = input('Quer continuar? (S/N) ')
m = soma/cont
print(f'Você digitou {cont} números e a média foi {m:.2f}')
print(f'O maior valor digitado foi {maior} e o menor foi {menor}')
