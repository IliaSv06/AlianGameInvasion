import pygame
from pygame.sprite import Group
from settings import Settings
from ship import Ship
import game_functions as gf
from game_stats import GameStats
from button import Button
from scoreboard import Scoreboard


def run_game():
    '''Инициализирует окно'''
    pygame.init()
    ai_setting = Settings()
    pygame.time.set_timer(pygame.USEREVENT, 1500)
    pygame.time.set_timer(pygame.NUMEVENTS, 2)
    screen = pygame.display.set_mode((ai_setting.screen_width, ai_setting.screen_height))
    sound1 = pygame.mixer.Sound('music/sfx_laser1.ogg')
    stats = GameStats(ai_setting)
    score = Scoreboard(ai_setting, screen, stats)
    ship = Ship(screen, ai_setting)
    play_button = Button(ai_setting, screen, 'Play')
    bullets = Group() #создание группы для хранения пуль
    aliens = Group()
    pygame.display.set_caption('Alien invasion')
    clock = pygame.time.Clock()
    animation_object = Group()
    '''Цикл событий'''
    while True:
        clock.tick(ai_setting.FPS)
        gf.check_events(ship, bullets, ai_setting, screen, play_button, stats, aliens, score, sound1)
        if stats.game_active:
            ship.update()
            bullets.update()
            #Проресовка экрана
            gf.update_bullets(bullets, aliens, ai_setting, screen, ship, score, stats ,animation_object)
            gf.update_alien(aliens, ship, ai_setting, stats, screen, bullets, score, animation_object)
        gf.update_screen(ship, screen, ai_setting, bullets, aliens, play_button, stats, score, animation_object, sound1)

run_game()
