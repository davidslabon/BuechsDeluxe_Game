import pygame
from pygame.sprite import Sprite

class Attacker(Sprite):
    """A class to represent a single attacker in the fleet."""

    def __init__(self, bd_game):
        super().__init__()
        self.screen = bd_game.screen
        self.settings = bd_game.settings

        # Load the attacker image and set its rect attribute.
        self.image = pygame.image.load("images/buechs.bmp")
        self.rect = self.image.get_rect()

        # Start each new attacker near the top left of the screen
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        # Store the attacker's horizontal positiion.
        self.x = float(self.rect.x)

    def update(self):
        """Move the attacker right or left."""
        self.x += (self.settings.attacker_speed *
                        self.settings.fleet_direction)
        self.rect.x = self.x

    def check_edges(self):
        """Return True if attacker reaches edge of screen."""
        screen_rect = self.screen.get_rect()
        if self.rect.right >= screen_rect.right or self.rect.left <= 0:
            return True
        