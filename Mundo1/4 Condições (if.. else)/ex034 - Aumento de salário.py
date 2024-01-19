s = float(input('Qual seu salário?: '))
if s >= 1250:
    ns = s + (s*0.1)
    print(f'Seu aumento será de 10%, passando de R${s} para R${ns}')
else:
    ns = s + (s*0.15)
    print(f'Seu aumento será de 15%, passando de R${s} para R${ns}')