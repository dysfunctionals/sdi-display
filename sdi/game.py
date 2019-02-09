"""You just lost the game."""

import pygame

from sdi.state import StateMachine, GameState
from sdi.background import Background


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
                machine.state = self.play(self.screen)
            else:
                raise EnvironmentError

        pygame.quit()

    def play(self, screen):

        all_sprites = pygame.sprite.Group()
        background = Background(screen)

        clock = pygame.time.Clock()

        game_playing = True

        start_ticks = pygame.time.get_ticks()

        while game_playing:

            for event in pygame.event.get():

                if event.type == pygame.QUIT:
                    game_playing = False

            all_sprites.update()

            background.render(screen)
            all_sprites.draw(screen)

            pygame.display.flip()
            clock.tick(60)

        return GameState.END

