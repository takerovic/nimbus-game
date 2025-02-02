from pygame import *


class GameObject:
    def __init__(self):
        self.Size = (0, 0)
        self.Position = (0, 0)
        self.DisplayedPosition = (0, 0)
        self.Rectangle = Rect(0, 0, 0, 0)
        self.IgnoreDisplay = False

        self.Scene = 0
        pass

    def SetSize(self, size: (float, float)):
        self.Size = size

    def Draw(self, screen: surface, cam):
        self.Rectangle = Rect(self.DisplayedPosition[0], self.DisplayedPosition[1], self.Size[0], self.Size[1])

        if self != cam:
            if not self.IgnoreDisplay:
                self.DisplayedPosition = (self.Position[0] - cam.Position[0], self.Position[1] - cam.Position[1])
            else:
                self.DisplayedPosition = self.Position
        else:
            self.DisplayedPosition = (200, screen.get_height()/2)

        pass

    def Start(self):
        pass


class GameCamera(GameObject):
    def __init__(self):
        super().__init__()
        pass


class GameScene:
    def __init__(self):
        self.Objects = []
        self.Color = (255, 255, 255)
        self.Running = False

        self.Camera = GameObject()

    def AddGameObject(self, gobject: GameObject):
        self.Objects.append(gobject)
        gobject.Scene = self
        gobject.Start()

    def Start(self):
        for on in self.Objects:
            on.Start()

    def DrawScene(self, screen, cam: GameCamera):
        screen.fill(self.Color)
        for gameobject in self.Objects:
            gameobject.Draw(screen, cam)
