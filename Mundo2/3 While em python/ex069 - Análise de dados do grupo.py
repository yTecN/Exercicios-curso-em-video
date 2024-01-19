sep = '-'*25
#var
Maior18 = H = Menor20 = 0
#código
print(sep) 
print('   CADASTRE UMA PESSOA')
print(sep)
while True:
    i = int(input('Idade: '))
    s = input('Seco: [Masculino/Feminino] ').strip().lower()[0]
    while not s in 'MmFf':
        print('Opção inválida')
        s = input('Seco: [Masculino/Feminino] ').strip().lower()[0]
    if s in 'Mm':
        H += 1
    if i >= 18:
        Maior18 += 1
    if s in 'Ff' and i < 20:
        Menor20 += 1
    opc = input('Quer continuar? ').strip().lower()[0]
    while not opc in 'SsNn':
        print('Opção inválida')
        opc = input('Quer continuar? [S/N] ')
    if opc == 'n':
        break
print(f'{H} Homens foram cadastrados')
print(f'{Maior18} Pessoas com mais de 18 anos foram cadastradas')
print(f'{Menor20} Mulheres com menos de 20 anos foram cadastradas')