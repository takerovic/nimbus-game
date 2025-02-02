from gameObjects import GameScene

from sprite import Sprite
from playButton import PlayButton

import os
from text import TextLabel


class MenuScene(GameScene):
    def __init__(self, screen):
        super().__init__()
        self.Color = (46, 139, 87)

        self.Logo = Sprite("menu-sprites\\game logo.png")
        self.Logo.Position = (30, 0)
        self.Logo.Size = (400, 200)

        self.PlayButton = PlayButton(screen)

        self.AddGameObject(self.PlayButton)
        self.AddGameObject(self.Logo)

        print(os.path.exists("record"))
        if os.path.exists("record"):
            print("hi")
            self.BestTime = TextLabel()
            f = open("record", "r")
            self.BestTime.SetText("Best Time: " + f.read())
            self.BestTime.Position = (0, 600)

            self.AddGameObject(self.BestTime)