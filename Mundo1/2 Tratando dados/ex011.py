alt = (input('Digite a altura da parede em metros: '))
lar = (input('Digite a largura da parede em metros: '))
if alt.isdecimal():
    area = int(alt) * int(lar)
    print(f'A área da parede é {area}')
    x = area/2
    print(f'serão necessários {x} litros de tinta para pintar essa parede')
else:
    area = float(alt) * float(lar)
    print(f'A área da parede é {area}')
    x = area/2
    print(f'Serão necessários {x} litros de tinta para pintara essa parede')

#  1 --- 2
#  X --- y