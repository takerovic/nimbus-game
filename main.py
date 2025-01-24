import pygame, sys
import game-obj

pygame.init()
screen = pygame.display.set_mode((640, 480))
pygame.display.set_caption("NIMBUS")

currentScene =

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
