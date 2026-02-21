import pygame as pg
import sys  # Για να μπορούμε να κλείσουμε το παράθυρο

class Challenge1:
    def __init__(self):
        pg.init()

        self.screen = pg.display.set_mode((1000, 800))
        self.screen_rect = self.screen.get_rect()

        self.popai_image = pg.image.load("Popeye_transparent.png")
        self.image_rect = self.popai_image.get_rect()

        self.image_rect.center = self.screen_rect.center

    def run(self):
        while True:
            self._check_events()
            self._update_screen()

    def _check_events(self):
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                sys.exit()

    def _update_screen(self):
        self.screen.fill("blue")

        self.screen.blit(self.popai_image, self.image_rect)

        # παντα υπάρχει αυτό!!!!
        pg.display.update()

challenge = Challenge1()
challenge.run()
