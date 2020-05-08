import pygame
from pygame.sprite import Sprite

class Attacker(Sprite):
    """A class to represent a single attacker in the fleet."""

    def __init__(self, bd_game):
        super().__init__()
        self.screen = bd_game.screen

        # Load the attacker image and set its rect attribute.
        self.image = pygame.image.load("images/buechs.bmp")
        self.rect = self.image.get_rect()

        # Start each new attacker near the top left of the screen
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        # Store the attacker's horizontal positiion.
        self.x = float(self.rect.x)