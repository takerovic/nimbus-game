import threading
import time

import pygame.image
from animation import Animation
from inputHandler import InputHandler
from sprite import Sprite


class Nimbus(Sprite):
    def __init__(self):
        super().__init__("nimbus-sprite\\nimbus-fall.png")
        JumpAnim = Animation()
        JumpAnim.AddKeyPoint(0.1, "nimbus-sprite\\nimbus-jump.png")
        JumpAnim.Looped = True
        self.JumpingAnimation = JumpAnim
        self.Size = (100, 100)
        self.DefaultImage = self.Image
        self.DisplayedPosition = (300, 320)

        InputHandler.KeyDownEvent.AddMethod(self.OnKeyDown)
        InputHandler.KeyUpEvent.AddMethod(self.OnKeyUp)

        self.Arrows = {
            "left": False,
            "right": False,
        }

        self.MovementValue = 0

        self.FreeFallValue = 0
        self.Gravity = 1
        Nimbus.Singleton = self

    def OnKeyDown(self, key):
        if key == pygame.K_LEFT:
            self.Arrows["left"] = True
        elif key == pygame.K_RIGHT:
            self.Arrows["right"] = True

    def OnKeyUp(self, key):
        if key == pygame.K_LEFT:
            self.Arrows["left"] = False
        elif key == pygame.K_RIGHT:
            self.Arrows["right"] = False

    def MovementLoop(self):
        while self.Scene.Running:
            if self.Arrows["left"]:
                self.MovementValue -= 1/50
            elif self.Arrows["right"]:
                self.MovementValue += 1/50
            self.FreeFallValue += 1/50
            self.Position = (self.Position[0] + self.MovementValue, self.Position[1] + self.FreeFallValue)

            if self.FreeFallValue >= 0:
                self.Image = self.JumpingAnimation.KeyPoints[0].Image
            else:
                self.Image = self.DefaultImage
            time.sleep(0.0035)

    def StartJump(self):
        self.PlayAnimation(self.JumpingAnimation)

    def StopJump(self):
        self.StopAnimation()

    def Start(self):
        super().Start()
        threading.Thread(target=self.MovementLoop).start()