import pygame, os, random, time


class Star(pygame.sprite.Sprite):

    def __init__(self, scale, init_y, init_x=1920):
        super().__init__()
        self.images = []
        self.last_change = time.time()
        self.delays = [0.6 * random.randint(8,12) / 10,
                       0.8 * random.randint(8,12) / 10,
                       0.5 * random.randint(8,12) / 10,
                       0.4 * random.randint(8,12) / 10,
                       0.2 * random.randint(8,12) / 10]
        self.scale = int(3.2 * (random.randint(7, 14) / 10) * scale)
        self.image_ref = random.randint(0,4)
        for suffix in range(5):
            image = pygame.image.load(os.path.join("assets","Animations","Stars","Star1_{}.png".format(suffix)))
            self.images.append(pygame.transform.scale(
                image,
                (
                    int(32 * self.scale),
                    int(32 * self.scale),
                ),
            ))
        self.image = self.images[0]
        self.rect = self.images[0].get_rect()

        self.rect.y = init_y
        self.rect.x = init_x
        self.x_pos = init_x

    def update(self):

        if time.time() > self.last_change + self.delays[self.image_ref]:
            self.image_ref += 1
            if self.image_ref > 4:
                self.image_ref = 0
            self.image = self.images[self.image_ref]
            self.last_change = time.time()
        self.x_pos -= self.scale
        self.rect.x = int(self.x_pos)

        if self.rect.x <= 0:
            self.x_pos = 1920
            self.rect.y = random.randint(0, 1080)
