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


def linha1(tam=1):
    print('-'*tam)


def linha2(tam=1):
    print('~'*tam)


def linha3(tam=1):
    print('-=')


def titulo1(msg=str):
    linha1(len(msg)+4)
    print(msg.center(len(msg)+4))
    linha1(len(msg)+4)

if __name__ == '__main__':
    titulo1('teste dessa porrakkkj')
    titulo1('piroca doce ou salgada?')
    titulo1('arroz é bom')
