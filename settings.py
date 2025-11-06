from parms_const import *
class Settings:
    # класс для хранениея всех настроект игры
    def __init__(self):
        self.screen_width = SCREEN_WIDTH
        self.screen_height = SCREEN_HEIGHT
        # self.bg_color = BACKGOUD_COLOR  # добавил картинку космоса
        self.bg_image_path = 'images/background.bmp'
        self.ship_speed = 0.5
        # создание снарядов
        self.bullet_speed = 1
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (135, 206, 235)  # подумай, что бы торпеды летали
        self.bullets_allowed = 3  # ограничение количества снарядов
