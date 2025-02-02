from gameObjects import GameScene


class SceneManager:
    CurrentScene = GameScene()

    @staticmethod
    def SetScene(scene: GameScene):
        SceneManager.CurrentScene.Running = False
        SceneManager.CurrentScene = scene
        SceneManager.CurrentScene.Running = True
        SceneManager.CurrentScene.Start()
