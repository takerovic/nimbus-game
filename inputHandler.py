import threading

from gameEvent import GameEvent
from pygame import *
import pygame, sys


class InputHandler:
    KeyUpEvent = GameEvent()
    KeyDownEvent = GameEvent()

    @staticmethod
    def Run(events: list[event]):
        for game_event in events:
            if game_event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            else:
                def t():
                    if game_event.type == pygame.KEYDOWN:
                        InputHandler.KeyDownEvent.Fire(game_event.key)
                    elif game_event.type == pygame.KEYUP:
                        InputHandler.KeyUpEvent.Fire(game_event.key)

                threading.Thread(target=t).start()
