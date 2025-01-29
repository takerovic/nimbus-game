from pygame import surface
import pygame
from gameObjects import GameObject
import threading
from nimbus import Nimbus
import time


class Floor(GameObject):
    def __init__(self):
        super().__init__()
        threading.Thread(target=self.Collision).start()
        pass

    def Collision(self):
        while True:
            nimbes: Nimbus = Nimbus.Singleton
            if nimbes.Rectangle.colliderect(self.Rectangle):
                print("coll")
                nimbes.FreeFallValue = -2

            time.sleep(0.01)

    def Draw(self, screen: surface, cam):
        super().Draw(screen, cam)
        pygame.draw.rect(screen, (0,0,0), self.Rectangle)

