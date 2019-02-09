import pygame, \
os

class Detailoid(pygame.sprite.Sprite):

    def __init__(self, image_path):

        super().__init__()
        self.image = pygame.image.load(os.path.join("assets", "spaceships", image_path))
        self.image = pygame.transform.scale(self.image, (1080, 288))