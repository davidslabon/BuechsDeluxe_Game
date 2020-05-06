from background import Background

class Settings:
    """A class to store all settings for Buechs Deluxe"""

    def __init__ (self):
        """Initialize the game's settings"""
        self.screen_width = int(1920) 
        self.screen_height = int(1080)
        self.bg_image = Background('images/suellberg_background.bmp', [0, 0])
        self.bg_color = (255, 255, 255)

        #Throw settings.
        self.throw_speed = 2.0
        self.throw_width = 6
        self.throw_height = 15
        self.throw_color = (100, 100, 255)
        self.throws_allowed = 3

        # Toiletpaper settings.
        self.toiletpaper_speed = 3.5