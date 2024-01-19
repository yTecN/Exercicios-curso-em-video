s = input('Inforce seu sexo: ').strip().upper()[0]
while not s in 'FM':
    s = input('Dados inválidos! Por favor, informe seu sexo: ').strip().upper()[0]
print(f'Sexo {s} registrado com sucesso')