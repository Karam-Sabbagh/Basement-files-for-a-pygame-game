from Engine import Engine
from Engine import Images

import pygame

pygame.init()

screen = pygame.display.set_mode((600, 600))
pygame.display.set_caption('Window Name')

background_colour = (0, 0, 0)
screen.fill(background_colour)

# game setup here:

clock = pygame.time.Clock()

FPS = 60
running_game = True

while running_game:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running_game = False

    screen.fill(background_colour)

    # drawing here:

    pygame.display.update()
    clock.tick(FPS)
