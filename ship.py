import pygame
from pygame.sprite import Sprite
class Ship(Sprite):
    def __init__(self, screen, ai_settings):
        '''Инициализация корабля и задние позиции'''
        super(Ship, self).__init__()
        self.screen=screen
        self.ai_settings=ai_settings
        self.image=pygame.image.load('images/playerShip1_blue.png')
        self.image=pygame.transform.scale(self.image, (60, 70))
        self.rect=self.image.get_rect()
        self.screen_rect=screen.get_rect()

        self.rect.centerx=self.screen_rect.centerx
        self.rect.bottom=self.screen_rect.bottom
        self.center=float(self.rect.centerx)
        self.y=float(self.rect.y)
        self.moving_right=False
        self.moving_left=False
        self.moving_top=False
        self.moving_bottom=False
    '''Ресует корабль в текущей позиции'''
    def blitme(self):
        self.screen.blit(self.image, self.rect)

    def update(self):
        '''Обновляет позицию корабля с учетом флага'''
        if self.moving_right and self.rect.right < self.screen_rect.right:
                self.center+=self.ai_settings.ship_speed_factor
        
        if self.moving_left and self.rect.left > 0 :
                self.center-=self.ai_settings.ship_speed_factor
        
        if self.moving_top and self.rect.top > 0 :
            self.y-=self.ai_settings.ship_speed_factor

        if self.moving_bottom and self.rect.bottom < self.screen_rect.bottom:
            self.y+=self.ai_settings.ship_speed_factor
        self.rect.centerx=self.center
        self.rect.y=self.y
    
    def center_ship(self):
        '''Размещает объект в центре нижнего угла экрана'''
        self.center=self.screen_rect.centerx
        self.y=self.ai_settings.screen_height-100

