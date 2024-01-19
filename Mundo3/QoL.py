def Linha(n):
    """
    -> Faz uma linha do tamanho desejado
    """
    print('-=-'*n)

def Titulo(txt):
    """
    -> Faz um título adaptável ao tamanho do texto
    """
    print('-=-'*len(txt))
    print(' '*int(len(txt))+txt)
    print('-=-'*len(txt))

def Cor(cor):
    Cores = (
        '\033[0;30m', # Preto
        '\033[0;31m', # Vermelho
        '\033[0;32m', # Verde
        '\033[0;33m', # Amarelo
        '\033[0;34m', # Azul
        '\033[0;35m', # Magenta
        '\033[0;36m', # Azul claro
        '\033[0;37m', # Cinza
        '\033[0;97m'  # Branco
    )
    return Cores[cor]