import pygame


class AnimationKeypoint:
    def __init__(self, duration: float, imagepath: str):
        self.Duration = duration
        self.Image = pygame.image.load(imagepath)


class Animation:
    def __init__(self):
        self.KeyPoints: [AnimationKeypoint] = []
        self.Looped = False

    def AddKeyPoint(self, duration: float, imagepath: str):
        self.KeyPoints.append(AnimationKeypoint(duration, imagepath))