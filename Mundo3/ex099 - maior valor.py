from time import sleep
def maior(*num):
    max = 0
    print('-='*30)
    print('Analisando os valores passados...')
    for v in num:
        if v > max:
            max = v
        print(v, end=' ', flush=True)
        sleep(0.3)
    print(f'Foram informados {len(num)} valores')
    print(f'O maior valor informado foi {max}')


maior(1,5,1,7,23)
maior()
maior(1)
