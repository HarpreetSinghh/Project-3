import pygame
from pygame.locals import *

pygame.display.init()
screen = pygame.display.set_mode((800, 600))
img = pygame.image.load('coins.gif')

imgPos = pygame.Rect((0, 0), (0, 0))

LeftButton = 0
while 1:
    for e in pygame.event.get():
        if e.type == QUIT: exit(0)
        if e.type == MOUSEMOTION:
            if e.buttons[LeftButton]:
                # clicked and moving
                rel = e.rel
                imgPos.x += rel[0]
                imgPos.y += rel[1]
    screen.fill(0)
    screen.blit(img, imgPos)
    pygame.display.flip()
    pygame.time.delay(30)
