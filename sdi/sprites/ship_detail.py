import pygame
import os

class ShipDetail(pygame.sprite.Sprite):

    def __init__(self, image_path):

        super().__init__()

        self.image = pygame.image.load(os.path.join("assets", "spaceships", image_path))
        self.image = pygame.transform.scale(self.image, (128, 128))