import pygame as pg
import sys
import random

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

        # Paddles
        self.player_1 = pg.Rect(0,0, 20, 100)
        self.player_1.midleft = self.screen_rect.midleft
        self.player_2 = pg.Rect(0,0,20, 100)
        self.player_2.midright = self.screen_rect.midright

        self.player_1_speed = 0
        self.player_2_speed = 0

        # Score
        self.player_1_score = 0
        self.player_2_score = 0
        self.score_font = pg.font.Font(None, 80)

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

        pg.draw.rect(self.screen, 'white', self.player_1)
        pg.draw.rect(self.screen, 'white', self.player_2)

        self._update_ball_position()
        self._update_player_1_pos()
        self._update_player_2_pos()
        self.update_score()
        pg.display.update()

    def _update_player_1_pos(self):
        self.player_1.y = self.player_1.y + self.player_1_speed

        # Do not allow the paddles to go out of the screen
        if self.player_1.top < 0:
            self.player_1.top = 0
        elif self.player_1.bottom > self.screen_rect.bottom:
            self.player_1.bottom = self.screen_rect.bottom

    def _update_player_2_pos(self):
        self.player_2.y = self.player_2.y + self.player_2_speed

        if self.player_2.top < 0:
            self.player_2.top = 0
        elif self.player_2.bottom > self.screen_rect.bottom:
            self.player_2.bottom = self.screen_rect.bottom

    def _update_ball_position(self):
        """Update the position of the ball based on its current x, y speeds and directions"""
        self.ball.x = self.ball.x + (self.ball_speed_x * self.ball_x_direction)
        self.ball.y = self.ball.y + (self.ball_speed_y * self.ball_y_direction)

        if self.ball.bottom >= self.screen_rect.bottom or self.ball.top <= 0:
            # Every time the direction of the ball is reverted
            self.ball_y_direction *= -1
        if self.ball.colliderect(self.player_2) or self.ball.colliderect(self.player_1):
            self.ball_x_direction *= -1
            self.ball_speed_x += 1
            self.ball_speed_y += 1

        if self.ball.right >= self.screen_rect.right:
            self.point_won("player_1")
        if self.ball.left <= self.screen_rect.left:
            self.point_won("player_2")

    def point_won(self, winner):
        """Gives the winner 1 point"""
        if winner == "player_1":
            self.player_1_score += 1
        elif winner == "player_2":
            self.player_2_score += 1

        self.reset_ball()
        
    def reset_ball(self):
        """Reset the ball's position to the center of the screen"""
        self.ball.center = self.screen_rect.center
        self.ball.y = random.randint(10, 100)
        self.ball_x_direction = random.choice([1, -1])
        self.ball_y_direction = random.choice([1, -1])
        self.ball_speed_x = 6
        self.ball_speed_y = 6

    def _check_keydown_events(self, event):
        if event.key == pg.K_UP:
            self.player_2_speed = -6
        if event.key == pg.K_DOWN:
            self.player_2_speed = 6
        if event.key == pg.K_w:
            self.player_1_speed = -6
        if event.key == pg.K_s:
            self.player_1_speed = 6

    def _check_keyup_events(self, event):
        if event.key == pg.K_UP:
            self.player_2_speed = 0
        if event.key == pg.K_DOWN:
            self.player_2_speed = 0
        if event.key == pg.K_w:
            self.player_1_speed = 0
        if event.key == pg.K_s:
            self.player_1_speed = 0

    def update_score(self):
        """Displayes the right score to the screen"""
        player_1_score_img = self.score_font.render(str(self.player_1_score),True, 'white', 'black')
        self.screen.blit(player_1_score_img, (self.screen_rect.width/4, 20))
        player_2_score_img = self.score_font.render(str(self.player_2_score),True, 'white', 'black')
        self.screen.blit(player_2_score_img, (self.screen_rect.width * 3/4, 20))

my_pong_game = PongGame()
my_pong_game.run()
            