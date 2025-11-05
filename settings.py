from parms_const import *
class Settings:
    # класс для хранениея всех настроект игры
    def __init__(self):
        self.screen_width = SCREEN_WIDTH
        self.screen_height = SCREEN_HEIGHT
        # self.bg_color = BACKGOUD_COLOR
        self.bg_image_path = 'images/background.bmp'
        self.ship_speed = 0.5
