import pygame

pygame.init()
CELL_NUMBER = 20
CELL_SIZE = 40
FPS = 60
screen = pygame.display.set_mode((CELL_NUMBER*CELL_SIZE, CELL_SIZE*CELL_NUMBER))
pygame.display.set_caption('Snake')
clock = pygame.time.Clock()
