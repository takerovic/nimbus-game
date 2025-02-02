from pygame import surface
import pygame
from gameObjects import GameObject
import threading
from nimbus import Nimbus
import time


class Floor(GameObject):
    def __init__(self):
        super().__init__()
        self.Color = (0, 0, 0)
        pass

    def Collision(self):
        while self.Scene.Running:
            nimbes: Nimbus = Nimbus.Singleton
            if nimbes.Rectangle.colliderect(self.Rectangle):
                nimbes.FreeFallValue = -3

            time.sleep(0.01)

    def Draw(self, screen: surface, cam):
        super().Draw(screen, cam)
        pygame.draw.rect(screen, self.Color, self.Rectangle)

    def Start(self):
        super().Start()
        threading.Thread(target=self.Collision).start()

