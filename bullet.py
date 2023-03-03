import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
    def __init__(self, ai_settings, screen, ship):
        '''Создает объект пули в текущей позиции корабля'''
        super(Bullet, self).__init__()
        self.screen=screen
        # Создание пули в позиции (0,0) и назначение правильной позиции

        self.image = pygame.image.load('images/laserBlue01.png')
        self.rect = self.image.get_rect()
        self.rect.centerx=ship.rect.centerx
        self.rect.top=ship.rect.top
        self.y=float(self.rect.y)

        self.color=ai_settings.bullet_color
        self.speed_factor=ai_settings.bullet_speed_factor

    def update(self):
        self.y-=self.speed_factor
        self.rect.y=self.y
    
    def draw_bullet(self):
        self.screen.blit(self.image, self.rect)

