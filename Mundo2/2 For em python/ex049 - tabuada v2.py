n = int(input('Digite um valor inteiro: '))
print('-=-' * 10)
for x in range(1, 11):
    print(f'{n} * {x:0>2} = {x * n}')
print('-=-' * 10)