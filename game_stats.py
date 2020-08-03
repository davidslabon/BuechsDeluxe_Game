class GameStats:
    """Track Statistics for Buechs Deluxe."""

    def __init__(self, bd_game):
        """Initialize statistics."""
        self.settings = bd_game.settings
        self.reset_stats()

    def reset_stats(self):
        """Initialize statistics that can change during the game."""
        self.toiletpaper_left = self.settings.toiletpaper_limit