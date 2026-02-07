import pygame as pg

class Ship:
    """A class to manage the spaceship"""
    def __init__(self, game):
        """Initialize the ship and set its starting position"""
        self.screen = game.screen
        self.screen_rect = self.screen.get_rect()

        # Load the ship image and get its rect
        self.image = pg.image.load("ship.bmp")
        self.image.set_colorkey((230, 230, 230))
        self.rect = self.image.get_rect()

        # Put the ship at the bottom center of the screen
        self.rect.midbottom = self.screen_rect.midbottom

    def draw_ship(self):
        """Draw the ship at its current location"""
        self.screen.blit(self.image, self.rect)
