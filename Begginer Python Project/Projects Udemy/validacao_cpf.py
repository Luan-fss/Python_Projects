
cpf = input('Qual é o seu CPF: ')
new_cpf = cpf[:-2]
total = 0

reverse = 10
# Listando do 10 ao 2 para multiplicação e do 11 ao 2
for i in range(19):
    if not cpf.isdigit():
        print('Só é possivel inserir números')
        break
        if i > 8:
            i -= 9

    # Somando no total a multiplicação de cada linha e acumulando
        total += int(new_cpf[i]) * reverse

    # Utilizado para a multiplicação
        reverse -= 1 # Colocando Loop
        if reverse < 2: # Quando chegar na multiplicação de 2... Reseta o total e o reverse (Multiplicador) vai pra 11
            reverse = 11
            d = 11 - (total % 11) # Calculo dos digitos

            if d > 9: # Se o Digito for maior que 9 = Final 0, se não, utiliza-se o próprio número
                d = 0
            total = 0
            new_cpf += str(d) # Soma ao novo cpf um digito para saber se é verdadeiro

if cpf == new_cpf:
    print('Válido')
else:
    print('Este CPF é inválido')

"""
def cpf(x):
    new_cpf = x[:-2]
    total = 0

    reverse = 10
    # Listando do 10 ao 2 para multiplicação e do 11 ao 2
    for i in range(19):
        if not x.isdigit():
            print('Só é possivel inserir números')
            break
            if i > 8:
                i -= 9

        # Somando no total a multiplicação de cada linha e acumulando
            total += int(new_x[i]) * reverse

        # Utilizado para a multiplicação
            reverse -= 1 # Colocando Loop
            if reverse < 2: # Quando chegar na multiplicação de 2... Reseta o total e o reverse (Multiplicador) vai pra 11
                reverse = 11
                d = 11 - (total % 11) # Calculo dos digitos

                if d > 9: # Se o Digito for maior que 9 = Final 0, se não, utiliza-se o próprio número
                    d = 0
                total = 0
                new_cpf += str(d) # Soma ao novo cpf um digito para saber se é verdadeiro
    print (x)
    print(new_cpf)
    if x == new_cpf:
        print('Válido')
    else:
        print('Este CPF é inválido')

cpf (x = input('Qual é o seu CPF: '))

"""