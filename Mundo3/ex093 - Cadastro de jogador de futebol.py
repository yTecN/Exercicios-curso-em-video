import QoL
dados = {}
dados['nome'] =  input('Nome do jogador: ')
dados['gols'] = []
dados['total'] = 0
num_partidas = int(input(f'Quantas partidas {dados["nome"]} jogou? '))
for i in range(1, num_partidas+1):
    gol = int(input(f'  Quantos gols na partida {i}? '))
    dados['total'] += gol
    dados['gols'].append(gol)
QoL.Linha(25)
print(dados)
QoL.Linha(25)
for k, v in dados.items():
    print(f'O campo {k} tem o valor {v}')
QoL.Linha(25)
print(f'O jogador {dados["nome"]} jogou {num_partidas} partidas.')
for i, v in enumerate(dados['gols']):
    print(f'    => Na {i+1}° partida, fez {v} gols')
print(f'Um total de {dados["total"]} gols')