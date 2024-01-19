import QoL
lista = []
dic= {}
listaM = []
listaAM = []
s = 0
while True:
    dic['nome'] = input('Nome: ')
    dic['sexo'] = input('Sexo [M/F]: ')[0].upper().strip()
    while dic['sexo'] not in 'MF':
        print('Erro! Digite apenas M ou F')
        dic['sexo'] = input('Sexo [M/F] ')[0].upper().strip()
    while True:
        try:
            dic['idade'] = int(input('Idade: '))
            break
        except:
            print('Tu é burro(a) ou o quê? idade é número não texto anta')
    lista.append(dic.copy())
    if dic['sexo'] == 'F':
        listaM.append(dic['nome'])
    dic.clear()
    continuar = input('Quer continuar? [S/N] ').strip().upper()[0]
    while continuar not in 'SN':
        print('Erro! Por favor digite apenas S ou N')
        continuar = input('Continuar? [S/N] ').strip().upper()[0]
    if continuar == 'N':
        break
QoL.Linha(15)
print(f'Foram cadastradas {len(lista)} pessoas')
for i in lista:
    s += i['idade']
media = s / len(lista)
print(f'A média de idade é: {media:.2f}')
print(f'As mulheres cadastradas foram: ', end=' ')
for i in listaM:
    print(i,end=', ')
print('\nPessoas com idade acima da média: ')
for i in lista:
    if i['idade'] > media:
        listaAM.append(i.copy())
for i in listaAM:
    print(f'nome == {i['nome']}, sexo == {i['sexo']}, idade == {i['idade']}')

# A) Quantas pessoas foram cadastradas v
# B) A média de idade v
# C) Uma lista com as mulheres v
# D) Uma lista de pessoas com idade acima da média v