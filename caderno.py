import pygame
pygame.init()

### Set a timer to object ###
SCREEN_UPDATE = pygame.USEREVENT
pygame.time.set_timer(SCREEN_UPDATE, 150)
# No laço
if event.type == SCREEN_UPDATE:
    main_game.update() # Move do objeto



### Types of control objects ###
# Quando pressionado, move para tal direção, se soltado ele para
keys = pygame.key.get_pressed()
if keys [pygame.K_UP]:
    # Conditions to move

############################################################################################################################################################################
