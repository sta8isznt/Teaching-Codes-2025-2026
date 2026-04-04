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

        # Start each new alien near the top left of the screen
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        # Game settings
        self.settings = game.settings

        # Store the alien's exact horizontal position
        self.x = float(self.rect.x)

    def draw(self):
        self.screen.blit(self.image, self.rect)

    def update(self):
        """Move the alien to the right"""
        self.rect.x += (self.settings.alien_speed * self.settings.fleet_direction)

    def check_edges(self):
        """Return True if alien is at the edge of the screen"""
        screen_rect = self.screen.get_rect()
        return (self.rect.right >= screen_rect.right) or (self.rect.left <= screen_rect.left)