import time

# Banco/Base de dados
login_bd = 'luanjogo'
senha_bd = 'luan123'

# Login em função
def login(x, y):
    if x == login_bd and y == senha_bd:
        print('Logado com sucesso')
        print('Aguarde um pouco...')
        time.sleep(2)
        print('Ok... Loading...')
        time.sleep(1)
        print('...')
        time.sleep(1)
        print('...')
        time.sleep(2)
        print('Ok credenciais confirmadas.')
    elif x != login_bd and y == senha_bd:
        print('Login está incorreto')
    elif x == login_bd and y != senha_bd:
        print('Senha está incorreto')
    else:
        print('Por favor verifique os campos...')
login (x = input('Digite seu nome de usúario: '), y = input('Digite sua senha: '))