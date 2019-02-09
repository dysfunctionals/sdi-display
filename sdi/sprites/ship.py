import pygame, os


class Spaceship(pygame.sprite.Sprite):

    def __init__(self, img_path):

        super().__init__()

        self.image = pygame.image.load(os.path.join("assets", "spaceships", img_path))
        self.image = pygame.transform.scale(self.image, (64, 64))

        self.rect = self.image.get_rect()

        self.rect.x = 0
        self.rect.y = 0

        self.x_velocity = 0
        self.y_velocity = 0
