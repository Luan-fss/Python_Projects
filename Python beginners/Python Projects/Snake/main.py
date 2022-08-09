# Escopo = Create settings > Import here
# Create def main() for upgrade in screen and fixed window
# Create classes > draw > move... Pass all of them to Loop in main()
import pygame, random
from settings import *
from pygame.math import Vector2


class Snake():
    COLOR = ((183,111,122))
    def __init__(self):
        self.body = [Vector2(5,10), Vector2(6,10), Vector2(7,10)]
        self.direction = Vector2(1,0)

    def draw(self):
        # Vai checar todos o vetores do body da snake... Ex: {5,10}, {6,10}, {7,10}... E vai criar os rect nas devidas coordenadas
        for block in self.body:
            pygame.draw.rect(screen, self.COLOR,(block.x*CELL_SIZE, block.y*CELL_SIZE, CELL_SIZE, CELL_SIZE))

    def move(self):            ########################
        body_copy = self.body[:-1] 
        body_copy.insert(0,body_copy[0] + self.direction)
        self.body = body_copy[:]

SCREEN_UPDATE = pygame.USEREVENT              #################
pygame.time.set_timer(SCREEN_UPDATE, 150)         ######################

class Fruit():
    COLOR = ((122,166,114))
    def __init__(self):
        self.x = random.randint(0, CELL_NUMBER-1)
        self.y = random.randint(0, CELL_NUMBER-1)
        self.pos = pygame.math.Vector2(self.x, self.y)

    def draw(self):
        pygame.draw.rect(screen, self.COLOR, (int(self.pos.x*CELL_SIZE), int(self.pos.y*CELL_SIZE), CELL_SIZE, CELL_SIZE))

def main():
    run = True

    fruit = Fruit()
    snake = Snake()

    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                break
            if event.type == SCREEN_UPDATE:  ################
                snake.move()    ##############

        # Updates
        screen.fill((175,215,70))
        fruit.draw()
        snake.draw()
        pygame.display.update()
        clock.tick(FPS)

if __name__ == '__main__':
    main()