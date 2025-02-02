import random
import threading
import time

from pygame import surface

from sprite import Sprite
from nimbus import Nimbus

from animation import Animation


class Cloud(Sprite):
    def __init__(self):
        super().__init__("cloud-sprite\\cloud1.png")
        self.Size = (100, 50)
        self.Position = (100, 100)

        self.StaticAnimation = Animation()
        self.StaticAnimation.AddKeyPoint(1, "cloud-sprite\\cloud1.png")
        self.StaticAnimation.AddKeyPoint(1, "cloud-sprite\\cloud2.png")
        self.StaticAnimation.Looped = True

        def playAnim():
            time.sleep(random.uniform(0.1, 2))
            self.PlayAnimation(self.StaticAnimation)

        threading.Thread(target=playAnim).start()

    def Collision(self):
        nimbes: Nimbus = Nimbus.Singleton
        while self.Scene.Running:
            if nimbes.Rectangle.colliderect(self.Rectangle):
                rect1 = self.Rectangle
                rect2 = nimbes.Rectangle
                dr = abs(rect1.right - rect2.left)
                dl = abs(rect1.left - rect2.right)
                db = abs(rect1.bottom - rect2.top)
                dt = abs(rect1.top - rect2.bottom)

                if min(dl, dr) > min(dt, db):
                    if db > dt:
                        nimbes.FreeFallValue = -3
                        self.Destroy()
            time.sleep(0.01)

    def Draw(self, screen: surface, cam):
        super().Draw(screen, cam)

    def Destroy(self):
        old_pos = self.Position
        self.Position = (10000, 100000)

        def posthread():
            time.sleep(3)
            self.Position = old_pos

        threading.Thread(target=posthread).start()

    def Start(self):
        super().Start()
        threading.Thread(target=self.Collision).start()
