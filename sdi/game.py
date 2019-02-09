"""You just lost the game."""

import pygame

from sdi.state import StateMachine, GameState


class Game:
    """It's a game."""

    title = "Strategic Defense Initiative"
    screen_width = 1920
    screen_height = 1080

    def __init__(self):
        pygame.init()

        pygame.display.set_caption(Game.title)

        self.screen = pygame.display.set_mode((Game.screen_width, Game.screen_height))

    def run(self):
        """Run the main game loop."""

        machine = StateMachine()

        while machine.state != GameState.END:

            if machine.state == GameState.PLAYING:
                self.play(self.screen)
            else:
                raise EnvironmentError

        pygame.quit()

    def play(self, screen):
        pass
