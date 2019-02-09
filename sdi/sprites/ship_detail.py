import pygame
import os

class ShipDetail(pygame.sprite.Sprite):

    def __init__(self, image_path):

        super().__init__()

        self.image = pygame.image.load(os.path.join("assets", "spaceships", image_path))
        self.rect = self.image.get_rect()
        self.image = pygame.transform.scale(self.image, (222, 222))
