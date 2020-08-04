from background import Background



class Settings:
    """A class to store all settings for Buechs Deluxe"""

    def __init__ (self):
        """Initialize the game's static settings"""
        self.screen_width = int(1200) 
        self.screen_height = int(800)
        self.bg_image = Background('images/suellberg_background.bmp', [0, 0])
        self.bg_color = (255, 255, 255)

        # Throw settings.
        self.throw_width = 300
        self.throw_height = 15
        self.throw_color = (100, 100, 255)
        self.throws_allowed = 8
        self.throw_rot_speed = 1.7

        # Toiletpaper settings.
        self.toiletpaper_speed = 3.5
        self.toiletpaper_limit = 3

        # Attacker settings.
        self.fleet_drop_speed = 20

        # How quickly the game speeds up
        self.speedup_scale = 1.3
        
        # How quickly the attacker point values increase
        self.score_scale = 1.2

        self.initialize_dynamic_settings()

        
        
    def initialize_dynamic_settings(self):
        """Initialize settings that change throughout the game."""
        self.toiletpaper_speed = 1.5
        self.throw_speed = 3.0
        self.attacker_speed = 1.0

        # fleet_direction of 1 represents right; -1 represents left.
        self.fleet_direction = 1

        # Scoring
        self.attacker_points = 50
        

    def increase_speed(self):
        """Increase speed settings and attacker point values"""
        self.toiletpaper_speed *= self.speedup_scale
        self.throw_speed *= self.speedup_scale
        self.attacker_speed *= self.speedup_scale
        
        self.attacker_points = int(self.attacker_points * self.score_scale)
