class GameObject:
    def __init__(self):
        pass

    def Draw(self):
        pass


class GameScene:
    def __init__(self):
        self.Objects = []

    def DrawScene(self):
        for object in self.Objects:
            object.Draw()
