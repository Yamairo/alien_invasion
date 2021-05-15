import pygame
from ship_ai import Ship
from button import Button
from button import Game_Over
import game_functions as gf
from settings_ai import Settings
from pygame.sprite import Group
from gamestats import GameStats
from scoreboard import Scoreboard
from scoreboard import Quit_State

pygame.mixer.init()
music_file = 'music/Arcade-Puzzler.mp3'
pygame.mixer.music.load(music_file)
pygame.mixer.music.play(-1)
pygame.mixer.music.set_volume(0)


def run_game():
    # Initialize pygame, settings, and screen object.
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
    pygame.display.set_caption("Alien Invasion")

    # Set FPS
    FPS = 144
    clock = pygame.time.Clock()

    # Make a ship, a group of bullets, and a group of aliens.
    ship_ai = Ship(ai_settings, screen)
    bullets = Group()

    enemy_bullets = Group()
    aliens = Group()

    # Create an instance to store game statistics, a quit statement
    # and create a scoreboard.
    stats = GameStats(ai_settings)
    sb = Scoreboard(ai_settings, screen, stats)
    qs = Quit_State(ai_settings, screen)

    # Create the fleet of aliens.
    gf.create_fleet(ai_settings, screen, ship_ai, aliens, stats)

    # Make the Play and Game Over button.
    play_button = Button(ai_settings, screen, "CLICK HERE TO START THE GAME")
    game_over = Game_Over(ai_settings, screen, "GAME OVER")

    # Load the high score.
    gf.load_score(stats)
    sb.prep_high_score()
    sb.prep_highest_level()
    sb.show_score()

    # Start the main loop for the game.
    while True:
        clock.tick(FPS)
        gf.check_events(ai_settings, screen, stats, play_button, ship_ai,
                        aliens, bullets, sb, enemy_bullets)
        if stats.game_active:
            print(stats.level)
            ship_ai.update()
            gf.update_bullets(ai_settings, screen, stats, sb,
                              ship_ai, aliens, bullets)
            gf.update_enemy_bullets(ai_settings, screen, stats, sb, ship_ai,
                                    aliens, enemy_bullets)
            gf.update_aliens(ai_settings, stats, sb, screen, ship_ai, aliens,
                             bullets, enemy_bullets, game_over)
        if not stats.game_active:
            game_over.draw_button()
        gf.update_screen(ai_settings, screen, stats, sb, ship_ai, aliens,
                         bullets, play_button, qs, enemy_bullets, game_over)


run_game()
