import pygame
import os
from sdi.state import GameState


class CircleBoi(pygame.sprite.Sprite):

    def __init__(self):
        super().__init__()

        self.image = pygame.image.load(
            os.path.join("assets", "circle.png")
        )
        self.image = pygame.transform.scale(self.image, (500, 500))

        self.rect = self.image.get_rect()

        self.rect.x = 710
        self.rect.y = 1080

    def update(self):

        if self.rect.y > 290:
            self.rect.y -= 10


class TitleBoi(pygame.sprite.Sprite):

    def __init__(self):
        super().__init__()

        self.image = pygame.image.load(
            os.path.join("assets", "title.png")
        )

        self.rect = self.image.get_rect()

        self.rect.x = 662
        self.rect.y = 1500

    def update(self):

        if self.rect.y > 800:
            self.rect.y -= 5


class PressyBoi(pygame.sprite.Sprite):

    def __init__(self):
        super().__init__()

        self.image = pygame.image.load(
            os.path.join("assets", "begin.png")
        )

        self.rect = self.image.get_rect()

        self.rect.x = 771
        self.rect.y = 1800

    def update(self):

        if self.rect.y > 930:
            self.rect.y -= 4.5


class Menu:

    @staticmethod
    def run(screen):

        clock = pygame.time.Clock()

        all_sprites = pygame.sprite.Group()

        circleboi = CircleBoi()
        titleboi = TitleBoi()
        pressyboi = PressyBoi()

        all_sprites.add(circleboi)
        all_sprites.add(titleboi)
        all_sprites.add(pressyboi)

        start_ticks = pygame.time.get_ticks()

        waiting = True

        while waiting:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    return GameState.END
                elif event.type == pygame.KEYDOWN:
                    waiting = False

            all_sprites.update()

            screen.fill((0, 0, 0))
            all_sprites.draw(screen)

            pygame.display.flip()
            clock.tick(60)

        return GameState.PLAYING
