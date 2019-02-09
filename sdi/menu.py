import pygame
import os
from sdi.state import GameState


class Menu:

    @staticmethod
    def run(screen):
        screen.fill((0, 0, 0))


        pygame.display.flip()

        waiting = True

        while waiting:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    return GameState.END
                elif event.type == pygame.KEYDOWN:
                    waiting = False

        return GameState.PLAYING
