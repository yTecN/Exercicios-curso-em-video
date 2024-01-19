import QoL
matrix = [
    [None,None,None],
    [None,None,None],
    [None,None,None]
]
for i1 in range(len(matrix)):
    for i2 in range(len(matrix[i1])):
            matrix[i1][i2] = int(input(f'Digite um valor para [{i1},{i2}]'))
QoL.Linha(10)
for m in matrix:
    for i3 in range(len(m)):
        print(f'[{m[i3]:^5}]', end=' ')
    print()

