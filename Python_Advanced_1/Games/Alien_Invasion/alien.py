import pygame as pg
from pygame.sprite import Sprite

class Alien(Sprite):
    """A class to represent a single alien in the fleet"""

    def __init__(self, game):

        super().__init__()
        self.screen = game.screen

        # Load the alien image and set its rect attribute
        self.image = pg.image.load('alien.bmp')
        self.image.set_colorkey((230, 230, 230))
        self.rect = self.image.get_rect()