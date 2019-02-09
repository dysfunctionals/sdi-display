"""You just lost the game."""

import pygame

from sdi.state import StateMachine, GameState
from sdi.background import Background
from sdi.sprites import Spaceship


class Game:
    """It's a game."""

    title = "Strategic Defense Initiative"
    screen_width = 1920
    screen_height = 1080

    def __init__(self, config):
        self.config = config

        pygame.init()

        pygame.display.set_caption(Game.title)

        self.screen = pygame.display.set_mode((Game.screen_width, Game.screen_height))

    def run(self):
        """Run the main game loop."""

        machine = StateMachine()

        while machine.state != GameState.END:

            if machine.state == GameState.PLAYING:
                machine.state = self.play(self.screen, self)
            else:
                raise EnvironmentError

        pygame.quit()

    def play(self, screen, game):

        all_sprites = pygame.sprite.Group()
        ships = pygame.sprite.Group()
        background = Background(screen)

        clock = pygame.time.Clock()

        game_playing = True

        start_ticks = pygame.time.get_ticks()

        for sh in game.config['ships']:
            ship = Spaceship(sh['img'])
            ship.rect.x = sh['init_pos'][0]
            ship.rect.y = sh['init_pos'][1]
            all_sprites.add(ship)
            ships.add(ship)

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

