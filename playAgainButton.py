from button import Button
from sceneManager import SceneManager

from GameplayScene import GameplayScene


class PlayAgainButton(Button):
    def __init__(self, screen):
        super().__init__("end-sprite\\playagain.png")
        self.Position = (180, 500)
        self.Size = (125, 60)
        self.Screen = screen

    def OnMouseClick(self):
        SceneManager.SetScene(GameplayScene(screen=self.Screen))