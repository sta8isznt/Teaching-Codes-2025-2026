class Settings:
    """A class to store all settings for Alien Invasion"""

    def __init__(self):
        """Initialize the game's settings"""
        self.screen_width = 1200
        self.screen_height = 800

        # Ship Settings
        self.ship_speed = 6

        # Bullet Settings
        self.bullet_speed = 7.0
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (255, 255, 255)
        self.bullets_allowed = 7

        # Alien settings
        self.alien_speed = 2.0
        self.fleet_drop_speed = 10
        self.fleet_direction = 1