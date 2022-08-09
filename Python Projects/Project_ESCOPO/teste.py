import pygame, random
from pygame.math import Vector2
from settings import *
pygame.init()

class Snake:
    def __init__(self):
        self.body = [Vector2(5,10), Vector2(6,10), Vector2(7,10)]

    def draw(self):
        for block in self.body:
            pygame.draw.rect(screen, ((255,255,255)), (block.x * CELL_SIZE, block.y * CELL_SIZE, CELL_SIZE, CELL_SIZE))

class Fruit:
    def __init__(self):
        self.x = random.randint(0, CELL_NUMBER-1)
        self.y = random.randint(0, CELL_NUMBER-1)
        self.pos = Vector2(self.x, self.y)

    def draw(self):
        pygame.draw.rect(screen, ((255,255,255)), (self.pos.x * CELL_SIZE, self.pos.y * CELL_SIZE, CELL_SIZE, CELL_SIZE))

# Começo da def main
# 1 - Quero que a tela fique fixada
# 2 - Quero pintar a tela
# 3 - Criar objetos = Snake, Fruit
# 4 - Definir onde meus objetos vao ficar e largura.. altura > Utilizar Vetores
# 5 - Desenhar(draw), meus objetos 
# 6 - Passar para tela no laço

# 7 - Movimento por user ou automatico?

def main():
    run = True
    fruit = Fruit()
    snake = Snake()

    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                break

        screen.fill('Purple')
        fruit.draw()
        snake.draw()
        pygame.display.update()
        clock.tick(FPS)

if __name__ == '__main__':
    main()