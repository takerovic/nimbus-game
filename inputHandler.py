import threading
from gameEvent import GameEvent
from pygame import *
import pygame, sys

from sprite import Sprite


class InputHandler:
    KeyUpEvent = GameEvent()
    KeyDownEvent = GameEvent()

    QuitEvent = GameEvent()

    @staticmethod
    def Run(events: list[event]):
        for game_event in events:
            if game_event.type == pygame.QUIT:
                InputHandler.QuitEvent.Fire()

                pygame.quit()
                sys.exit()
            else:
                def t():
                    if game_event.type == pygame.KEYDOWN:
                        InputHandler.KeyDownEvent.Fire(game_event.key)
                    elif game_event.type == pygame.KEYUP:
                        InputHandler.KeyUpEvent.Fire(game_event.key)
                    elif game_event.type == pygame.MOUSEBUTTONUP:
                        pos = pygame.mouse.get_pos()

                        clicked_sprites = [s for s in Sprite.Sprites if s.Rectangle.collidepoint(pos)]
                        for s in clicked_sprites:
                            s.OnMouseClick()

                threading.Thread(target=t).start()
