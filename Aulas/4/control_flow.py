
# Break = Stop the loop before finish all itens
word_list = ['Subscribe', 'to', 'Luan', 'Channel']
for name in word_list:
    print(name)
    if name == 'Luan':
        break # Só vai printar até o "Luan"
print ('The end') # Quando acabar: Break ou final do laço

# Continue = Pula o print daquela condição e continua o código
word_list = ['Subscribe', 'to', 'Luan', 'Channel']
for name in word_list:
    if name == 'Luan':
        continue # Vai pular o print "Luan"
    print(name)
print ('The end') # Quando acabar: Break ou final do laço

