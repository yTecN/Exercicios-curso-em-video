import requests

try:
    site = requests.get('https://pudim.com.br/')
except:
    print('O site está inacessível')
else:
    print(f'{"consegui acessar o site"}')
