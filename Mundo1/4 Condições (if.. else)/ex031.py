dis = float(input('Qual a distância da viagem em Km?: '))
if dis <= 200:
    preco = 0.50 * dis
    print(f'O custo da viagem será de {preco} (R$0.50 por Km)')
else:
    preco = 0.45 * dis
    print(f'O custo da viagem será de {preco} (R$0.45 por Km)')
