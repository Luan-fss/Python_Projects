

# Padrão de inicialização
class Beach:
        def __init__(self, location, water_color, temperature): # Adicionar variáveis/atributos aos parametros 
            self.location = location # instance variable
            self.water_color = water_color
            self.heat_rating = 'hot' if temperature > 38 else 'cool'
            self.parts = ['sand', 'water'] # class variable [List]

                # Adding a method in a class
        def add_part(self, part): 
            self.parts.append(part) # append() = adiciona um item a lista (sand e water)

def main():
    # Definindo as variáveis das funções
    praia_peruibe = Beach('Peruibe', 'Blue', 40) # Set variables in other def
    praia_itanhaem = Beach('Itanhaem', 'Dark blue', 37) # Set variables in def
    praia_itanhaem.add_part('rock') # Adicionando uma word na lista 
    la_beach = Beach('LA', 'Turquoise', 42)
    italy_beach = Beach('Italy', 'Crystal blue', 25)
    italy_beach.add_part('rock')
    hot_not_rocky = []
    for beach in [praia_peruibe, praia_itanhaem, la_beach, italy_beach]:
        if beach.heat_rating == 'hot' and 'rock' not in beach.parts: # > 38 graus and não tiver 'rock'
            hot_not_rocky.append(beach)

    return hot_not_rocky

# N entendi
if __name__ == '__main__': # ?
    beaches = main() # Certo
    print([beach.location for beach in beaches]) # ?




