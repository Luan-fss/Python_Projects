
# For = Iterar Lists, tuple, dictionary, set, strings...

name = 'luan'
for letter in name: # Guardando na variável letter o nome iterado
    print(letter) # Print uma letra por vez

# list
name = ['Subscribe', 'to', 'Luan', 'Channel']
for letter in name:
    print(letter) # Print uma palavra por vez

# Loop dentro do Loop
adjs = ['shiny', 'purple', 'clear']
nouns = ['coin', 'speaker', 'iphone']

for adj in adjs:
    for noun in nouns:
        print(adj, noun) # = (shiny coin, shiny speaker...)
