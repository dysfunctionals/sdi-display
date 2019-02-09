import pygame, os

TWO_HUNDRED_EIGHTY_EIGHT = 288


class Detailoid(pygame.sprite.Sprite):
    def __init__(self):

        super().__init__()
        self.image = pygame.image.load(os.path.join("assets", "detail_display.png"))
        self.image = pygame.transform.scale(self.image, (288, 1080))

        self.rect = self.image.get_rect()
        self.rect.x = 1920 - TWO_HUNDRED_EIGHTY_EIGHT
        self.rect.y = 0
