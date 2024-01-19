val = float(input('Qual o valor da casa?: R$'))
sal = float(input('Qual o seu salário?: R$'))
anos = int(input('Em quantos anos você vai pagar?: '))
meses = anos*12
prest = val / meses
if prest > (sal*(30/100)):
    print('Empréstimo negado, o valor da prestação mensal é superior à 30% do seu salário')
else:
    print('Empréstimo autorizado')