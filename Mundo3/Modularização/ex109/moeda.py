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