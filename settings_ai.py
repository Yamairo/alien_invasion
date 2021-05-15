import random
import pygame


class Settings():
    """"This class contains the settings for Alien Invasion"""

    def __init__(self):
        """"This initilizes the game's settings"""
        # Game settings
        infoObject = pygame.display.Info()
        self.screen_width = infoObject.current_w
        self.screen_height = infoObject.current_h
        self.bg_color = (0, 0, 0)

        # Ship setting
        self.ship_limit = 3

        # Bullet settings
        self.bullet_width = self.screen_width / 400
        self.bullet_height = self.screen_height / 100
        self.bullet_color = "white"
        self.bullets_allowed = 4
        self.enemy_bullets_allowed = 4
        self.enemy_bullet_color = "yellow"
        self.enemy_bullet_speed_factor = 7

        # Alien settings
        self.alien_speed_factor = 5
        self.fleet_drop_speed = 5

        # How quick does the game speed up
        self.speedup_scale = 1.1
        self.initialize_dynamic_settings()

        # How quick alien-point values increase
        self.score_scale = 1.5

    def initialize_dynamic_settings(self):
        """Initialize settings that change throughout the game"""
        self.ship_speed_factor = 15
        self.bullet_speed_factor = 25
        self.alien_speed_factor = 3
        self.fleet_scale = 0.1

        # Fleet direction of 1 represents right and -1 left
        direction = [-1, 1]
        self.fleet_direction = random.choice(direction)

        # Scoring
        self.alien_points = 100

    def increase_speed(self):
        """Increase speed settings and alien poin values"""
        self.ship_speed_factor *= self.speedup_scale
        self.bullet_speed_factor *= self.speedup_scale
        self.alien_speed_factor *= self.speedup_scale
        self.alien_points = int(self.alien_points * self.score_scale)
