import pygame.font
from pygame.sprite import Group
from toilet_paper import ToiletPaper

class Scoreboard:
    """A class to report scoring information."""

    def __init__(self, bd_game):
        """Initialize scorekeeping attributes."""
        self.bd_game = bd_game
        self.screen = bd_game.screen 
        self.screen_rect = self.screen.get_rect()
        self.settings = bd_game.settings
        self.stats = bd_game.stats
        

        # Font Settings for scoring information.
        self.text_color = (30, 30, 30)
        self.font = pygame.font.SysFont(None, 48)

        # Prepare the initial score images.
        self.prep_score()
        self.prep_high_score()
        self.prep_level()
        self.prep_toiletpapers()

    def prep_score(self):
        """Turn the score into a rendered image."""
        rounded_score = round(self.stats.score, -1)
        score_str = "{:,}".format(rounded_score)
        self.score_image = self.font.render(score_str, True, self.text_color, self.settings.bg_image)


        # Display the score at the top right of the screen.
        self.score_rect = self.score_image.get_rect()
        self.score_rect.right = self.screen_rect.right - 20
        self.score_rect.top = 20

    def prep_high_score(self):
        """Turn the high score into a rendered image."""
        high_score = round(self.stats.high_score, -1)
        high_score_str = "{:,}".format(high_score)
        self.high_score_image = self.font.render(high_score_str, True, self.text_color, self.settings.bg_image)

        # Display the score at the top right of the screen.
        self.high_score_rect = self.high_score_image.get_rect()
        self.high_score_rect.centerx = self.screen_rect.centerx
        self.high_score_rect.top = self.score_rect.top

    def prep_level(self):
        """Turn the level into a rendered image."""
        level_str = str(self.stats.level)
        self.level_image = self.font.render(level_str, True, self.text_color, self.settings.bg_image)

        # Display the score at the top right of the screen.
        self.level_rect = self.level_image.get_rect()
        self.level_rect.right = self.score_rect.right
        self.level_rect.top = self.score_rect.bottom + 10

    def prep_toiletpapers(self):
        """Show how many paper rolls are left."""
        self.toiletpapers = Group()
        for paper_numer in range(self.stats.toiletpaper_left):
            toiletpaper = ToiletPaper(self.bd_game)
            toiletpaper.rect.x = 10 + paper_numer * toiletpaper.rect.width
            toiletpaper.rect.y = 10
            self.toiletpapers.add(toiletpaper)

    def check_high_score(self):
        """Check to see if there's a new highscore."""
        if self.stats.score > self.stats.high_score:
            self.stats.high_score = self.stats.score
            self.prep_high_score()

    def show_score(self):
        """Draw scores, level and paper rolls to the screen."""
        self.screen.blit(self.score_image, self.score_rect)
        self.screen.blit(self.high_score_image, self.high_score_rect)
        self.screen.blit(self.level_image, self.level_rect)
        self.toiletpapers.draw(self.screen)