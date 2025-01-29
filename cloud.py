import threading
import time

from pygame import surface

from sprite import Sprite
from nimbus import Nimbus


class Cloud(Sprite):
    def __init__(self):
        super().__init__("cloud-sprite\\cloud.png")
        self.Size = (100, 50)
        self.Position = (100, 100)

        threading.Thread(target=self.Collision).start()

    def Collision(self):
        nimbes: Nimbus = Nimbus.Singleton
        while True:
            if nimbes.Rectangle.colliderect(self.Rectangle):
                rect1 = self.Rectangle
                rect2 = nimbes.Rectangle
                dr = abs(rect1.right - rect2.left)
                dl = abs(rect1.left - rect2.right)
                db = abs(rect1.bottom - rect2.top)
                dt = abs(rect1.top - rect2.bottom)

                if min(dl, dr) > min(dt, db):
                    if db > dt:
                        nimbes.FreeFallValue = -2
                        self.Destroy()
            time.sleep(0.01)

    def Draw(self, screen: surface, cam):
        super().Draw(screen, cam)
