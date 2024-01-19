#  Crie um programa que gerencie o aproveitamento de um jogador de futebol.
#  O programa vai ler o nome do jogador e quantas partidas ele jogou.
#  Depois vai ler a quantidade de gols feitos em cada partida.
#  No final, tudo isso será guardado em um dicionário, incluindo o total de gols feitos durante o campeonato.
import QoL
lista = []
while True:
    info = {}
    info['jogador'] = input('Nome do jogador: ')
    info['gols'] = []
    info['tot_gols'] = 0
    for c in range(int(input('Quantas partidas ele jogou? '))):
        gols = int(input(f'Quantos gols ele fez na partida {c+1}? '))
        info['gols'].append(gols)
        info['tot_gols'] += gols
    lista.append(info.copy())
    continuar = input('Quer continuar? [S/N] ')[0].upper().strip()
    while continuar not in 'SN':
        continuar = input('Erro! Tente novamente [S/N] ')[0].upper().strip()
    if continuar == 'N':
        break

# placar
print(f'{"ind":<4}{"NOME":<10}{"GOLS":<10}{"TOTAL"}')
for i, d in enumerate(lista):
    print(f'{i:^3}{d['jogador']:<10}  {d['gols']}{d['tot_gols']:>10}')
# info
while True:
    ind = int(input('Exibir dados de qual jogador? (999 para parar) '))
    while ind > len(lista)-1 or ind < 0:
        if ind == 999:
           break
        print(f'Erro! Não existe jogador com o número {ind}')
        ind = int(input('Exibir dados de qual jogador? (999 para parar) '))
    print(f'-- LEVANTAMENTO DO JOGADOR {lista[ind]['jogador']}:')
    for i, v in enumerate(lista[ind]['gols']):
        print(f'   No jogo {i+1} fez {v} gols.')
    if ind == 999:
        break
