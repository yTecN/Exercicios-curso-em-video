s = 0
c = 0
print('Digite 6 números inteiros')
for x in range(1,7):
    n = int(input(f'Digite o {x} número: '))
    if n % 2 == 0:
        s += n
        c += 1
print(f'Você digitou {c} números pares e a soma deles é: {s}')
