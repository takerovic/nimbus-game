class GameEvent:
    def __init__(self):
        self.HookedMethods = []

    def AddMethod(self, func):
        self.HookedMethods.append(func)

    def Fire(self, *arg):
        for method in self.HookedMethods:
            method(*arg)