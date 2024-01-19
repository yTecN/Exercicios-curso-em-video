print('Digite em Cm o comprimento de cada reta')
a = float(input('Primeira: '))
b = float(input('Segunda: '))
c = float(input('Terceira: '))
if a < b + c and b < a + c and c < b + a:
    print('Podemos formar um triângulo com essas retas')
else:
    print('Não podemos formar um triângulo com essas retas')