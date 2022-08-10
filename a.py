import pygame, random
from pygame.math import Vector2

# Criado movimento da Snake
# Colocado tempo para esse movimento nao ser feito rapido no loop = Criar um timer
# Colocada class Main para organização ...
class Snake:
    COLOR = ((255,255,255))
    def __init__(self):
        self.body = [Vector2(1,10), Vector2(2,10), Vector2(3,10)]
        self.direction = Vector2(1,0)

    def draw_snake(self):
        for block in self.body:
            pygame.draw.rect(screen, self.COLOR, (block.x * CELL_SIZE, block.y * CELL_SIZE, CELL_SIZE, CELL_SIZE))

    def move_snake(self):
        body_copy = self.body[:-1]
        body_copy.insert(0, body_copy[0] + self.direction)
        self.body = body_copy[:]
        print(self.body)

class Fruit:
    COLOR = ((255,0,0))
    def __init__(self):
        self.x = random.randint(0, CELL_NUMBER - 1)
        self.y = random.randint(0, CELL_NUMBER - 1)
        self.pos = Vector2(self.x, self.y)

    def draw_fruit(self):
        pygame.draw.rect(screen, self.COLOR, (self.pos.x*CELL_SIZE, self.pos.y*CELL_SIZE, CELL_SIZE, CELL_SIZE))

class Main:
    def __init__(self):
        self.snake = Snake()
        self.fruit = Fruit()

    def update(self):
        self.snake.move_snake()

    def draw_elemments(self):
        self.snake.draw_snake()
        self.fruit.draw_fruit()
        
pygame.init()
CELL_NUMBER = 20
CELL_SIZE = 40
WIDTH, HEIGHT = CELL_NUMBER*CELL_SIZE, CELL_NUMBER*CELL_SIZE
FPS = 60
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Snake')
clock = pygame.time.Clock()
# Adicionar TIMER em um evento costumizado
SCREEN_UPDATE = pygame.USEREVENT # Criando um event custom pra adicionar ao Loop
pygame.time.set_timer(SCREEN_UPDATE, 150)

main_game = Main()

def main():
    run = True

    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                break
            # Timer
            if event.type == SCREEN_UPDATE:
                main_game.update()
            # Keys to control snake
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
        screen.fill((0,0,0))
        main_game.draw_elemments()
        # Setup DISPLAY
        pygame.display.update()
        clock.tick(FPS)

if __name__ == '__main__':
    main()