import pygame, random

class Animatable(pygame.sprite.Sprite):
    def __init__(self, files, image_count, delays, scale, init_y, init_x=1920):
        super().__init__()
        self.images = []
        self.delays = delays

        self.scale = int(32 * (random.randint(7, 14) / 10) * self.scale)

        for suffix in range(image_count):
            image = pygame.image.load(files + "_{}.png".format(suffix))
            self.images.append(pygame.transform.scale(
                image,
                (
                    int(32 * self.scale),
                    int(32 * self.scale),
                ),
            ))

        self.rect = self.images[0].get_rect()

        self.rect.y = init_y
        self.rect.x = init_x
        self.x_pos = init_x

    def update(self):
        self.x_pos -= self.scale
        self.rect.x = int(self.x_pos)

        if self.rect.x <= 0:
            self.x_pos = 1920
            self.rect.y = random.randint(0, 1080)