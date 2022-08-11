from tkinter.tix import CELL
import pygame, random
from pygame.math import Vector2

pygame.init()
#Abrir a window / Configuração inicial
CELL_NUMBER = 20
CELL_SIZE = 40
SCREEN = pygame.display.set_mode((CELL_NUMBER*CELL_SIZE, CELL_NUMBER*CELL_SIZE))
NOME = pygame.display.set_caption('Snake')
FPS = 60

class Fruit():
    COLOR = ((0,255,255))
    def __init__(self):
        self.x = random.randint(0, CELL_NUMBER-1)
        self.y = random.randint(0, CELL_NUMBER-1)
        self.pos = Vector2(self.x, self.y)

    def draw(self):
        pygame.draw.rect(SCREEN, self.COLOR, (self.pos.x*CELL_SIZE, self.pos.y*CELL_SIZE, CELL_SIZE, CELL_SIZE))

class Snake():
    COLOR = ((255,0,0))
    def __init__(self):
        self.body = [Vector2(2,10), Vector2(3,10), Vector2(4,10)]
        self.direction = Vector2(1,0)

    def draw(self):
        for block in self.body:
            pygame.draw.rect(SCREEN, self.COLOR, (block.x*CELL_SIZE, block.y*CELL_SIZE, CELL_SIZE, CELL_SIZE))

    def movement(self):
        body_copy = self.body[:-1]
        body_copy.insert(0, body_copy[0] + self.direction)
        self.body = body_copy

class Main():
    def __init__(self):
        self.snake = Snake()
        self.fruit = Fruit()

    def update(self):
        self.snake.movement()

    def draw_elemments(self):
        self.snake.draw()
        self.fruit.draw()

SCREEN_UPDATE = pygame.USEREVENT
pygame.time.set_timer(SCREEN_UPDATE, 150)

main_game = Main()
def main():
    run = True
    clock = pygame.time.Clock()
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                break
            # Update frames of snake
            if event.type == SCREEN_UPDATE:
                main_game.update()
            # Control Snake
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    main_game.snake.direction = Vector2(0,-1)
                if event.key == pygame.K_DOWN:
                    main_game.snake.direction = Vector2(0,1)
                if event.key == pygame.K_LEFT:
                    main_game.snake.direction = Vector2(-1,0)     
                if event.key == pygame.K_RIGHT:
                    main_game.snake.direction = Vector2(1,0)  
                              
        # Draw
        SCREEN.fill((0,0,0))
        main_game.draw_elemments()

        # Setup display
        pygame.display.update()
        clock.tick(FPS)

if __name__ == '__main__':
    main()