sep = '-' * 25
# código
while True:
    print(sep)
    num = int(input('Digite um valor inteiro: '))
    print(sep)
    if num < 0:
        break
    for x in range(1, 11):
        print(f'{num} x {x} = {num*x}')
