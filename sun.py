from sprite import Sprite

from animation import Animation

from nimbus import Nimbus
from sceneManager import SceneManager
from EndScene import EndScene
import time, threading


class Sun(Sprite):
    def __init__(self, screen):
        super().__init__("sun-sprite\\sun1.png")

        self.StaticAnimation = Animation()
        self.StaticAnimation.AddKeyPoint(1, "sun-sprite\\sun1.png")
        self.StaticAnimation.AddKeyPoint(1, "sun-sprite\\sun2.png")
        self.StaticAnimation.Looped = True

        self.GameplayTime = 0

        self.Screen = screen

    def Collision(self):
        nimbes: Nimbus = Nimbus.Singleton
        while self.Scene.Running:
            if nimbes.Rectangle.colliderect(self.Rectangle):
                SceneManager.SetScene(EndScene(self.Screen, self.GameplayTime))
            time.sleep(0.01)

    def Counter(self):
        while self.Scene.Running:
            self.GameplayTime += 1
            time.sleep(1)

    def Start(self):
        super().Start()
        threading.Thread(target=self.Collision).start()
        threading.Thread(target=self.Counter).start()
