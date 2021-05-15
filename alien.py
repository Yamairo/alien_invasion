import pygame
from pygame.sprite import Sprite
import random


class Alien(Sprite):
    """A class to represent a single alien in the fleet"""

    def __init__(self, ai_settings, screen):
        """Initialize the alien and set its starting position."""
        super().__init__()
        self.screen = screen
        self.ai_settings = ai_settings

        # load the alien image and set its rect attribute.
        image_number = random.randint(1, 4)
        w, h = screen.get_size()
        if image_number == 1:
            self.image = pygame.image.load('images/alien.png').convert_alpha()
            self.image = pygame.transform.scale(self.image, (w // 40, h // 23))
        if image_number == 2:
            self.image = pygame.image.load(
                'images/alien 2.png').convert_alpha()
            ai_settings = self.ai_settings
            self.image = pygame.transform.scale(self.image, (w // 40, h // 23))
        if image_number == 3:
            self.image = pygame.image.load(
                'images/alien 3.png').convert_alpha()
            ai_settings = self.ai_settings
            self.image = pygame.transform.scale(self.image, (w // 40, h // 23))
        if image_number == 4:
            self.image = pygame.image.load(
                'images/alien 4.png').convert_alpha()
            ai_settings = self.ai_settings
            self.image = pygame.transform.scale(self.image, (w // 40, h // 23))
        if image_number == 5:
            self.image = pygame.image.load('images/alien.png').convert_alpha()
            ai_settings = self.ai_settings
            self.image = pygame.transform.scale(self.image, (w // 40, h // 23))
        self.rect = self.image.get_rect()

        # start each new alien near the top left of the screen
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        # store the alien's exact position.
        self.x = float(self.rect.x)

    def blitme(self):
        """Draw the alien at its current location"""
        self.screen.blit(self.image, self.rect)

    def update(self):
        """Move the alien right"""
        self.x += (self.ai_settings.alien_speed_factor *
                   self.ai_settings.fleet_direction)
        self.rect.x = self.x

    def check_edges(self):
        """"Return True if alien is at the edge of the screen"""
        screen_rect = self.screen.get_rect()
        if self.rect.right >= screen_rect.right:
            return True
        elif self.rect.left <= 0:
            return True
