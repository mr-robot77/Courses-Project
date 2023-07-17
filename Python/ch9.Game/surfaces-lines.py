import pygame

from math import pi

pygame.init()

screen = pygame.display.set_mode((800, 600))

red = (255, 0, 0)

blue = (0, 0, 255)

green = (0, 255, 0)

gray = (128, 128, 128)

screen.fill(gray)

pygame.draw.lines(screen, green, True, [(700, 200), (600, 200), (550, 150), (650, 140)])

pygame.draw.lines(screen, green, False, [(700, 350), (600, 350), (550, 300), (650, 290)])

pygame.display.update()

while True:

    pygame.event.pump()