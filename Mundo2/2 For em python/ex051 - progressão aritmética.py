sep = '='
print(f"""\033[0:35m{sep*40}
Progressão artmética de 10 termos
{sep*40}""")
a1 = int(input('\033[0:33mDigite o primeiro termo: '))
r = int(input('Digite a razão: '))
for x in range(1, 11):
    print(f'\033[0:32m{a1}', end= ', ')
    a1 += r
print('Acabou')