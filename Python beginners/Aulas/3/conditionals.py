# IF ELIF ELSE

x = int(input('Digite um número qualquer: '))

if x > 5: # Condição 1 - True or False
    x += 2
elif x == 4: # Condição 2 se 1 for false
    x += 4
elif x < 4: # Condição 3 se 2 for false
    x += 3
else:      # Condição se for tudo false
    x += 1

print (x)