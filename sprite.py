import pygame.image
import threading
from gameObjects import *
from pygame import *
from animation import Animation, AnimationKeypoint
import time


class Sprite(GameObject):
    def __init__(self, texturepath: str):
        super().__init__()

        self.Image = pygame.image.load(texturepath)

        self.PlayingAnimation = False

    def PlayAnimation(self, anim: Animation):
        def KeypointPlaythrough():
            oldimage = self.Image
            self.PlayingAnimation = True
            if anim.Looped:
                while self.PlayingAnimation:
                    for kp in anim.KeyPoints:
                        Keypoint: AnimationKeypoint = kp
                        self.Image = Keypoint.Image
                        time.sleep(Keypoint.Duration)
            else:
                for kp in anim.KeyPoints:
                    Keypoint: AnimationKeypoint = kp
                    self.Image = Keypoint.Image
                    time.sleep(Keypoint.Duration)

            self.PlayingAnimation = False
            self.Image = oldimage

        threading.Thread(target=KeypointPlaythrough).start()

    def StopAnimation(self):
        self.PlayingAnimation = False

    def Draw(self, screen: surface, cam: GameCamera):
        self.Image = pygame.transform.scale(self.Image, self.Size)
        if not cam == self:
            self.DisplayedPosition = (self.Position[0], (self.Position[1] - cam.Position[1]))
            screen.blit(self.Image, self.DisplayedPosition)
        else:
            self.DisplayedPosition = self.Position
            screen.blit(self.Image, self.Position)

        super().Draw(screen, cam)

    def Destroy(self):
        self.Position = (-10000, -10000)

