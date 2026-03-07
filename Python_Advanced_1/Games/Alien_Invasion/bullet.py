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