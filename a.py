import pygame
from pygame.math import Vector2

pygame.init()
CELL_NUMBER = 20
CELL_SIZE = 40
FPS = 60
screen = pygame.display.set_mode((CELL_NUMBER*CELL_SIZE, CELL_SIZE*CELL_NUMBER))
pygame.display.set_caption('TESTE')
clock = pygame.time.Clock()


class Quad_opponent:
    COLOR = ('red')
    def __init__(self):
        self.x = 1
        self.y = 1
        self.pos = Vector2(self.x, self.y)

    def draw(self):
        pygame.draw.rect(screen, self.COLOR, (self.pos.x * CELL_SIZE, self.pos.y * CELL_SIZE, CELL_SIZE, CELL_SIZE))

class Quad_player:
    COLOR = ('blue')
    def __init__(self):
        self.x = CELL_NUMBER - 2
        self.y = CELL_NUMBER - 2
        self.pos = Vector2(self.x, self.y)

    def draw(self):
        pygame.draw.rect(screen, self.COLOR, (self.pos.x * CELL_SIZE, self.pos.y * CELL_SIZE, CELL_SIZE, CELL_SIZE))

def main():
    run = True
    quad_player = Quad_player()
    quad_opponent = Quad_opponent()

    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                break

        screen.fill('Black')
        quad_player.draw()
        quad_opponent.draw()
        pygame.draw.rect(screen, ('White'), (0 ,17*CELL_SIZE-5, 800, 5))
        pygame.draw.rect(screen, ('White'), (0 ,3*CELL_SIZE, 800, 5))
        pygame.draw.aaline(screen,(255,0,0), (0, 17*CELL_SIZE-5), (800, 3*CELL_SIZE+3), blend=1)

        pygame.display.update()
        clock.tick(FPS)

if __name__ == '__main__':
    main()
