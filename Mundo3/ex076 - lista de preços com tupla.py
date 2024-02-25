# Crie um programa que tenha uma tupla única com nomes de produtos e seus respectivos preços, na sequência. No final, mostre uma listagem de preços, organizando os dados em forma tabular.

itens = ('Lápis', 1.75, 'Borracha', 2, 'Caderno', 15.9, 'Estojo', 25)

print('~'*32)
print('             Preços')
print('~'*32)
for i in range(0, len(itens), 2):
    print(f'{itens[i]:.<23}R${itens[i+1]:>7.2f}')
print('~'*32)

''' VVVVV Outra maneira de fazer VVVVV'''
# for i in range(len(itens)):
#     if i % 2 == 0:
#         print(f'{itens[i]:.<23}R$', end='')
#     else:
#         print(f'{itens[i]:>7.2f}')  


