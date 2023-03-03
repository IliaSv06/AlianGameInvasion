import pygame
from pygame.sprite import Sprite
from random import randint, randrange

class Alien(Sprite):
    def __init__(self, ai_setting, screen):
        super(Alien, self).__init__()
        self.screen=screen
        rect_screen = self.screen.get_rect()
        self.ai_setting=ai_setting
        '''Инициализация объекта'''
        self.image=pygame.image.load('images/alien_version1.1.png')
        self.image = pygame.transform.scale(self.image, (80, 80))
        self.rect=self.image.get_rect()
        # Каждый новый пришелец появляется в левом верхнем углу экрана, c отступом
        self.rect.x = randint(rect_screen.left + 100, rect_screen.right - 100)
        self.rect.y = 0
        self.y=float(self.rect.y)
        self.x=float(self.rect.x)
        self.fleet_direction = randrange(-1, 2, 2)
    def blitme(self):
        self.screen.blit(self.image, self.rect)

    def check_edges(self):
        '''Определяет где находится пришелец относительно краев экрана'''
        screen_rect=self.screen.get_rect()
        if self.rect.right >= screen_rect.right or self.rect.left <= screen_rect.left:
            self.fleet_direction*=-1

    def update(self):
        self.x = self.x + self.ai_setting.alien_speed_x  * self.fleet_direction
        self.y += self.ai_setting.alien_speed_factor
        self.rect.x=self.x
        self.rect.y = self.y
