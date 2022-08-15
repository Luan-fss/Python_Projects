import pygame, random
from pygame.math import Vector2

CELL_NUMBER, CELL_SIZE = 20, 40
SCREEN = pygame.display.set_mode((CELL_NUMBER * CELL_SIZE, CELL_NUMBER * CELL_SIZE))
NOME_JOGO = pygame.display.set_caption('Snake')
FPS = 60

class Snake:
    def __init__(self):
        self.body = [Vector2(5,10), Vector2(4,10), Vector2(3,10)]
        self.direction = Vector2(1,0)
        self.new_block = False

    def draw(self):
        for block in self.body:
            pygame.draw.rect(SCREEN, (0,255,255), (block.x * CELL_SIZE, block.y * CELL_SIZE, CELL_SIZE, CELL_SIZE))
    
    def move(self):
        if self.new_block == True:
            body_copy = self.body[:]
            body_copy.insert(0, body_copy[0] + self.direction)
            self.body = body_copy
            self.new_block = False
        else:
            body_copy = self.body[:-1]
            body_copy.insert(0, body_copy[0] + self.direction)
            self.body = body_copy

    def add_block(self):
        self.new_block = True

class Fruit:
    def __init__(self):
        self.x = random.randint(0, CELL_NUMBER - 1)
        self.y = random.randint(0, CELL_NUMBER - 1)
        self.pos = Vector2(self.x, self.y)

    def draw(self):
        pygame.draw.rect(SCREEN, (255,0,0), (self.pos.x * CELL_SIZE, self.pos.y * CELL_SIZE, CELL_SIZE, CELL_SIZE))

    def reposition(self):
        self.x = random.randint(0, CELL_NUMBER - 1)
        self.y = random.randint(0, CELL_NUMBER - 1)
        self.pos = Vector2(self.x, self.y)

class Main:
    def __init__(self):
        self.snake = Snake()
        self.fruit = Fruit()

    def update(self):
        self.snake.move()
        self.colissions()
        self.check_fail()

    def draw_elemments(self):
        self.fruit.draw()
        self.snake.draw()

    def colissions(self):
        if self.snake.body[0] == self.fruit.pos:
            self.fruit.reposition()
            self.snake.add_block()
            
    def check_fail(self):
        # Nao pode ser 0 nem maior que 19
        if not 0 <= self.snake.body[0].x < CELL_NUMBER or not 0 <= self.snake.body[0].y < CELL_NUMBER:
            self.game_over()

        for block in self.snake.body[1:]:
            if block == self.snake.body[0]:
                self.game_over()

    def game_over(self):
        pygame.quit()
        self.run = False

SCREEN_UPDATE = pygame.USEREVENT
pygame.time.set_timer(SCREEN_UPDATE, 150)

def main():
    run = True
    clock = pygame.time.Clock()
    main_game = Main()
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                break
            if event.type == SCREEN_UPDATE:
                main_game.update()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    main_game.snake.direction = (0,-1)
                if event.key == pygame.K_DOWN:
                    main_game.snake.direction = (0,1)
                if event.key == pygame.K_LEFT:
                    main_game.snake.direction = (-1,0)
                if event.key == pygame.K_RIGHT:               
                    main_game.snake.direction = (1,0)
                
                print (main_game.snake.direction)

        #Screen updates
        SCREEN.fill('Black')
        main_game.draw_elemments()

        #Setup
        pygame.display.update()
        clock.tick(FPS)

if __name__ == '__main__':
    main()