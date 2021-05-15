import pygame.font
from pygame.sprite import Group
from hearts import Heart


class Scoreboard():
    """A class to report scoring information."""

    def __init__(self, ai_settings, screen, stats):
        """Initialize scorekeeping attributes."""
        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.ai_settings = ai_settings
        self.stats = stats

        # Font settings for scoring information.
        self.text_color = (200, 200, 200)
        self.font = pygame.font.Font('__pycache__/invasion.TTF', 30)

        # Prepare the initial score images.
        self.prep_score()
        self.prep_high_score()
        self.prep_highest_level()
        self.prep_level()
        self.prep_hearts()

    def prep_score(self):
        """Turn the score into a rendered image."""
        rounded_score = int(round(self.stats.score, -1))
        score_str = "SCORE: " + "{:,}".format(rounded_score)
        self.score_image = self.font.render(
            score_str, True, self.text_color, self.ai_settings.bg_color)

        # Display the score at the top right of the screen.
        self.score_rect = self.score_image.get_rect()
        self.score_rect.left = self.screen_rect.left + 20
        self.score_rect.top = 20

    def prep_high_score(self):
        """Turn the high score into a rendered image."""
        high_score = int(round(self.stats.high_score, -1))
        high_score_str = "HIGH SCORE: " + "{:,}".format(high_score)
        self.high_score_image = self.font.render(
            high_score_str, True, self.text_color, self.ai_settings.bg_color)

        # Center the high score at the top fo the screen.
        self.high_score_rect = self.high_score_image.get_rect()
        self.high_score_rect.centerx = self.screen_rect.centerx
        self.high_score_rect.top = self.score_rect.top

    def prep_highest_level(self):
        """Turn the high score into a rendered image."""
        highest_level = int((self.stats.highest_level))
        highest_level_str = "HIGHEST LEVEL: " + "{:,}".format(highest_level)
        self.highest_level_image = self.font.render(highest_level_str,
                                                    True, self.text_color,
                                                    self.ai_settings.bg_color)

        # Center the high score at the top fo the screen.
        self.highest_level_rect = self.highest_level_image.get_rect()
        self.highest_level_rect.centerx = self.screen_rect.centerx
        self.highest_level_rect.top = self.score_rect.bottom + 5

    def prep_level(self):
        """Turn the level into a rendered image."""
        level = "LEVEL: " + str(self.stats.level)
        self.level_image = self.font.render(
            level, True, self.text_color, self.ai_settings.bg_color)

        # Position the level below the score.
        self.level_rect = self.level_image.get_rect()
        self.level_rect.left = self.score_rect.left
        self.level_rect.top = self.score_rect.bottom + 5

    def prep_hearts(self):
        '''show how many ships you have left'''
        self.heart = Group()
        for hearts_number in range(self.stats.hearts_left):
            heart = Heart(self.ai_settings, self.screen)
            ai_settings = self.ai_settings
            heart.rect.x = ai_settings.screen_width - \
                ai_settings.screen_width * 0.22 + hearts_number * \
                heart.rect.width
            heart.rect.y = 0
            self.heart.add(heart)

    def show_score(self):
        """Draw scores and ships to the screen."""
        self.screen.blit(self.score_image, self.score_rect)
        self.screen.blit(self.high_score_image, self.high_score_rect)
        self.screen.blit(self.highest_level_image,
                         self.highest_level_rect
                         )
        self.screen.blit(self.level_image, self.level_rect)
        self.heart.draw(self.screen)


class Quit_State():
    def __init__(self, ai_settings, screen):
        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.ai_settings = ai_settings

        # Font settings for scoring information.
        self.text_color = (0, 0, 0)
        self.font = pygame.font.SysFont(None, 40)
        self.quit_statement(ai_settings)

    def quit_statement(self, ai_settings):
        quit_state = "'ESC' to quit"
        self.font = pygame.font.SysFont(None, 20)
        self.quit_state = self.font.render(
            quit_state, True, self.text_color, (71, 230, 44))
        self.quit_rect = self.quit_state.get_rect()
        self.quit_rect.center = self.screen_rect.center
        self.quit_rect.centery = self.screen_rect.centery + 135

    def show_quit(self):
        self.screen.blit(self.quit_state, self.quit_rect)
