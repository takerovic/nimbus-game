import random
import threading
import time

from gameObjects import *
from sprite import Sprite
from animation import *
from pygame import *
from nimbus import Nimbus
from cloud import Cloud
from inputHandler import InputHandler
import pygame, sys, time

pygame.init()
screen = pygame.display.set_mode((480, 640))
pygame.display.set_caption("NIMBUS")

currentScene = GameScene()

nimbus_animation = Animation()
nimbus_animation.AddKeyPoint(5, "nimbus-sprite\\nimbus-jump.png")
nimbus_animation.AddKeyPoint(5, "nimbus-sprite\\nimbus-fall.png")

nimbes = Nimbus()

currentScene.AddGameObject(nimbes)

for i in range(0,100):
    cloud = Cloud()
    currentScene.AddGameObject(cloud)
    cloud.Position = (random.randint(0,480), random.uniform(1000, -5000))

currentCamera = nimbes

while True:
    InputHandler.Run(pygame.event.get())
    currentScene.DrawScene(screen, currentCamera)
    pygame.display.flip()
