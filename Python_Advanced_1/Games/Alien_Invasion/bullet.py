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

        self.rect = pg.Rect(0,0, self.bullet_width, self.bullet_height)
        self.rect.midtop = game.ship.rect.midtop

    def update_position(self):
        """Move the bullet up the screen"""
        self.rect.y -= self.settings.bullet_speed
