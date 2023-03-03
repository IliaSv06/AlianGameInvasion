class GameStats():
    '''Статистика игры'''
    def __init__(self, ai_setting):
        self.ai_setting=ai_setting
        self.reset_stats()
        self.game_active=False
        self.high_score = 0 # игоровой рекорд
        self.first_time = 0
    def reset_stats(self):
        self.limit_object = 30
        self.ship_left=self.ai_setting.ship_limit
        self.score = 0 # игоровой счет
        self.level = 1  # уровень