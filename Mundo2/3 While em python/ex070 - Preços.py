print('-'* 25)
print(f"{'Mercado Bom Preço':^25}")
print('-'* 25)
totP = cont = maismil = 0
while True:
    cont += 1
    n = input('Nome do produto: ')
    p = float(input('Preço do produto: R$'))
    if p >= 1000:
        maismil += 1
    if cont == 1 or p < menor:
        menor = p
        pb = n
    totP += p
    c = input('Quer continuar? (S/N) ').strip().lower()[0]
    while c not in 'SsNn':
        print('Opção inválida')
        c = input('Quer continuar? (S/N) ').strip().lower()[0]
    if c in 'Nn':
        break
print(f'{maismil} produtos custaram mais de R$1000')
print(f'O nome do produto mais barato é {pb}')
print(f'A quantidade total gasta foi de R${totP}')
