import pygame, math, os, time
from .Torpedo import Torpedo

FRICTION_COEFF = 1 - 0.015


class Spaceship(pygame.sprite.Sprite):
    def __init__(self, colour, img_path, bearing, torpedo_group):

        super().__init__()
        self.torpedo_group = torpedo_group
        self.colour = colour
        self.last_shoot = 0
        self.shoot_delay = 0.9


        self.raw_image = pygame.image.load(
            os.path.join("assets", "spaceships", img_path)
        )
        self.raw_image = pygame.transform.scale(self.raw_image, (64, 64))

        self.image = self.raw_image

        self.rect = self.image.get_rect()

        self.rect.x = 0
        self.rect.y = 0

        self.x_vel = 0
        self.y_vel = 0

        self.power = {"engines": 0, "shields": 0, "weapons": 0}

        self.bearing = {"engines": bearing, "shields": 0, "weapons": 0}

        self.active = {"engines": False, "shields": False, "weapons": False}

        self.health = 100

    def update(self):
        print("{col} health is {health}".format(col=self.colour,health=self.health))
        if self.health <0 :
            print("{me} has now died".format(me=self.colour))
            self.kill()
            return
        self.bearing["engines"] = self.bearing["engines"] % 360
        self.bearing["shields"] = self.bearing["shields"] % 360
        self.bearing["weapons"] = self.bearing["weapons"] % 360

        self.rect.x += self.x_vel
        self.rect.y += self.y_vel

        self.x_vel *= FRICTION_COEFF
        self.y_vel *= FRICTION_COEFF

        if self.active["engines"]:
            self.x_vel -= (
                    math.sin(math.radians(self.bearing["engines"])) * self.power["engines"]
            )
            self.y_vel -= (
                    math.cos(math.radians(self.bearing["engines"])) * self.power["engines"]
            )

        self.image, self.rect = Spaceship.rotate(
            self.raw_image, self.rect, self.bearing["engines"]
        )

        if (self.rect.y < 0 and self.y_vel < 0) or (
            self.rect.y > 1080 - self.image.get_height() and self.y_vel > 0
        ):
            self.y_vel = -self.y_vel

        if (self.rect.x < 0 and self.x_vel < 0) or (
            self.rect.x > (1920 - 378) - self.image.get_width() and self.x_vel > 0
        ):
            self.x_vel = -self.x_vel

        if self.active["weapons"] and time.time() > self.last_shoot + (self.shoot_delay/(self.power["weapons"]/65 + 0.1)):
            self.shoot()
            self.last_shoot = time.time()

    def shoot(self):
        self.torpedo_group.add(Torpedo(self.colour,self.bearing["weapons"],self.rect.x,self.rect.y,self.x_vel,self.y_vel))


    @staticmethod
    def rotate(image, rect, angle):
        """Rotate the image while keeping its center."""
        # Rotate the original image without modifying it.
        new_image = pygame.transform.rotate(image, angle)
        # Get a new rect with the center of the old rect.
        rect = new_image.get_rect(center=rect.center)
        return new_image, rect
