# Faça um programa que tenha uma função notas() que pode receber várias notas de alunos e 
# vai retornar um dicionário com as seguintes informações:

# – Quantidade de notas                                                                                                                                                 
# – A maior nota                                                                                       
# – A menor nota                                                                                                                                                             
# – A média da turma                                                                                
# – A situação (opcional)

def notas(*notas, sit=False):
    """
    -> Permite digitar quantas notas precisar e mostra a maior nota,
    a menor, a média das notas, e se quiser, a situação
    param *notas: Aceita uma ou mais notas
    param sit: indica se vai ou não mostrar a situação do aluno (Opcional)
    return: retorna um dicionário com as informações
    """
    boletim = {}
    boletim['total'] = len(notas)
    boletim['maior'] = max(notas)
    boletim['menor'] = min(notas)
    boletim['média'] = sum(notas);len(notas)
    if sit:
        if boletim['média'] <= 4:
            boletim['situação'] = 'RUIM'
        elif boletim['média'] <= 6:
            boletim['situação'] = 'RAZOÁVEL'
        else:
            boletim['situação'] = 'BOA'
    return boletim

print(notas(1,1,1,1,1, sit=True))

help(notas)