# Int
n = int(input('Digite um número entre 0 e 9999: '))
u = n // 1 % 10
d = n // 10 % 10
c = n // 100 % 10
m = n // 1000 % 10
print(f"""
Unidade: {u}
Dezena: {d}
Centena: {c}
Milhar: {m}
""")

# String
num = int(input('Digite um número entre 0 e 9999: '))
n = str(num + 10000)
u = n[-1]
d = n[-2]
c = n[-3]
m = n[-4]
print(f"""
Unidade: {u}
Dezena: {d}
Centena: {c}
Milhar {m}""")