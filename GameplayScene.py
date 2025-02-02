import random

from gameObjects import GameScene
from nimbus import Nimbus
from floor import Floor
from cloud import Cloud
from sun import Sun

from text import TextLabel

from gameTime import GameTime

import os
import pygame


class GameplayScene(GameScene):
    def __init__(self, screen: pygame.Surface):
        super().__init__()
        self.Player = Nimbus()
        self.AddGameObject(self.Player)

        self.Color = (135, 206, 235)

        self.Camera = self.Player
        self.Floor = Floor()
        self.Floor.Size = (screen.get_width() * 10, 10000)
        self.Floor.Position = (screen.get_width() * -5, 500)
        self.Floor.Color = (86, 125, 70)

        self.Player.Position = (0, 0)

        self.AddGameObject(self.Floor)

        self.Sun = Sun(screen)
        for i in range(-100, 5):
            new_cloud = Cloud()
            new_cloud.Position = (random.uniform(-250, 250), i * 100)
            self.AddGameObject(new_cloud)

        self.Sun.Position = (0, -10000)
        self.Sun.Size = (250, 250)
        self.AddGameObject(self.Sun)

        self.GameTime = GameTime()
        self.AddGameObject(self.GameTime)


