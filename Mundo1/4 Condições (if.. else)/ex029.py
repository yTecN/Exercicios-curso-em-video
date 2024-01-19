km = float(input('O carro está a quantos quilômetros por hora?: '))
lim = float(80)
if km <= lim:
    print('Você não será multado')
else:
    kml = 7 * (km - lim)
    print(f'Você será multado em R${kml:.2f}!!')