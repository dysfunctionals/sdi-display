import pygame, math, os


class Spaceship(pygame.sprite.Sprite):

    def __init__(self, img_path):

        super().__init__()

        self.raw_image = pygame.image.load(os.path.join("assets", "spaceships", img_path))
        self.raw_image = pygame.transform.scale(self.raw_image, (64, 64))

        self.image = self.raw_image

        self.rect = self.image.get_rect()

        self.rect.x = 0
        self.rect.y = 0

        self.velocity = 0

        self.bearing = 0

    def update(self):

        self.update_rect()

        self.bearing = self.bearing % 360

        self.image, self.rect = Spaceship.rotate(self.raw_image, self.rect, self.bearing)

    def update_rect(self):

        if self.bearing >= 0 and self.bearing < 90:
            self.rect.x += math.sin(math.radians(self.bearing)) * self.velocity
            self.rect.y -= math.cos(math.radians(self.bearing)) * self.velocity

        if self.bearing >= 90 and self.bearing < 180:
            self.rect.x += math.sin(math.radians(180 - self.bearing)) * self.velocity
            self.rect.y += math.cos(math.radians(180 - self.bearing)) * self.velocity

        if self.bearing >= 180 and self.bearing < 270:
            self.rect.x -= math.sin(math.radians(180 + self.bearing)) * self.velocity
            self.rect.y += math.cos(math.radians(180 + self.bearing)) * self.velocity

        if self.bearing >= 270 and self.bearing <= 360:
            self.rect.x -= math.sin(math.radians(360 - self.bearing)) * self.velocity
            self.rect.y -= math.cos(math.radians(360 - self.bearing)) * self.velocity



    @staticmethod
    def rotate(image, rect, angle):
        """Rotate the image while keeping its center."""
        # Rotate the original image without modifying it.
        new_image = pygame.transform.rotate(image, angle)
        # Get a new rect with the center of the old rect.
        rect = new_image.get_rect(center=rect.center)
        return new_image, rect


