import pygame, os


class Background:
    """The background, obviously?"""

    def __init__(self, screen):

        self.bg_img = pygame.image.load(os.path.join("assets", "background.png"))
        self.bg_img = pygame.transform.scale(self.bg_img, (screen.get_width(), screen.get_height()))

    def render(self, screen):
        screen.blit(self.bg_img, (0,0))
