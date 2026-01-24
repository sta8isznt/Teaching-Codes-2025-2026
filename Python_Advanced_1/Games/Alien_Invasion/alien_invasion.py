import pygame as pg
import sys
from settings import Settings
from ship import Ship

class AlienInvasion:
    def __init__(self):
        pg.init()
        self.settings = Settings()

        # Screen Settings
        self.screen = pg.display.set_mode((self.settings.screen_width, self.settings.screen_height))
        pg.display.set_caption("Alien Invasion")

        # Clock Settings
        self.clock = pg.time.Clock()

        # Images
        self.bg_image = pg.image.load("space_image.jpg")
        self.window_image = pg.image.load("ship.bmp")
        pg.display.set_icon(self.window_image)

        # Ship
        self.ship = Ship(self)

    def run(self):
        while True:
            self._check_events()
            self._update_screen()
            self.clock.tick(60)

    def _check_events(self):
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                sys.exit()
            elif event.type == pg.KEYDOWN:
                self._check_keydown_events(event)
            elif event.type == pg.KEYUP:
                self._check_keyup_events(event)

    def _update_screen(self):
        self.screen.blit(self.bg_image, (0,0))
        self.ship.draw_ship()
        pg.display.update()

    def _check_keydown_events(self, event):
        pass

    def _check_keyup_events(self, event):
        pass

ai  = AlienInvasion()
ai.run()


    