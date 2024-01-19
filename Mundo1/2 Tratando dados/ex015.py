# 01 -- 0.15
# 13 --  x
# x = 13 * 0.15

# 01 --- 60
# 13 --- x
# x = 13*60

km = float(input('Quantos quilômetros você andou?: KM '))
day = int(input('Quantos dias ficou alugado?: '))
kmp = km * 0.15
dayp = day * 60
ptotal = kmp + dayp
print(f'O preço total a pagar é R$ {ptotal:.2f}\n'
      f'Sendo R$ {dayp} dos dias alugados;\n'
      f'e R$ {kmp} dos quilômetros rodados')