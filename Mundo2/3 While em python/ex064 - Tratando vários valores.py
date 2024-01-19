# variaveis
cont = soma = 0
# código
num = int(input('Digite um número inteiro [999 para parar] '))
while num != 999:
    soma += num
    cont += 1
    num = int(input('Digite um número inteiro [999 para parar] '))
print(f'Você digiyou {cont} números e a soma deles é {soma}')
