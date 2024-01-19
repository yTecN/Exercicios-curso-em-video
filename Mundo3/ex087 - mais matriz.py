import QoL
matrix = [
    [None,None,None],
    [None,None,None],
    [None,None,None]
]
SomarPares = SomaTerceiraCol = 0
for x in range(len(matrix)):
    for y in range(len(matrix)):
        matrix[x][y] = int(input(f'Digite o valor para [{x}, {y}] '))
        if matrix[x][y] % 2 == 0:
            SomarPares += matrix[x][y]
for m in matrix:
    for i in range(len(matrix)):
        print(f'[{m[i]:^5}]', end=' ')
    SomaTerceiraCol += m[-1]
    print()
maior = max(matrix[1])
QoL.Linha(15)
print(f'A soma dos valores pares é {SomarPares}.')
print(f'A soma dos valores da terceira coluna é {SomaTerceiraCol}.')
print(f'O maior valor da segunda linha é {maior}.')

