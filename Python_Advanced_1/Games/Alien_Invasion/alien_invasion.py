import pygame as pg
import sys

class AlienInvasion:
    def __init__(self):
        pg.init()

        # Screen Settings
        self.screen = pg.display.set_mode((1200, 800))
        pg.display.set_caption("Alien Invasion")

        # Clock Settings
        self.clock = pg.time.Clock()

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
        self.screen.fill('black')
        pg.display.update()

    def _check_keydown_events(self, event):
        pass

    def _check_keyup_events(self, event):
        pass

ai  = AlienInvasion()
ai.run()


    