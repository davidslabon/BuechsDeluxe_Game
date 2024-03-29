import sys
from time import sleep

import pygame

from settings import Settings
from game_stats import GameStats
from toilet_paper import ToiletPaper
from buechs import Buechs
from throw import Throw
from attacker import Attacker
from button import Button
from scoreboard import Scoreboard

class BuechsDeluxe:
    """Overall class to manage game assets and behavior."""

    def __init__(self):
        """Initialize the game, and create game ressources."""
        pygame.init()
        self.settings = Settings()
        
        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))
        self.settings.screen_width = self.screen.get_rect().width
        self.settings.screen_height = self.screen.get_rect().height

        pygame.display.set_caption("Buechs Deluxe")
        
        # Create an instance to store game statistics 
        #   and create a scoreboard.
        self.stats = GameStats(self)
        self.sb = Scoreboard(self)
        self.toiletpaper = ToiletPaper(self)
        self.throws = pygame.sprite.Group()
        self.attackers = pygame.sprite.Group()

        self._create_fleet()
        self.play_button = Button(self, "Play")
        
    def run_game(self):
        """Start the main loop for the game."""
        while True:
            self._check_events()

            if self.stats.game_active:
                self.toiletpaper.update()
                self._update_throws()   
                self._update_attackers()

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
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                self._check_play_button(mouse_pos)


    def _check_play_button(self, mouse_pos):
        """Start a new game when the player clicks Play."""
        if self.play_button.rect.collidepoint(mouse_pos):
            self._start_game()

    def _start_game(self):
        if not self.stats.game_active:
            # Rest the game settings.
            self.settings.initialize_dynamic_settings()
            
            # Reset the game statistics
            self.stats.reset_stats()
            self.stats.game_active = True
            self.sb.prep_score()
            self.sb.prep_level()
            self.sb.prep_toiletpapers()

            #Get rid of any remaining attackers and throws.
            self.attackers.empty()
            self.throws.empty()

            # Create a new attacker fleet and center the toilet paper.
            self._create_fleet()
            self.toiletpaper.center_toiletpaper()

            # Hide the mouse cursor.
            pygame.mouse.set_visible(False)

    def _check_keydown_events(self, event):
        """Check for keydown events and start movement."""
        if event.key == pygame.K_RIGHT:
            self.toiletpaper.moving_right = True
        elif event.key == pygame.K_LEFT:
            self.toiletpaper.moving_left = True
        elif event.key == pygame.K_q or event.key == pygame.K_ESCAPE:
            sys.exit()
        elif event.key == pygame.K_p:
            self._start_game()
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
        
        self._check_throw_attacker_collision()

    def _check_throw_attacker_collision(self):
        """ Check for any throws that have hit attackers."""
        #  If so, get rid of the throw and the attacker.
        collisions = pygame.sprite.groupcollide(self.throws, self.attackers, True, True)

        if collisions:
            for attackers in collisions.values():
                self.stats.score += self.settings.attacker_points
                self.sb.check_high_score()
            self.sb.prep_score()
            
            

        if not self.attackers:
            # Destroy existing throws and create a new fleet.
            self.throws.empty()
            self._create_fleet()
            self.settings.increase_speed()

            # Increase level.
            self.stats.level += 1
            self.sb.prep_level()

    def _update_attackers(self):
        """Check if the fleet is at an edge,
        then update the position of all attackers in the fleet."""
        self._check_fleet_edges()
        self.attackers.update()

        # Look for an attacker - toiletpaper collision.
        if pygame.sprite.spritecollideany(self.toiletpaper, self.attackers):
            self._toiletpaper_hit()

        # Look for attackers itting the bottom of the screeb.
        self._check_attackers_bottom()

    def _check_attackers_bottom(self):
        """Check if any attackers have reached the bottom of the screen"""
        screen_rect = self.screen.get_rect()
        for attacker in self.attackers.sprites():
            if attacker.rect.bottom >= screen_rect.bottom:
                # Treat this the same as if the paper got hit.
                self._toiletpaper_hit()
                break
        
    def _toiletpaper_hit(self):
        """Respond to the toiletpaper hit by an attacker."""
        if self.stats.toiletpaper_left > 0:
            # Decrement toiletpapers left and update scoreboard
            self.stats.toiletpaper_left -= 1
            self.sb.prep_toiletpapers()

            # Get rid of any remaining throws and attackers.
            self.attackers.empty()
            self.throws.empty()

            # Create a new fleet and center the toiletpaper.
            self._create_fleet()
            self.toiletpaper.center_toiletpaper()

            # Pause
            sleep(0.5)
        else:
            self.stats.game_active = False
            pygame.mouse.set_visible(True)


    def _update_screen(self):
        """Redraw the screen and image elements during each passs through the loop."""
        self.screen.fill(self.settings.bg_color)
        self.screen.blit(self.settings.bg_image.image, self.settings.bg_image.rect)
        self.toiletpaper.blitme()
        for throw in self.throws.sprites():
            throw.blitme()
        self.attackers.draw(self.screen)
        
        self.sb.show_score()
   
        if not self.stats.game_active:
            self.play_button.draw_button()
        
        pygame.display.flip()

    def _throw_paper(self):
        """Create a new throw and add it to the throws group."""
        if len(self.throws) < self.settings.throws_allowed:
            new_throw = Throw(self)
            self.throws.add(new_throw)

    def _create_attacker(self, attacker_number, row_number):
        """Create an attacker and place it in the row."""
        attacker = Attacker(self)
        attacker_width, attacker_height = attacker.rect.size
        attacker.x = attacker_width + 2 * attacker_width * attacker_number
        attacker.rect.x = attacker.x
        attacker.y = attacker.rect.height + 2* attacker.rect.height * row_number
        attacker.rect.y = attacker.y
        self.attackers.add(attacker)

    def _check_fleet_edges(self):
        """Respond appropriatly if any attackers have reached the edge."""
        for attacker in self.attackers.sprites():
            if attacker.check_edges():
                self._change_fleet_direction()
                break

    def _change_fleet_direction(self):
        """Drop the entire fleet and change the fleets direction."""
        for attacker in self.attackers.sprites():
            attacker.rect.y += self.settings.fleet_drop_speed
        self.settings.fleet_direction *= -1

    def _create_fleet(self):
        """Create a fleet of attackers."""
        # Create an attacker and find the numer of attackers in a row.
        # Spacing between each attacker is equal to one attecker width
        attacker = Attacker(self)
        attacker_width, attacker_height = attacker.rect.size
        available_space_x = self.settings.screen_width - (2 * attacker_width)
        number_attackers_x = available_space_x // (2 * attacker_width)

        # Determine the number of rows of attackers that fit on the screnn.
        toiletpaper_height = self.toiletpaper.rect.height
        available_space_y = self.settings.screen_height - (3 * attacker_height) - toiletpaper_height
        number_rows = available_space_y // (2 * attacker_height)

        # Create first row of attackers.
        for row_number in range (number_rows):
            for attacker_number in range (number_attackers_x):
                self._create_attacker(attacker_number, row_number)




if __name__ == "__main__":
    #Make a game instance, and run the game.
    bd = BuechsDeluxe()
    bd.run_game()