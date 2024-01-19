import QoL

def aumentar(p=0, t=0,form=False):
    return p*(t/100)+p if form == False else moeda(p*(t/100)+p)

def diminuir(p=0, t=0,form=False):
    return p-p*(t/100) if form is False else moeda(p-p*(t/100))

def dobra(p=0,form=False):
    return p*2 if form == False else moeda(p*2)

def metade(p=0,form=False):
    return p/2 if form is False else moeda(p/2)

def moeda(p=0, moeda='R$'):
    return f'{moeda}{p:.2f}'.replace('.',',')

def resumo(p=0, aum=10, dim=5):
    QoL.line1(35)
    print('RESUMO DO VALOR'.center(35))
    QoL.line1(35)
    print(f'Preço Analisado: \t{moeda(p)}')
    print(f'Dobro do preço: \t{dobra(p, True)}')
    print(f'Metade do Preço: \t{metade(p, True)}')
    print(f'{aum:0>2}% de aumento: \t{aumentar(p, aum, True)}')
    print(f'{dim:0>2}% de redução: \t{diminuir(p, dim, True)}')
    QoL.line1(35)