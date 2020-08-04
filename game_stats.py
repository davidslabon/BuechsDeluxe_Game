class GameStats:
    """Track Statistics for Buechs Deluxe."""

    def __init__(self, bd_game):
        """Initialize statistics."""
        self.settings = bd_game.settings
        self.reset_stats()

        # High score should never be reset.
        self.high_score = 0

        # Start Buechs Deluxe in active state.
        self.game_active = False

    def reset_stats(self):
        """Initialize statistics that can change during the game."""
        self.toiletpaper_left = self.settings.toiletpaper_limit
        self.score = 0
        self.level = 1