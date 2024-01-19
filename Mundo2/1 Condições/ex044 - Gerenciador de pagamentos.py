p = float(input('Qual o preço do produto² R$'))
print("""
Formas de pagamento:
dinheiro/cheque: 10% de desconto (1)
cartão: 5% de desconto (2)
2x no cartão: preço formal (3)
3x ou mais no cartão: 20% de juros (4)
""")
e = int(input('Sua escolha: '))
if e == 1:
    pag = p - (p * (10/100))
elif  e == 2:
    pag = p - (p * (5/100))
elif e == 3:
    pag = p
else:
    pag = p + (p * (20/100))
print(f'Você pagará R${pag}')