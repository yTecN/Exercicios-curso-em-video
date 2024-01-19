def leiadinheiro(msg=str):
    while True:
        p = input(msg).strip().replace(',','.')
        if p.replace('.','', 1).isdigit():
            return float(p)
            break
        else:
            print(f'Erro! \'{p}\' não é um valor válido!')

if __name__ == '__main__':
    print(leiadinheiro('Digite um valor: R$'))