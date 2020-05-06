import pygame
 
class Buechs:
    """A class to manage the ship."""
 
    def __init__(self, bd_game):
        """Initialize the ship and set its starting position."""
        self.screen = bd_game.screen
        self.screen_rect = bd_game.screen.get_rect()

        # Load the ship image and get its rect.
        self.image = pygame.image.load('images/buechs.bmp')
        self.rect = self.image.get_rect()

        # Start each new ship at the bottom center of the screen.
        self.rect.center = self.screen_rect.center

    def blitme(self):
        """Draw the buechs at its current location."""
        self.screen.blit(self.image, self.rect)
