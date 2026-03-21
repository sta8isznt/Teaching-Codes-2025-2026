import pygame as pg
from pygame.sprite import Sprite # Αυτή η κλάση θα είναι ο γονέας των Bullets

class Bullet(Sprite):
    """A class to manage bullets fired from the ship"""

    def __init__(self, game):
        """Create a bullet object at the ship's current position."""

        super().__init__()
        self.screen = game.screen
        self.settings = game.settings
        self.color = self.settings.bullet_color
        self.bullet_width = self.settings.bullet_width
        self.bullet_height = self.settings.bullet_height

        self.rect = pg.Rect(0,0, self.bullet_height, self.bullet_width)
        self.rect.midleft = game.ship.rect.midright

    def update(self):
        """Move the bullet up the screen"""
        self.rect.x += self.settings.bullet_speed

    def draw_bullet(self):
        pg.draw.rect(self.screen, self.color, self.rect)
