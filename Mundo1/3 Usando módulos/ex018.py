import math
ang = float(input('Digite um ângulo: '))
print(f'O seno de {ang}° é: {math.sin(math.radians(ang)):.2f}\n'
      f'O coseno de {ang} é: {math.cos(math.radians(ang)):.2f}\n'
      f'A tangente de {ang} é: {math.tan(math.radians(ang)):.2f}')
