# Faça um programa que leia 5 valores numéricos e guarde-os em uma lista. No final, mostre qual foi o maior e o menor valor digitado e as suas respectivas posições na lista.
valores = []
posicao_maior = []
posicao_menor = []
for x in range(1, 6):
    numero = int(input(f'Digite o {x}° número: '))
    valores.append(numero)
for indice, numero in enumerate(valores):
    if numero == max(valores):
        posicao_maior.append(indice)
    if numero == min(valores):
        posicao_menor.append(indice)
print(f'Os valores digitados foram: {valores}')
print(f'O menor valor digitado foi {min(valores)}, na(s) posição(ões) {posicao_menor}')
print(f'O maior valor digitado foi {max(valores)}, na(s) posição(ões) {posicao_maior}')
