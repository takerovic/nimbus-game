from pygame import surface, font

from gameObjects import  GameObject


class TextLabel(GameObject):
    def __init__(self):
        super().__init__()
        self.Text = ""
        self.Font = font.SysFont('Comic Sans MS', 30)
        self.Color = (0, 0, 0)
        self.TextObject = self.Font.render(self.Text, False, self.Color)

    def UpdateText(self):
        self.TextObject = self.Font.render(self.Text, False, self.Color)

    def SetText(self, txt: str):
        self.Text = txt
        self.UpdateText()

    def SetFont(self, fontname: str, size: int):
        self.Font = font.SysFont(fontname, size)
        self.UpdateText()

    def SetColor(self, color):
        self.Color = color
        self.UpdateText()

    def Draw(self, screen: surface, cam):
        super().Draw(screen, cam)

        screen.blit(self.TextObject, self.Position)