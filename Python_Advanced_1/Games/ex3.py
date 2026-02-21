import pygame as pg
import sys

class Game:
    def __init__(self):
        pg.init()

        self.screen = pg.display.set_mode((300, 300))
    

    def run(self):
        while True:
            self._check_events()
            self._update_screen()

    def _check_events(self):
        for event in pg.event.get():
            if event.type == pg.KEYDOWN:
                print(event.key)
            if event.type == pg.QUIT:
                pg.quit()
                sys.exit()

    def _update_screen(self):
        pg.display.update()

game = Game()
game.run()