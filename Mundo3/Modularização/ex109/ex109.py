import moeda


p = float(100)
print(f'dobro de {moeda.moeda(p)}: {moeda.dobra(p, form=True)}')
print()
print(f'metade de {moeda.moeda(p)}: {moeda.metade(p, form=True)}')
print()
print(f'aumento de 10% de {moeda.moeda(p)}: {moeda.aumentar(p, 10)}')
print()
print(f'diminuição de 13% de {moeda.moeda(p)}: {moeda.diminuir(p, 13)}')