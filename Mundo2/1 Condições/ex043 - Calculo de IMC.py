kg = float(input('Qual o peso da pessoa em kilos² '))
alt = float(input('Qual a altura da pessoa em metros? '))
imc = kg / alt ** 2
print(f'O IMC dessa pessoa é {imc:.1f}')
if imc < 18.5:
    print('Abaixo do peso')
elif 18.5 <= imc < 25:
    print('Peso Ideal')
elif 25 <= imc < 30:
    print('Sobrepeso')
elif 30 <= imc < 40:
    print('Obesidade')
else:
    print('Obesidade Morbida')