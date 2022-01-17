from Engine import *
import pygame

pygame.init()

screen = pygame.display.set_mode((600, 600))
pygame.display.set_caption('Window Name')

background_colour = (0, 0, 0)
screen.fill(background_colour)

# game setup here:

clock = pygame.time.Clock()
start_tick = pygame.time.get_ticks()
pause_seconds = 0
seconds = 0

FPS = 60
running_game = True

while running_game:
    if seconds > 0:
        seconds_changed = ((((pygame.time.get_ticks() - start_tick) / 1000) - last_seconds) - pause_seconds)
        seconds += seconds_changed
    else:
        seconds = (pygame.time.get_ticks() - start_tick) / 1000

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running_game = False

    screen.fill(background_colour)

    # drawing here:

    pygame.display.update()
    clock.tick(FPS)

    last_seconds = seconds
