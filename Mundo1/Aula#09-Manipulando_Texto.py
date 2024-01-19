
f = 'abobora com leite é ruim, eu acho'
print('012345678901234567890123456789012')
print(f)
print('-' * 20)
print('Len:')
print(' ' * 20)

print(len(f))

print('-' * 20)
print("""Caracteres de 0 à 7 e
de 0 à 7 pulando 1 casa:""")
print(' ' * 20)

print(f[:7])
print(f[:7:2])

# [1:2:3]  1 é onde começa, 2 é o final, e 3 é quantos caracteres vai pular

print('-' * 20)
print('Count(o): ')
print(' ' * 20)
print(f.count('o'))


print('-' * 20)
print('Find:')
print(' ' * 20)

print(f.find('leite'), '(encontrado)') # encontrado
print(f.find('awdgbawhjk'), '(não encontrado)') # não encontrado

print('-' * 20)
print('In:')
print(' ' * 20)

print('abobora' in f, '(está presente)')
print('manjericão' in f, '(não está presente)')

print('-' * 20)
print('replace:')
print(' ' * 20)

print(f, '->')
print(f.replace('abobora','arroz'))

print('-' * 20)
print('upper, lower, capitalize, title:')
print(' ' * 20)

print(f.upper(), '(TUDO MAIÚSCULO)') # tudo maiúsculo
print(f.lower(), '(tudo minúsculo)') # tudo minúsculo
print(f.capitalize(), '(Apenas a primeira letra maiúscula)') # apenas a primeira letra maiúscula
print(f.title(), '(Todas As Palavras Começando Com Letra Maiúscula)') # todas as palavras começando com letra maiúscula

print('-' * 20)
print('removendo espaços inuteis (strip):')
print(' ' * 20)

f2 = '     abrobawjdgawjkdhajlw    jamanta   '
print(f2) # normal
print(f2.strip(),' (todos os espaços)')
print(f2.rstrip(),' (todos os espaços à direita)')
print(f2.lstrip(),' (todos os espaços à esquerda)')

print('-' * 20)
print('Split:')
print(' ' * 20)

a = f.split()
print(a)

print('-' * 20)
print('Join:')
print(' ' * 20)

print('-'.join(a))
###################################################################################################################
