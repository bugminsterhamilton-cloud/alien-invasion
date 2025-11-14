from parms_const import *
from settings import *

class Settings:
    # класс для хранениея всех настроект игры
    def __init__(self):
        self.screen_width = SCREEN_WIDTH
        self.screen_height = SCREEN_HEIGHT
        # self.bg_color = BACKGOUD_COLOR  # добавил картинку космоса
        self.bg_image_path = 'images/background.bmp'
        self.ship_speed = SHIP_SPEED
        # создание снарядов
        self.bullet_speed = BULLET_SPEED
        self.bullet_width = BULLET_WIDTH
        self.bullet_height = BULLET_HEIGHT
        self.bullet_color = BULLET_COLOR  # подумай, что бы торпеды летали
        self.bullets_allowed = BULLET_ALLOWED  # ограничение количества снарядов
        self.alien_speed = 1.0  # настройка пришельцев началась тут (используется в реализации update())
        self.fleet_drop_speed = 10
        self.fleet_direction = 1  # 1 - движение вправо, а -1 - влево
