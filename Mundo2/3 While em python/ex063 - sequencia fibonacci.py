# Enfeite :p
print('-'*25)
print('Sequência de Fibonacci')
print('-'*25)
# Variaveis
cont = 3
f1 = 0
f2 = 1
n = int(input('Digite quantos termos você quer exibir: '))
# Código
print('~'*25)
print(f'{f1} > {f2}', end='')
while cont <= n:
    fn = f1 + f2
    print(f' > {fn}', end='')
    f1 = f2
    f2 = fn
    cont += 1
print(' > FIM')
