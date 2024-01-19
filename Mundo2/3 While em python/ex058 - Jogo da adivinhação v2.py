from random import randint
num = randint(0, 10)
palpites = 0
print('Pensei em um número entre 0 e 10, tente adinha-lo')
p = -1
while p != num:
    p = int(input('Qual é seu palpite? '))
    palpites += 1
    if p < num and p >= 0:
        print('Mais... Tente Novamente ')
    if p > num:
        print('Menos... Tente Novamente ')
    if p > 10 or p < 0:
        print('Mermão, é entre 0 e 10, tu é burro(a)?')
        palpites -= 1
print(f'Parabéns, você acertou com {palpites} tentativas')
