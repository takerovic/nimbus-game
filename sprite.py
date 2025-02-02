import pygame.image
import threading
from gameObjects import *
from pygame import *
from animation import Animation, AnimationKeypoint
import time


class Sprite(GameObject):
    Sprites = []

    def __init__(self, texturepath: str):
        super().__init__()

        self.Image = pygame.image.load(texturepath)

        self.PlayingAnimation = False
        Sprite.Sprites.append(self)


    def PlayAnimation(self, anim: Animation):
        def KeypointPlaythrough():
            oldimage = self.Image
            self.PlayingAnimation = True
            if anim.Looped:
                while self.PlayingAnimation and self.Scene.Running:
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
        screen.blit(self.Image, self.DisplayedPosition)

        super().Draw(screen, cam)

    def Destroy(self):
        self.Position = (-10000, -10000)

    def OnMouseClick(self):
        pass

