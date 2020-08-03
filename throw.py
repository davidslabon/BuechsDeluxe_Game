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
        self.rot_speed = self.settings.throw_rot_speed
        self.rot = 0
        
        # Create a Throw rect at (0, 0) and then set current position.
        # Load the toiletpaper image and get its rect.
        self.image = pygame.image.load('images/toilet_paper_opt3.bmp')
        self.rect = self.image.get_rect()
        self.rect.midtop = bd_game.toiletpaper.rect.midtop

        # self.rect = pygame.Rect(0, 0, self.settings.throw_width, 
        #     self.settings.throw_height)
        # self.rect.midtop = bd_game.toiletpaper.rect.midtop
      

        # Store the throws position as a decimal value.
        self.y = float (self.rect.y)

  
    def update(self):
        """Move the toiletpaper up the screen."""
        # Update the decimal position of the throw.
        self.y -= self.settings.throw_speed
        self.rot += self.rot_speed
        self.throw_image = pygame.transform.rotate(self.image, self.rot)
        

        # Update the rect position.
        self.rect.y = self.y

    def blitme(self):
        """Draw the throw at its current location."""
        self.screen.blit(self.throw_image, self.rect)

    # def draw_throw(self):
    #     """Draw throw on the screen."""
    #     pygame.draw.rect(self.screen, self.color, self.rect)
        

