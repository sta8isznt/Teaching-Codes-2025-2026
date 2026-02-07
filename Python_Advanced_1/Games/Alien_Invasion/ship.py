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
        self.settings = game.settings

        # Put the ship at the bottom center of the screen
        self.rect.midbottom = self.screen_rect.midbottom

        # Moving Settings
        self.moving_right = False   # Start the game without moving
        self.moving_left = False

    def update_position(self):
        """Update the ship's position based on the moving flag"""
        if self.moving_right == True and self.rect.right < self.screen_rect.right:
            self.rect.x += self.settings.ship_speed
        if self.moving_left == True and self.rect.left > self.screen_rect.left:
            self.rect.x -= self.settings.ship_speed

    def draw_ship(self):
        """Draw the ship at its current location"""
        self.screen.blit(self.image, self.rect)
