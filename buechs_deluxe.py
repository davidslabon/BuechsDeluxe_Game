import sys

import pygame

from settings import Settings
from toilet_paper import ToiletPaper
from buechs import Buechs
from throw import Throw

class BuechsDeluxe:
    """Overall class to manage game assets and behavior."""

    def __init__(self):
        """Initialize the game, and create game ressources."""
        pygame.init()
        self.settings = Settings()

        self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
        self.settings.screen_width = self.screen.get_rect().width
        self.settings.screen_height = self.screen.get_rect().height

        pygame.display.set_caption("Buechs Deluxe")

        self.toiletpaper = ToiletPaper(self)
        self.buechs = Buechs(self)
        self.throws = pygame.sprite.Group()
        
    def run_game(self):
        """Start the main loop for the game."""
        while True:
            self._check_events()
            self.toiletpaper.update()
            self._update_throws()   
            self._update_screen()
                        
            
            # Make the most recently drawn screen visible.
            pygame.display.flip()
    
    def _check_events(self):
        """Respond to keyboard and mouse events."""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)
                

    def _check_keydown_events(self, event):
        """Check for keydown events and start movement."""
        if event.key == pygame.K_RIGHT:
            self.toiletpaper.moving_right = True
        elif event.key == pygame.K_LEFT:
            self.toiletpaper.moving_left = True
        elif event.key == pygame.K_q or event.key == pygame.K_ESCAPE:
            sys.exit()
        elif event.key == pygame.K_SPACE:
            self._throw_paper()
    
    def _check_keyup_events(self, event):
        """Check for keyup events and stop movement."""
        if event.key == pygame.K_RIGHT:
            self.toiletpaper.moving_right = False
        elif event.key == pygame.K_LEFT:
            self.toiletpaper.moving_left = False

    def _update_throws(self):
        """Update the position of the throws an get rid of old throws."""
        # Update throw position
        self.throws.update()
        
        # Get rid of throws that have disappeared.
        for throw in self.throws.copy():
            if throw.rect.bottom <= 0:
                self.throws.remove(throw)

    def _update_screen(self):
        """Redraw the screen and image elements during each passs through the loop."""
        self.screen.fill(self.settings.bg_color)
        self.screen.blit(self.settings.bg_image.image, self.settings.bg_image.rect)
        self.toiletpaper.blitme()
        self.buechs.blitme()
        for throw in self.throws.sprites():
            throw.draw_throw()

    def _throw_paper(self):
        """Create a new throw and add it to the throws group."""
        if len(self.throws) < self.settings.throws_allowed:
            new_throw = Throw(self)
            self.throws.add(new_throw)


if __name__ == "__main__":
    #Make a game instance, and run the game.
    bd = BuechsDeluxe()
    bd.run_game()