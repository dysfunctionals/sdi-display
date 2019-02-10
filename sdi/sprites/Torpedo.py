import pygame, random, os, time, math


class Torpedo(pygame.sprite.Sprite):

    def __init__(self, colour, bearing, x, y, ship_x_vel,ship_y_vel):
        super().__init__()
        self.speed = 5
        self.x_vel = ship_x_vel
        self.y_vel = ship_y_vel
        self.bearing = bearing
        self.images = []
        self.colour = colour
        self.damage = 11
        self.last_change = time.time()
        self.delays = [0.4 * random.randint(8,12) / 10,
                       0.4 * random.randint(8,12) / 10
                       ]
        self.image_ref = random.randint(0,1)
        for suffix in range(2):
            image = pygame.image.load(os.path.join("assets","Animations","Torpedoes","Torpedo{colour}_{suffix}.png".format(colour=colour,suffix=suffix)))
            self.images.append(pygame.transform.scale(
                image,
                (
                    32,
                    32,
                ),
            ))
        self.image = self.images[0]
        self.rect = self.images[0].get_rect()

        self.rect.y = y
        self.rect.x = x
        self.x_pos = x

        self.x_vel -= (
                math.sin(math.radians(self.bearing)) * self.speed
        )
        self.y_vel -= (
                math.cos(math.radians(self.bearing)) * self.speed
        )

    def update(self):

        if time.time() > self.last_change + self.delays[self.image_ref]:
            self.image_ref += 1
            if self.image_ref > 1:
                self.image_ref = 0
            self.image = self.images[self.image_ref]
            self.last_change = time.time()

        self.rect.x += self.x_vel
        self.rect.y += self.y_vel

        if (self.rect.y < 0) or (
            self.rect.y > 1080 - self.image.get_height()
        ):
            self.kill()
        elif (self.rect.x < 0) or (
            self.rect.x > (1920 - 378) - self.image.get_width()
        ):
            self.kill()

    @staticmethod
    def rotate(image, rect, angle):
        """Rotate the image while keeping its center."""
        # Rotate the original image without modifying it.
        new_image = pygame.transform.rotate(image, angle)
        # Get a new rect with the center of the old rect.
        rect = new_image.get_rect(center=rect.center)
        return new_image, rect