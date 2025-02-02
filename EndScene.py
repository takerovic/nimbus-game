from gameObjects import GameScene

from text import TextLabel


class EndScene(GameScene):
    def __init__(self, screen, t: int):
        super().__init__()
        self.Color = (46, 139, 87)

        self.WinText = TextLabel()
        self.WinText.Position = (30, 0)
        self.WinText.SetText("YOU WON!")
        self.WinText.SetFont("Comic Sans MS", 40)

        self.TimeText = TextLabel()
        self.TimeText.Position = (30, 100)
        self.TimeText.SetText("YOUR TIME: " + str(t))
        self.TimeText.SetFont("Comic Sans MS", 40)

        self.BestTimeText = TextLabel()
        self.BestTimeText.Position = (30, 200)
        import os.path
        if os.path.isfile("record"):
            f = open("record", "r")
            if t < int(f.read()):
                f.close()
                f = open("record", "w")
                f.write(str(t))
                self.BestTimeText.SetText("BEST TIME: " + str(t))
            else:
                self.BestTimeText.SetText("BEST TIME: " + f.read())

            f.close()
        else:
            f = open("record", "w")
            f.write(str(t))
            f.close()
            self.BestTimeText.SetText("BEST TIME: " + str(t))

        self.BestTimeText.SetFont("Comic Sans MS", 40)

        self.AddGameObject(self.WinText)
        self.AddGameObject(self.TimeText)
        self.AddGameObject(self.BestTimeText)
