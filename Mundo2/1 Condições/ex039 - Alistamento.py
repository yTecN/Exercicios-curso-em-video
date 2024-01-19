from datetime import date
hj = date.today()
sexo = input('Qual seu sexo? (F/M) ').strip().lower()
if sexo == 'f':
    print('Você não precisa se alistar')
if sexo == 'm':
    ano = int(input('Qual seu ano de nascimento? '))
    x = hj.year - ano
    if x < 18:
        print(f'Você é menor de idade ({x} anos)')
        print(f'Seu alistamento será no ano de {hj.year + (18 - (x))}')
    elif x > 18:
        print(f'Você têm {x} anos, passou-se {x - 18} anos do prazo')
    else:
        print('Está na hora do seu alistamento, você completou 18 anos')