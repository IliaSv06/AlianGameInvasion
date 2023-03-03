import pygame.font

class Button():
    def __init__(self, ai_setting, screen, msg):
        self.screen=screen
        self.screen_rect=screen.get_rect()

        self.width, self.height = 200, 50
        self.bt_color = (0, 255, 0)
        self.text_color = (255, 255, 255)
        self.font = pygame.font.SysFont(None, 48)
        #создаем прямоугольник кнопки и задаем кординаты
        self.rect = pygame.Rect(0, 0, self.width, self.height)
        self.rect.center = self.screen_rect.center

        #создание сообщение
        self.prep_msg(msg)

    def prep_msg(self, msg):
        '''Создание текста кнопки и ее кординаты'''
        self.msg_image = pygame.image.load('images/button_play.png')
        self.msg_image = pygame.transform.scale(self.msg_image, (400, 400))
        self.msg_image_rect = self.msg_image.get_rect()
        self.msg_image_rect.center = self.rect.center
        
    def draw_button(self):
        '''Отображает кнопку и ее текст на экран'''
        #self.screen.fill(self.bt_color, self.rect)
        self.screen.blit(self.msg_image, self.msg_image_rect)
