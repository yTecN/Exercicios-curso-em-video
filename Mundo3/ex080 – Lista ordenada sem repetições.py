valores = []
for x in range(5):
    numero = int(input(f'Digite o {x+1}° valor: '))
    if x == 0 or numero > valores[-1]:
        valores.append(numero)
        print('adicionado ao final da lista')
    else:
        posicao = 0
        while posicao < len(valores):
            if numero <= valores[posicao]:
                valores.insert(posicao, numero)
                if posicao == 0:
                    print('adicionado ao começo da lista')
                else:
                    print('adicionado no meio da lista')
                break
            posicao += 1
print(valores)