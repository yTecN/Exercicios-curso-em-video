while True:
    nums = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze', 'doze', 'treze', 'catorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte',)
    num = int(input('Digite um número entre 0 e 20: '))
    while not num in range(0, 21):
        num = int(input('Tente novamente, digite um número entre 0 e 20: '))
    print(f'Você digitou o número {nums[num]}')
    continuar = input('Quer continuar? ')
    if continuar == 'n':
        break









'NOTA: MODIFICAR O PROGRAMA PARA RODAR ATÉ QUE O USUÁRIO NÃO QUEIRA MAIS'