import pygame
from pygame.sprite import Sprite


class Heart(Sprite):

    def __init__(self, ai_settings, screen):
        super().__init__()
        self.screen = screen
        self.ai_settings = ai_settings
        self.image = pygame.image.load('images/heart.png').convert_alpha()
        self.rect = self.image.get_rect()
        x = ai_settings.screen_width
        y = ai_settings.screen_height
        self.rect.topright = (x, y)
