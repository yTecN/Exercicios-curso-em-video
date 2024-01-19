valores = [[], []]

for i in range(1,8):
    valor = int(input(f'Digite o {i}° valor: '))
    if valor % 2 == 0:
        if i == 1 or len(valores[0]) == 0:
            if len(valores[0]) == 0:
                valores[0].append(valor)
            elif valor >= valores[0][-1]:
                valores[0].append(valor)
        else:
            pos = 0
            while pos < len(valores[0]):
                if valor <= valores[0][pos]:
                    valores[0].insert(pos, valor)
                    break
                pos += 1
    else:
        if i == 1 or len(valores[1]) == 0:
            if len(valores[1]) == 0:
                valores[1].append(valor)
            elif valor >= valores[1][-1]:
                valores[1].append(valor)
        else:
            pos = 0
            while pos < len(valores[1]):
                if valor <= valores[1][pos]:
                    valores[1].insert(pos, valor)
                    break
                pos += 1

print(f'Valores pares: {valores[0]}')
print(f'Valores ímpares: {valores[1]}')
