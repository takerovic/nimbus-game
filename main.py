import sceneManager
from inputHandler import InputHandler
import pygame
from MenuScene import MenuScene

from sceneManager import SceneManager

pygame.init()
screen = pygame.display.set_mode((480, 640))
pygame.display.set_caption("NIMBUS")

SceneManager.SetScene(MenuScene(screen))


def OnQuit():
    SceneManager.CurrentScene.Running = False
    pass


InputHandler.QuitEvent.AddMethod(OnQuit)

while True:
    InputHandler.Run(pygame.event.get())
    SceneManager.CurrentScene.DrawScene(screen, SceneManager.CurrentScene.Camera)
    pygame.display.flip()
