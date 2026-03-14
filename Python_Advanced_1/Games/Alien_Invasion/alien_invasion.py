import pygame as pg
import sys
from settings import Settings
from ship import Ship
from bullet import Bullet

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

        # Bullets
        self.bullets = pg.sprite.Group()

    def run(self):
        while True:
            self._check_events()
            self.ship.update_position()
            self.bullets.update()
            for bullet in self.bullets.copy():
                if bullet.rect.bottom < 0:
                    self.bullets.remove(bullet)
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
        self.screen.blit(self.bg_image, (0,0))
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()
        self.ship.draw_ship()
        pg.display.update()

    def _check_keydown_events(self, event):
        if event.key == pg.K_RIGHT:
            self.ship.moving_right = True
        elif event.key == pg.K_LEFT:
            self.ship.moving_left = True
        elif event.key == pg.K_SPACE:
            self._fire_bullet()
        elif event.key == pg.K_ESCAPE:
            pg.quit()
            sys.exit()

    def _check_keyup_events(self, event):
        if event.key == pg.K_RIGHT:
            self.ship.moving_right = False
        elif event.key == pg.K_LEFT:
            self.ship.moving_left = False

    def _fire_bullet(self):
        """Create a new bullet and add it to the bullets Group"""
        if len(self.bullets) < self.settings.bullets_allowed:
            new_bullet = Bullet(self)
            self.bullets.add(new_bullet)

ai  = AlienInvasion()
ai.run()


    
