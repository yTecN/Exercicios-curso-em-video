from time import sleep
c = (
    '\033[m',
    '\033[0;30;40m', # Preto
    '\033[0;30;41m', # Vermelho
    '\033[0;30;42m', # Verde
    '\033[0;30;43m', # Amarelo
    '\033[0;30;44m', # Azul
    '\033[0;30;45m', # Magenta
    '\033[0;30;46m', # Azul claro
    '\033[0;30;47m', # Cinza
    '\033[7;30;m'     # Branco
)

def ajuda(com):
    titulo(f'Acessando o manual do comando \'{com}\'', 2)
    print(c[0], end='')
    help(com)
    print(c[0], end='')
    sleep(2)

def titulo(txt, cor=0):
    print(c[cor], end='')
    print('-'*(len(txt)+4))
    print(f'  {txt}  ')
    print('-'*(len(txt)+4))
    print(c[0], end='')
    sleep(1)


# programa principal
msg = ''
titulo('sistema interactive help pinton', 3)
while msg.upper() != 'FIM':
    msg = input('Função ou biblioteca: ')
    ajuda(msg)