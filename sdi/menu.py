import pygame, random
import copy
import os
from sdi.state import GameState
from sdi.sprites.Star import Star


class CircleBoi(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()

        self.image = pygame.image.load(os.path.join("assets", "circle.png"))
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

        self.image = pygame.image.load(os.path.join("assets", "title.png"))

        self.rect = self.image.get_rect()

        self.rect.x = 662
        self.rect.y = 1500

    def update(self):

        if self.rect.y > 800:
            self.rect.y -= 5


class PressyBoi(pygame.sprite.DirtySprite):
    def __init__(self):
        super().__init__()

        self.raw_image = pygame.image.load(os.path.join("assets", "begin.png"))

        self.image = copy.copy(self.raw_image)

        self.rect = self.image.get_rect()

        self.rect.x = 771
        self.rect.y = 2200

        self.count = 0
        self.visible = True

    def update(self):

        if self.rect.y > 930:
            self.rect.y -= 4.5
        else:
            self.count += 1

            if self.count > 30:
                self.visible = not self.visible
                self.count = 0

                if self.visible:
                    self.image = copy.copy(self.raw_image)
                else:
                    self.image.fill((0, 0, 0))


class Ronald(pygame.sprite.DirtySprite):
    def __init__(self):
        super().__init__()

        self.image = pygame.image.load(os.path.join("assets", "sizeable-ronald.png"))

        self.rect = self.image.get_rect()

        self.rect.x = 818
        self.rect.y = 1800

        self.count = 0
        self.visible = True

    def update(self):

        if self.rect.y > 405:
            self.rect.y -= 4.5


class Menu:
    @staticmethod
    def run(screen):

        clock = pygame.time.Clock()

        all_sprites = pygame.sprite.Group()

        circleboi = CircleBoi()
        titleboi = TitleBoi()
        pressyboi = PressyBoi()
        ron = Ronald()

        all_sprites.add(circleboi)
        all_sprites.add(titleboi)
        all_sprites.add(pressyboi)
        all_sprites.add(ron)

        start_ticks = pygame.time.get_ticks()

        waiting = True

        stars = pygame.sprite.Group()

        for i in range(0, 70):
            star = Star(0.5, random.randint(0, 1080), random.randint(0, 1920))
            stars.add(star)

        pygame.mixer.music.load(os.path.join("assets", "sound", "intro.mp3"))
        pygame.mixer.music.play()

        while waiting:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    return GameState.END
                elif event.type == pygame.KEYDOWN:
                    waiting = False

            all_sprites.update()
            stars.update()

            screen.fill((0, 0, 0))
            stars.draw(screen)
            all_sprites.draw(screen)

            pygame.display.flip()
            clock.tick(60)

        return GameState.PLAYING
