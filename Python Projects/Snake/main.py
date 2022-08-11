# Escopo = Create settings > Import here
# Create def main() for upgrade in screen and fixed window
# Create classes > draw > move... Pass all of them to Loop in class main()
import pygame, random
from settings import *
from pygame.math import Vector2

class Snake():
    COLOR = ((183,111,122))
    def __init__(self):
        self.body = [Vector2(5,10), Vector2(6,10), Vector2(7,10)]
        self.direction = Vector2(1,0)

    def draw_snake(self):
        # Vai checar todos o vetores do body da snake... Ex: {5,10}, {6,10}, {7,10}... E vai criar os rect nas devidas coordenadas
        for block in self.body:
            pygame.draw.rect(screen, self.COLOR,(block.x*CELL_SIZE, block.y*CELL_SIZE, CELL_SIZE, CELL_SIZE))

    def move_snake(self):    
        body_copy = self.body[:-1] 
        body_copy.insert(0,body_copy[0] + self.direction)
        self.body = body_copy[:]   

class Fruit():
    COLOR = ((122,166,114))
    def __init__(self):
        self.x = random.randint(0, CELL_NUMBER-1)
        self.y = random.randint(0, CELL_NUMBER-1)
        self.pos = pygame.math.Vector2(self.x, self.y)

    def draw_fruit(self):
        pygame.draw.rect(screen, self.COLOR, (int(self.pos.x*CELL_SIZE), int(self.pos.y*CELL_SIZE), CELL_SIZE, CELL_SIZE))

class Main():
    def __init__(self):
        self.snake = Snake()
        self.fruit = Fruit()
    
    def update(self):
        self.snake.move_snake()

    def draw_elemments(self):
        self.snake.draw_snake()
        self.fruit.draw_fruit()

main_game = Main()
SCREEN_UPDATE = pygame.USEREVENT        
pygame.time.set_timer(SCREEN_UPDATE, 150)

def main():
    run = True

    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                break
            # Timer in Loop
            if event.type == SCREEN_UPDATE:
                main_game.update()
            # Moves snake
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    main_game.snake.direction = (0, -1)
                if event.key == pygame.K_DOWN:
                    main_game.snake.direction = (0, 1)
                if event.key == pygame.K_LEFT:
                    main_game.snake.direction = (-1, 0)
                if event.key == pygame.K_RIGHT:
                    main_game.snake.direction = (1, 0)

        # Draw
        screen.fill((0,0,0))
        main_game.draw_elemments()

        # Setup DISPLAY
        pygame.display.update()
        clock.tick(FPS)


if __name__ == '__main__':
    main()