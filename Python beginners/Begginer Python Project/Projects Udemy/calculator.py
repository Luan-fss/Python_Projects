
def contas(x, y):
    x = int(x)
    y = int(y)
    operador = input('Digite um operador: ')
    # Calculo
    if operador == '+':
        calculo = x + y
        print(f'O resultado dessa conta é = {calculo}')
    elif operador == '-':
        calculo = x - y
        print(f'O resultado dessa conta é = {calculo}')
    elif operador == '/':
        calculo = x / y
        print(f'O resultado dessa conta é = {calculo:.2f}')
    elif operador == '*':
        calculo = x * y
        print(f'O resultado dessa conta é = {calculo}')
    else:
        print('Insira um operador válido: + - * /')

# Entradas do user
x = input('Digite um número: ')
y = input('Digite um número: ')
if x.isdigit() and y.isdigit():
    contas(x = x, y = y)
else:
    print('Inserir apenas números')