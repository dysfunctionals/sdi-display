import pygame, random, os, time, math

class Explosion(pygame.sprite.Sprite):
  def __init__(self, colour, x, y):
    super().__init__()
    
    self.images = []
    self.last_change = time.time()
    self.delays = [
      0.4 * random.randint(8,12) / 10,
      0.4 * random.randint(8,12) / 10,

      0.4 * random.randint(8,12) / 10,
      0.4 * random.randint(8,12) / 10,
      0.4 * random.randint(8,12) / 10,
      0.4 * random.randint(8,12) / 10,
      0.4 * random.randint(8,12) / 10,
      0.4 * random.randint(8,12) / 10,
      0.4 * random.randint(8,12) / 10,
      0.4 * random.randint(8,12) / 10,
      0.4 * random.randint(8,12) / 10,
      0.4 * random.randint(8,12) / 10,
      0.4 * random.randint(8,12) / 10,
      0.4 * random.randint(8,12) / 10,
      0.4 * random.randint(8,12) / 10,
      0.4 * random.randint(8,12) / 10,
      0.4 * random.randint(8,12) / 10,
      0.4 * random.randint(8,12) / 10,
      0.4 * random.randint(8,12) / 10,
      0.4 * random.randint(8,12) / 10,
      0.4 * random.randint(8,12) / 10,
      0.4 * random.randint(8,12) / 10,
      0.4 * random.randint(8,12) / 10,
      0.4 * random.randint(8,12) / 10,
    ]
    self.image_ref = 0 
    for suffix in range(16):
      image = pygame.image.load(os.path.join("assets", "Animations","Explosions", "Explosion{colour}_{suffix:02d}.png".format(colour=colour,suffix=suffix)))
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

  def update(self):

    if time.time() > self.last_change + self.delays[self.image_ref]:
      self.image_ref += 1
      if self.image_ref > 15:
         self.kill()
         return
      self.image = self.images[self.image_ref]
      self.last_change = time.time()

