import moeda


p = float(100)
print(f'dobro de {moeda.moeda(p)}: {moeda.moeda(moeda.dobra(p))}')
print()
print(f'metade de {moeda.moeda(p)}: {moeda.moeda(moeda.metade(p))}')
print()
print(f'aumento de 10% de {moeda.moeda(p)}: {moeda.moeda(moeda.aumentar(p, 10))}')
print()
print(f'diminuição de 13% de {moeda.moeda(p)}: {moeda.moeda(moeda.diminuir(p, 13))}')