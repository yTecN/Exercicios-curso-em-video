import moeda


p = float(100)
print(f'dobro de {p}: {moeda.dobra(p)}')
print()
print(f'metade de {p}: {moeda.metade(p)}')
print()
print(f'aumento de 10% de {p}: {moeda.aumentar(p, 10)}')
print()
print(f'diminuição de 13% de {p}: {moeda.diminuir(p, 13)}')