from datetime import date
hj = date.today().year
ano = int(input('Qual o ano de nascimento do atleta? '))
idade = hj - ano
print(f'O atleta têm {idade} anos.')
if idade <=9:
    print('Atleta MIRIM')
elif idade <= 14:
    print('Atleta INFANTIL')
elif idade <= 19:
    print('Atleta JUNIOR')
elif idade <= 25:
    print('Atleta SENIOR')
else:
    print('Atleta MASTER')