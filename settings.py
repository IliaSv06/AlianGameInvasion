import pygame

class Settings():
    def __init__(self):
        '''Инициализирует настройки игры'''
        #Параметры экрана
        self.background = pygame.image.load('images/starfield.png')
        self.background_rect = self.background.get_rect()
        self.screen_width=800
        self.screen_height=600
        self.bg_color=(0, 0, 0)
        self.FPS = 120
        self.last_timer = 0
        #параметры пули 
        self.bullet_with=3
        self.bullet_height=15
        self.bullet_color=(250, 0, 250)
        self.bullets_allowed=6
        #параметры пришельца
        self.fleet_drop_speed=10 #скорость смещения вниз
        #статистика игры
        self.ship_limit=3 #Кол-во попыток        
        self.speed_scale=1.1 # параметр увеличения скорости игры
        self.score_scale = 1.5  # темп роста кол-ва очков
        self.initialize_dynamic_settings() # инициализирует изменяемые параметры
        self.delete_alien = 3
        self.sound_boom = pygame.mixer.Sound('music/boom.mp3') #звук - бум
    def initialize_dynamic_settings(self):
        '''Инициализирует изменяемые настройки'''
        self.alien_speed_factor=1
        self.alien_speed_x = 1.5
        self.ship_speed_factor=3
        self.bullet_speed_factor=4
        self.fleet_direction=1 #направление смещения вправо(1)/влево(-1)
        self.alien_point = 50 # параметры изменения кол-ва очков
        self.min_objects = 3
        self.flag_fire = False

    def increase_speed(self):
        '''Увеличивает параметры скорости стоимоти очков'''
        self.alien_speed_factor*=self.speed_scale
        self.alien_speed_x*=self.speed_scale
        self.ship_speed_factor*=self.speed_scale
        self.bullet_speed_factor*=self.speed_scale
        self.alien_point = int(self.alien_point * self.score_scale)