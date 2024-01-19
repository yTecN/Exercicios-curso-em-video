from utils.texto import brush


def leiaint(msg=str):
    while True:
        try:
            n = int(input(msg))
        except (ValueError, TypeError):
            print(f'{brush('red')}Erro! Digite um valor inteiro válido!{brush()}')
            continue
        except KeyboardInterrupt:
            print(f'\n{brush('red')}O usuário preferiu não digitar um valor{brush()}')
            return 0
        else:
            return n


def leiafloat(msg=str):
    while True:
        try:
            n = float(input(msg))
        except (ValueError, TypeError):
            print(f'{brush('red')}Erro! Digite um valor decimal válido!{brush()}')
            continue
        except KeyboardInterrupt:
            print(f'\n{brush('red')}O usuário preferiu não digitar um valor{brush()}')
            return float(0)
        else:
            return n

i = leiaint('DIgite um número inteiro: ')
f = leiafloat('Digite um número decimal: ')
print(f'O valor inteiro digitado foi {i} e o decimal foi {f}')