import pygame

class Background(pygame.sprite.Sprite):
    """A class that manages the background image upload and handling."""

    def __init__(self, image_file, location):
        """Upload and initialize background image."""
        pygame.sprite.Sprite.__init__(self)  #call Sprite initializer
        self.image = pygame.image.load(image_file)
        self.rect = self.image.get_rect()
        self.rect.left, self.rect.top = location