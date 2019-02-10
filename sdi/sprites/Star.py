import pygame, os, random, pyganim


class Star(pygame.sprite.Sprite):

    def __init__(self, init_y, init_x=1920):
        super().__init__()
        self.scale = random.random()
        image = pygame.image.load(os.path.join("assets", "Star1.png"))
        self.image = pygame.transform.scale(
            image,
            (
                int(32 * (random.randint(7, 14) / 10) * self.scale),
                int(32 * (random.randint(7, 14) / 10) * self.scale),
            ),
        )
        self.rect = self.image.get_rect()

        self.rect.y = init_y
        self.rect.x = init_x
        self.x_pos = init_x

    def update(self):
        self.x_pos -= self.scale
        self.rect.x = int(self.x_pos)

        if self.rect.x <= 0:
            self.x_pos = 1920
            self.rect.y = random.randint(0, 1080)
