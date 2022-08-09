
def exec():
    # Palavras
    boy_name = input('Nome de menino: ')
    type_of_dinosaur = input('Um dinossauro: ')
    animal = input('Um animal: ')
    body_part = input('Uma parte do corpo: ')
    color = input('Uma cor: ')
    if color[-1] == 'o':
        color = color[0:-1]
        color += 'a'
    number = input('Um número: ')
    game = input('Nome de um jogo: ')
    emotion = input('Uma emoção: ')

    # Texto
    madlib = (f'{boy_name} é um {type_of_dinosaur}. Ele anda ao redor da selva com um amigo. \
    o amigo é bom em caçar {animal}, e tem um(a) {body_part} assutador. Ele mora \
    em uma caverna {color}, e tem {number} amigos que joga {game}, \
    com ele. Ele é um dinossauro muito {emotion}')

    print(madlib)
exec()