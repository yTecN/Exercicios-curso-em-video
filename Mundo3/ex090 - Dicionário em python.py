dict = {
    'nome': input('Nome: '),
    'media': float(input('Média: '))
    }
if dict['media'] >= 7:
    situacao = 'aprovado'
elif dict['media'] < 5:
    situacao = 'burro pra krl'
elif dict['media'] < 7:
    situacao = 'recuperação'
print(f'''--------------------------------------
- nome: {dict["nome"]}
- média: {dict["media"]}
- situação: {situacao}
''')

