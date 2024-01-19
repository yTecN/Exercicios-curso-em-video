def brush(cor='none'):
    """
    'none'
    'black'
    'red'
    'green'
    'yellow'
    'blue'
    'purple'
    'cyan'
    'white'
    """
    cores = {
        'none' : '\033[m',
        'black' : '\033[0;30;107m',
        'red' : '\033[0;31m',
        'green' : '\033[0;32m',
        'yellow' : '\033[0;33m',
        'blue' : '\033[0;34m',
        'purple' : '\033[0;35m',
        'cyan' : '\033[0;36m',
        'white' : '\033[0;97m'
    }
    return cores[cor]

def leiaint(msg=str):
    while True:
        try:
            n = int(input(msg))
        except (ValueError, TypeError):
            print(f'{brush('red')}ERRO! digite um número inteiro válido{brush()}')
            continue
        except KeyboardInterrupt:
            print(f'\n{brush('red')}O usuário preferiu não digitar um número{brush()}')
            return 3
        else:
            return n

def linha(tam=42):
    return '~'*tam


def cabeçalho(msg=str):
    print(linha())
    print(msg.center(42))
    print(linha())


def opc_menu(n, msg):
    print(f'{brush('yellow')}{n} {brush()}- {brush('blue')}{msg}')


def menu(lista=list):
    cabeçalho('MENU PRINCIPAL')
    for i, v in enumerate(lista, start=1):
        opc_menu(i, v)
    print(f'{brush()}{linha()}')
    opc = leiaint(f'{brush('yellow')}Sua opção: {brush()}')
    return opc

if __name__ == '__main__':
    menu(['Opc1', 'Opc2', 'Opc3'])