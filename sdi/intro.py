import pygame
import os
from sdi.state import GameState

class Intro:

    @staticmethod
    def run(screen):
        screen.fill((0, 0, 0))

        logo = pygame.image.load(os.path.join("assets", "team.png"))

        logo = pygame.transform.scale(logo, (1920, 1080))

        logo.set_alpha(20)

        screen.blit(logo, (0, 0))

        pygame.display.flip()

        pygame.mixer.music.load(os.path.join("assets", "sound", "theme.ogg"))
        MUSIC_DEATH = pygame.USEREVENT + 1
        pygame.mixer.music.set_endevent(MUSIC_DEATH)
        pygame.mixer.music.play()

        waiting = True

        while waiting:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    return GameState.END
                elif event.type == MUSIC_DEATH:
                    waiting = False

        return GameState.PLAYING
