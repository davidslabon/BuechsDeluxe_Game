import pygame
from pygame.sprite import Sprite

class Throw(Sprite):
    """A class to manage the throw of the toilet paper."""

    def __init__(self, bd_game):
        """Create a throw object at the paper's current position."""
        super().__init__()
        self.screen = bd_game.screen
        self.settings = bd_game.settings
        self.color = self.settings.throw_color
        

        # Create a Throw rect at (0, 0) and then set current position.
        self.rect = pygame.Rect(0, 0, self.settings.throw_width, 
            self.settings.throw_height)
        self.rect.midtop = bd_game.toiletpaper.rect.midtop

        # Store the throws position as a decimal value.
        self.y = float (self.rect.y)

    def rotate(self,angle):
        self.Surface = pygame.transform.rotate(self.rect, angle)

    def update(self):
        """Move the toiletpaper up the screen."""
        self.rotate(90)
        # Update the decimal position of the throw.
        self.y -= self.settings.throw_speed
        # Update the rect position.
        self.rect.y = self.y

    def draw_throw(self):
        """Draw the throw to the screen."""
        pygame.draw.rect(self.screen, self.color, self.rect)