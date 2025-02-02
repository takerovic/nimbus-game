import threading
import time

from pygame import surface

from text import  TextLabel


class GameTime(TextLabel):
    def __init__(self):
        super().__init__()
        self.Text = "0"
        self.SetFont('Comic Sans MS', 20)

        self.IgnoreDisplay = True

        self.GameplayTime = 0

    def Counter(self):
        while self.Scene.Running:
            self.GameplayTime += 1
            self.Text = str(self.GameplayTime)
            self.UpdateText()
            print(self.DisplayedPosition)
            time.sleep(1)

    def Start(self):
        super().Start()
        threading.Thread(target=self.Counter).start()
