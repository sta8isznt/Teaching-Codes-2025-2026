import pygame as pg
import sys

class PongGame:
    def __init__(self):
        # Initialize Pygame Graphics
        pg.init()

        # Screen Settings
        self.screen = pg.display.set_mode((1280, 760))
        pg.display.set_caption("Pong Game")
        self.screen_rect = self.screen.get_rect()

        # Clock Settings
        # self.clock will be an object of class Clock()
        self.clock = pg.time.Clock()

    def run(self):
        """Run the game loop"""
        while True:
            # In every loop check for user events and update the screen
            self._check_events()
            self._update_screen()
            self.clock.tick(60)

    def _check_events(self):
        """Check for user events"""
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()   # Closes Pygame Graphics
                sys.exit()  # Closes the window
            elif event.type == pg.KEYDOWN:
                self._check_keydown_events(event)
            elif event.type == pg.KEYUP:
                self._check_keyup_events(event)            

    def _update_screen(self):
        """Update the screen with the latest changes"""
        pg.display.update()

    def _check_keydown_events(event):
        pass

    def _check_keyup_events(event):
        pass

my_pong_game = PongGame()
my_pong_game.run()
            