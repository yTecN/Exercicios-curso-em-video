m1 = float(input('Digite sua primeira nota: '))
m2 = float(input('Digite a segunda nota: '))
if (m1 + m2) / 2 < 5.0:
    print('Reprovado')
elif 7 > (m1 + m2) / 2 >= 5.0:
    print('Recuperação')
else:
    print('Aprovado')