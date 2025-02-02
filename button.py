from sprite import Sprite


class Button(Sprite):
    def __init__(self, img):
        super().__init__(img)

    def OnMouseClick(self):
        print("click")

