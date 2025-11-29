import pygame as pg
import sys

class PongGame:
    def __init__(self):
        # Initialize Pygame Graphics
        pg.init()

        # Screen Settings
        self.screen = pg.display.set_mode((600, 600))
        pg.display.set_caption("Pong Game")

    def run(self):
        """Run the game loop"""
        while True:
            # In every loop check for user events and update the screen
            self._check_events()
            self._update_screen()

    def _check_events(self):
        """Check for user events"""
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()   # Closes Pygame Graphics
                sys.exit()  # Closes the window

    def _update_screen(self):
        pass

my_pong_game = PongGame()
my_pong_game.run()
            

