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

        # Ball
        self.ball = pg.Rect(0,0,30,30)
        self.ball.center = self.screen_rect.center
        self.ball_speed_x = 6
        self.ball_speed_y = 6
        self.ball_x_direction = 1
        self.ball_y_direction = 1

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
        # Fill the screen with black background color to erase all past changes
        self.screen.fill('black')

        # Draw a simple line at the center of the screen
        pg.draw.aaline(self.screen, 'white', self.screen_rect.midtop, self.screen_rect.midbottom)
        pg.draw.ellipse(self.screen, 'white', self.ball)
        self._update_ball_position()
        pg.display.update()

    def _update_ball_position(self):
        """Update the position of the ball based on its current x, y speeds and directions"""
        self.ball.x = self.ball.x + (self.ball_speed_x * self.ball_x_direction)
        self.ball.y = self.ball.y + (self.ball_speed_y * self.ball_y_direction)

        if self.ball.bottom >= self.screen_rect.bottom or self.ball.top <= 0:
            self.ball_y_direction *= -1
        if self.ball.right >= self.screen_rect.right or self.ball.left <= 0:
            self.ball_x_direction *= -1


    def _check_keydown_events(event):
        pass

    def _check_keyup_events(event):
        pass

my_pong_game = PongGame()
my_pong_game.run()
            