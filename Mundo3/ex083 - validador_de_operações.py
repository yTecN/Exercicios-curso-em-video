op = input('Digite a expressão: ')
stack = list()

for char in op:
    if char == '(':
        stack.append('(')
    elif char == ')':
        if len(stack) > 0:
            stack.pop()
        else:
            break
if len(stack) == 0:
    print('expressão válida')
else:
    print('q porra ce fez')