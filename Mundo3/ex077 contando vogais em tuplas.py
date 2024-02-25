tupla = ('arroz', 'batata', 'caminhao', 'aeroporto', 'helicoptero', 'gauchotrix')

print('~'*25)
for pal in tupla:
    print(f'Palavra: {pal}')
    print(f'Vogais: ', end='')
    for letra in pal:
        if letra in 'aeiou':
            print(letra, end=' ')
    print('\n'+'~'*25)