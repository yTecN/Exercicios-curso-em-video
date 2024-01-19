from unidecode import unidecode
n = input('Digite seu nome completo: ').strip().lower()
n = unidecode(n)
print(f"""
A letra A aparece {n.count('a')} Vezes
A primeira vez que a letra A apareceu foi na posição {n.find('a') + 1}
A ultima vez que a letra A apareceu foi na posição {n.rfind('a') + 1}
""")
