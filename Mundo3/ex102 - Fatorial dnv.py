# Crie um programa que tenha uma função fatorial() que receba dois parâmetros: 
# o primeiro que indique o número a calcular e outro chamado show, que será um 
# valor lógico (opcional) indicando se será mostrado ou não na tela o processo de cálculo do fatorial.
def fatorial(num, show=False):
    """
    -> Calcula o fatorial de um número.
    param num: Número a ser calculado
    param show: Mostra ou não a conta (Opcional)
    return: Retorna o valor do fatorial do número num
    """
    print('-'*30)
    fat = 1
    for n in range(num, 0, -1):
        if show:
            print(n, end=' ')
            print('x'if n > 1 else '=', end=' ')
        fat *= n
    return fat
        

print((fatorial(30)))
print()
