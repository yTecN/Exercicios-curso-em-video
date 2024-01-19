# Exercício Python 56: Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas. No final do programa, mostre:
# a média de idade do grupo, qual é o nome do homem mais velho e quantas mulheres têm menos de 20 anos.
maior = 0
mul = 0
mi = 0
nhv = ''
for x in range(1, 5):
    n = input(f'Digite o nome da {x}° pessoa: ').strip().capitalize()
    s = input(f'Digite o sexo dessa pessoa (F/M): ').strip().lower()
    i = int(input(f'Digite a idade dessa pessoa: '))
    mi += i
    if x == 1 and s == 'm':
        maior = i
        nhv = n
    if s == 'm' and i > maior:
        maior = i
        nhv = n
    if s == 'f':
        if i < 20:
            mul += 1
m = mi / 4
print(f'A média da idade das pessoas do grupo {m}')
print(f'O nome do homem mais velho do grupo é {nhv}, com {maior} anos')
print(f'A quantidade de mulheres com menos de 20 anos é {mul}')