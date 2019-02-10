"""You just lost the game."""

import pygame

from sdi.state import StateMachine, GameState
from sdi.background import Background
from sdi.sprites import Spaceship
from sdi.detailoid import Detailoid
from sdi.sprites.ship_detail import ShipDetail
from sdi.intro import Intro
from sdi.menu import Menu


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
            elif machine.state == GameState.INTRO:
                machine.state = Intro.run(self.screen)
            elif machine.state == GameState.MENU:
                machine.state = Menu.run(self.screen)
            else:
                raise EnvironmentError

        pygame.quit()

    def play(self, screen, game):

        all_sprites = pygame.sprite.Group()
        ship_group = pygame.sprite.Group()

        ships = []

        background = Background(screen)

        clock = pygame.time.Clock()

        game_playing = True

        start_ticks = pygame.time.get_ticks()

        d = Detailoid()

        for sh in game.config["ships"]:
            ship = Spaceship(sh["img"], sh["init_bearing"])
            ship.rect.x = sh["init_pos"][0]
            ship.rect.y = sh["init_pos"][1]
            all_sprites.add(ship)
            ship_group.add(ship)
            ships.append(ship)

        all_sprites.add(d)

        # Note: two for loops through ships are used because it needs to work like that
        for sh in game.config["ships"]:
            shop = ShipDetail(sh["detail_img"])
            shop.rect.x = sh["detail_pos"][0]
            shop.rect.y = sh["detail_pos"][1]
            all_sprites.add(shop)

        d.eat_frogs(all_sprites, ships)

        while game_playing:

            for event in pygame.event.get():

                if event.type == pygame.QUIT:
                    game_playing = False

                if event.type == pygame.KEYDOWN:

                    for index, ship in enumerate(game.config["ships"]):

                        try:
                            direction = ship["controls"].index(event.key)

                            velocity_delta = 0.2
                            bearing_delta = 15

                            if direction == 0:
                                ships[index].power['engines'] += velocity_delta
                            if direction == 1:
                                ships[index].bearing["engines"] += bearing_delta
                            if direction == 2:
                                ships[index].power['engines'] -= velocity_delta
                            if direction == 3:
                                ships[index].bearing['engines'] -= bearing_delta

                        except ValueError:
                            pass

            all_sprites.update()

            background.render(screen)
            all_sprites.draw(screen)

            pygame.display.flip()
            clock.tick(60)

        return GameState.END
