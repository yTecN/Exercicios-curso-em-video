from lib.interface import *


def arquivo_existe(file_name):
    try:
        file = open(file_name, encoding='utf-8')
        file.close()
    except FileNotFoundError:
        return False
    else:
        return True


def cria_arquivo(file_name):
    try:
        file = open(file_name, 'w', encoding='utf-8')
    except:
        print(f'Houve um erro na criação do arquivo')
    else:
        print(f'Arquivo criado com sucesso')
    file.close()

def leia_arquivo(file_name):
    pessoas = open(file_name, 'r', encoding='utf-8')
    cabeçalho('PESSOAS CADASTRADAS')
    for v in pessoas.readlines():
        v = v.replace('\n','').split(';')
        print(f' {v[0]:<31}{v[1]} anos')
    pessoas.close()


def gravar_arquivo(file_name):
    pessoas = open(file_name, 'a', encoding='utf-8')
    cabeçalho('Digite as informações')
    nome = input('Nome: ')
    idade = leiaint('Idade: ')
    pessoas.write(f'{nome};{idade}\n')
    pessoas.close()