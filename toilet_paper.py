import pygame
from pygame.sprite import Sprite
 
class ToiletPaper(Sprite):
    """A class to manage the toiletpaper."""
 
    def __init__(self, bd_game):
        """Initialize the toiletpaper and set its starting position."""
        super().__init__()
        self.screen = bd_game.screen
        self.screen_rect = bd_game.screen.get_rect()
        self.settings = bd_game.settings

        # Load the toiletpaper image and get its rect.
        self.image = pygame.image.load('images/toilet_paper_opt3.bmp')
        self.rect = self.image.get_rect()

        # Start each new toiletpaper at the bottom center of the screen.
        self.rect.midbottom = self.screen_rect.midbottom

        # Store a decimal value for the Paper's horizontal position.
        self.x = float(self.rect.x)

        # Movement flag
        self.moving_right = False
        self.moving_left = False

    def update(self):
        """Update the paper's position based on the movement flag."""
        # Update the papers x value, not the rect.
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += self.settings.toiletpaper_speed
        if self.moving_left and self.rect.left > 0:
            self.x -= self.settings.toiletpaper_speed

        # Update rect object from self.x
        self.rect.x = self.x

    def blitme(self):
        """Draw the paper at its current location."""
        self.screen.blit(self.image, self.rect)

    def center_toiletpaper(self):
        """Center the toiletpaper on the screen."""
        self.rect.midbottom = self.screen_rect.midbottom
        self.x = float(self.rect.x)
