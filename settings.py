from background import Background



class Settings:
    """A class to store all settings for Buechs Deluxe"""

    def __init__ (self):
        """Initialize the game's settings"""
        self.screen_width = int(1200) 
        self.screen_height = int(800)
        self.bg_image = Background('images/suellberg_background.bmp', [0, 0])
        self.bg_color = (255, 255, 255)

        # Throw settings.
        self.throw_speed = 5.0
        self.throw_width = 300
        self.throw_height = 15
        self.throw_color = (100, 100, 255)
        self.throws_allowed = 8
        self.throw_rot_speed = 1.5

        # Toiletpaper settings.
        self.toiletpaper_speed = 3.5
        self.toiletpaper_limit = 3

        # Attacker settings.
        self.attacker_speed = 1.0
        self.fleet_drop_speed = 50
        # fleet_direction of 1 represents right; -1 represents left.
        self.fleet_direction = 1