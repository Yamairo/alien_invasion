import pygame
from pygame.sprite import Sprite
import random


class Ship(Sprite):

    def __init__(self, ai_settings, screen):
        super().__init__()
        self.screen = screen
        self.ai_settings = ai_settings
        w, h = screen.get_size()
        image_number = random.randint(1, 4)
        if image_number == 1:
            self.image = pygame.image.load('images/ship.bmp').convert_alpha()
            self.image = pygame.transform.scale(self.image, (w // 18, h // 10))
        if image_number == 2:
            self.image = pygame.image.load('images/ship.png').convert_alpha()
            self.image = pygame.transform.scale(self.image, (w // 18, h // 10))
        if image_number == 3:
            self.image = pygame.image.load(
                'images/ship.bmg.bmp').convert_alpha()
            self.image = pygame.transform.scale(self.image, (w // 18, h // 10))
        if image_number == 4:
            self.image = pygame.image.load('images/ship2.bmp').convert_alpha()
            self.image = pygame.transform.scale(self.image, (w // 18, h // 10))
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom
        self.center = float(self.rect.centerx)
        self.moving_right = False
        self.moving_left = False

    def update(self):

        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.center += self.ai_settings.ship_speed_factor
        if self.moving_left and self.rect.left > 0:
            self.center -= self.ai_settings.ship_speed_factor
        self.rect.centerx = self.center

    def blitme(self):
        self.screen.blit(self.image, self.rect)

    def center_ship(self):
        self.center = self.screen_rect.centerx
