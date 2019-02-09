import pygame, os
import random, time

class Background:
    """The background, obviously?"""

    def __init__(self, screen):
        self.screen = screen
        self.bg_img = pygame.image.load(os.path.join("assets", "background2.png"))
        self.bg_img = pygame.transform.scale(
            self.bg_img, (screen.get_width(), screen.get_height())
        )
        self.front_scroller = StarScroller(screen.get_width(),screen.get_height(),2, 1, 5, 10)
        for x in range(self.front_scroller.sprite_amount):
            self.front_scroller.add_new(random.randint(0,screen.get_width()), random.randint(0,screen.get_height()))

        self.middle_scroller = StarScroller(screen.get_width(), screen.get_height(), 0.6, 0.5, 10, 25)
        for x in range(self.middle_scroller.sprite_amount):
            self.middle_scroller.add_new(random.randint(0, screen.get_width()), random.randint(0, screen.get_height()))

        self.back_scroller = StarScroller(screen.get_width(), screen.get_height(), 0.01, 0.1, 20, 57)
        for x in range(self.back_scroller.sprite_amount):
            self.back_scroller.add_new(random.randint(0, screen.get_width()), random.randint(0, screen.get_height()))

    def render(self, screen):
        self.front_scroller.update()
        self.middle_scroller.update()
        self.back_scroller.update()
        self.screen.blit(self.bg_img, (0, 0))
        self.front_scroller.draw(self.screen)
        self.middle_scroller.draw(self.screen)
        self.back_scroller.draw(self.screen)

class StarScroller(pygame.sprite.Group):

    def __init__(self, screen_width, screen_height, speed, scale, delay, sprite_amount):
        super().__init__()
        self.sprite_amount = sprite_amount
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.speed = speed
        self.scale = scale
        self.delay = delay
        self.last_spawned = time.time()
        self.curr_delay = self.delay * 10

    def add_new(self, x=-1,y=-1):
        if x > 0 and y > 0:
            sprite = Star(x, y, self.scale, self.speed)
        else:
            sprite = Star(self.screen_width,random.randint(0, self.screen_height), self.scale, self.speed)

        self.add(sprite)
        self.last_spawned = time.time()
        self.curr_delay = random.random() * self.delay

    def update(self):
        super().update()

        if len(self) < self.sprite_amount:
            q = -99999
            for thing in self:
                if thing.rect.x > q:
                    q = thing.rect.x
            if time.time() > self.last_spawned + self.delay:
                self.add_new()


class ScrollableSprite(pygame.sprite.Sprite):

    def __init__(self,speed):
        super().__init__()
        self.speed = speed

    def update(self):
        self.rect.x -= self.speed

        if self.rect.x < 0:
            self.kill()


class Star(ScrollableSprite):

    def __init__(self, xpos, ypos, scale, speed):
        super().__init__(speed)
        self.scale = scale
        image = pygame.image.load(os.path.join("assets", "Star1.png"))
        self.image = pygame.transform.scale(image, (int(32 * (random.randint(7,14) / 10) * self.scale), int(32 * (random.randint(7,14) / 10) * self.scale)))
        self.rect = self.image.get_rect()


        self.rect.y = ypos
        self.rect.x = xpos
