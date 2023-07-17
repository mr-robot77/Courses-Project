import pygame

from math import pi

pygame.init()

screen = pygame.display.set_mode((800, 600))

red = (255, 0, 0)

blue = (0, 0, 255)

green = (0, 255, 0)

gray = (128, 128, 128)

screen.fill(gray)

pygame.draw.circle(screen, green, (200, 200), 20)

pygame.display.update()

while True:

    pygame.event.pump()