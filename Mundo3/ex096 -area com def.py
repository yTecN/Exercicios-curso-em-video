import QoL
def area(b, h):
    area = b * h
    print(f'A área do terreno {b}m x {h}m é de {area}m².')


QoL.Titulo('Controle do Terreno')
area(float(input('LARGURA (m): ')), float(input('COMPRIMENTO (m): ')))
