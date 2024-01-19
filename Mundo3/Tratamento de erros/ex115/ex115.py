from lib.interface import * # importa bibliotecas criadas para o funcionamento deste programa
from lib.arquivo import *   # ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

nome_arquivo = 'pessoas.txt' # nome do arquivo para facilitar na digitação do código

if not arquivo_existe(nome_arquivo): # Verifica se o arquivo existe, se não, cria um arquivo com o nome "pessoas.txt"
    cria_arquivo(nome_arquivo)

while True:
    resposta = menu(['Ver pessoas cadastradas', 'Cadastrar uma nova pessoa', 'Sair do programa']) # Exibe o menu e retorna a opção desejada pelo usuário
    if resposta == 1: # Lista as pessoas cadastradas
        leia_arquivo(nome_arquivo)
    elif resposta == 2: # Cadastra uma pessoa
        gravar_arquivo(nome_arquivo) 
    elif resposta == 3: # Finaliza o programa
        cabeçalho('Finalizando programa...') 
        break
    else:
        print(f'{brush('red')}ERRO! Por favor digite uma opção válida{brush()}') # Erro caso o usuário digite algo errado

