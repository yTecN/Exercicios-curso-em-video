n1 = int(input('\033[1:35m Digite um número inteiro: '))
n2 = int(input('\033[1:35m Digite outro número inteiro: '))
if n1 > n2:
    print(f'\033[1:32m {n1} é maior que {n2}')
elif n1 < n2:
    print(f'\033[1:31m {n1} é menor que {n2}')
else:
    print(f'\033[1:33m {n1} e {n2} são o mesmo número')