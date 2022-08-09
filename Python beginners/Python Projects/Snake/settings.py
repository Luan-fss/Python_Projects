import pygame
pygame.init()

# Resolution
CELL_NUMBER = 20
CELL_SIZE = 40
# Set FPS
FPS = 60
clock = pygame.time.Clock()
# Set Display and Name 
screen = pygame.display.set_mode((CELL_NUMBER*CELL_SIZE, CELL_NUMBER*CELL_SIZE))
pygame.display.set_caption('Snake')
