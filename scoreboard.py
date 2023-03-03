import pygame.font
from ship import Ship
from pygame.sprite import Group
class Scoreboard():
    def __init__(self, ai_setting, screen, stats):
        '''Инициализация счета'''
        self.screen = screen
        self.screen_rect = self.screen.get_rect()
        self.ai_setting = ai_setting
        self.stats = stats 
        self.ships = Group()
        self.font = pygame.font.SysFont(None, 49)
        self.txt_color = (210, 210, 210)
        self.prep_score()
        self.prep_high_score()
        self.make_level()
       # self.make_ships()

    def prep_score(self):
        '''Преобразования счета в графическое изображение'''
        self.score = round(self.stats.score, -1)
        self.score = '{:,}'.format(self.score)
        self.image = self.font.render(self.score, True, self.txt_color, self.ai_setting.bg_color)

        # определение позиции счета
        self.image_rect = self.image.get_rect()
        self.image_rect.right = self.screen_rect.right - 20
        self.image_rect.top = 20

    def prep_high_score(self):
        '''Преобразование РЕКОРДА в графическое ихображение'''
        self.high_score = round(self.stats.high_score, -1)
        self.high_score = '{:,}'.format(self.high_score)
        self.high_score_image = self.font.render(self.high_score, True, self.txt_color, self.ai_setting.bg_color)

        # определение позиции счета
        self.high_image_rect = self.high_score_image.get_rect()
        self.high_image_rect.centerx = self.screen_rect.centerx
        self.high_image_rect.top = 20

    def make_level(self):
        '''Создает счетчик уровней'''
        self.score_level = str(self.stats.level)
        self.image_level = self.font.render(self.score_level, True, self.txt_color, self.ai_setting.bg_color)

        # определение позиции счета
        self.image_rect_level = self.image_level.get_rect()
        self.image_rect_level.right = self.screen_rect.right - 20
        self.image_rect_level.top = self.image_rect.bottom + 10

    def make_ships(self):
        '''Вносит кол-во оставшихся кораблей в группу '''
        self.ships = Group()
        for number_ship in range(self.stats.ship_left):
            ship = Ship(self.screen, self.ai_setting)
            # задание кординаты кораблям
            ship.rect.x = 10 + number_ship * ship.rect.width
            ship.rect.y = self.screen_rect.height - 80
            self.ships.add(ship)

    def make_text_level_number(self):
        self.text_level = f'Lavel {self.stats.level}'
        self.image_level_number = self.font.render(self.text_level, True, self.txt_color, self.ai_setting.bg_color)
        self.rect_image_level_n = self.image_level_number.get_rect()
        self.rect_image_level_n.center = self.screen_rect.center

    def draw_text_level_n(self):
        self.screen.blit(self.image_level_number, self.rect_image_level_n)

    def draw_score(self):
        '''Отображение счета на экране'''
        self.screen.blit(self.image, self.image_rect)
        self.screen.blit(self.high_score_image, self.high_image_rect)
        self.screen.blit(self.image_level, self.image_rect_level)
        self.ships.draw(self.screen)