import datetime
dados = {}
name = input('Nome: ')
birth_year = int(input('Ano de nascimento: '))
carteira_de_trabalho = int(input('Carteira de trabalho (0 não tem): '))

dados['nome'] = name
dados['idade'] = datetime.date.today().year - birth_year
dados['ctps'] = carteira_de_trabalho

if carteira_de_trabalho > 0:
    ano_contratação = int(input('Ano de contratação: '))
    salario = float(input('Salário: R$'))
    dados['contratação'] = ano_contratação
    dados['salário'] = salario
    dados['aposentadoria'] = ano_contratação + 35 - birth_year
for k, v in dados.items():
    print(f'- {k} tem o valor {v}')