import pygame, os
import random, time


class Background:
    """The background, obviously?"""

    def __init__(self, screen):
        self.screen = screen

    def render(self):
        self.screen.fill((0, 0, 0))
