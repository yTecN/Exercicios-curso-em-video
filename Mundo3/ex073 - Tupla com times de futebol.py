times = ('Palmeira','Corinthians', 'Fluminence', 'Athletico', 'Flamengo',
         'Internacional', 'Atletico-MG','Bragaritto', 'Santas', 'América-MG',
         'São Paulo', 'Botafogo','Goiás', 'Ceará', 'Ceará-SC',
         'Curitiba','Avaí','Fortaleza', 'Cuíaba', 'Atlético', 'Juventude')
print(times[0:5], '5 Primeiros')
print('='*25)
print(times[-4:], ' 4 Últimos')
print('='*25)
print(sorted(times), 'Ordem alfabética')
print('='*25)
'''x = 0
while times[x] != 'Fluminence':
    x += 1'''
for x in range(0, len(times)):
    if times[x] == 'Fluminence':
        x += 1
        break
print(times[x], 'está na posição', x)
print('='*25)