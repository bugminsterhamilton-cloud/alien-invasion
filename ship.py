import pygame

class Ship():
    '''класс управления кораблем'''
    def __init__(self, ai_game):
        '''создает корабль и задает начальную позицию'''
        self.screen = ai_game.screen  # тут экран присваевается атрибуту Ship.
        self.screen_rect = ai_game.screen.get_rect()  # получаем экран из игры

        # загружает изображение корабля и получает прямоугольник
        self.image = pygame.image.load('images/ship.bmp')  # метод передает местопложение корабля
        self.rect = self.image.get_rect()  # метод вызывается для позиционирования объекта. Доступны оси x/y

        # каждый новый корабль появляется у нижнего края экрана
        self.rect.midbottom = self.screen_rect.midbottom  # выравнивание объекта по центру

        self.moving_right = False  # флаг перемещения (клавиша нажата -> True, клавишу отпустили -> False)
        self.moving_left = False

    def update(self):
        """Обновляет позицию корабля с учетом флага"""
        if self.moving_right:
            self.rect.x += 1  # шаг движения вправо (логика перемещения)
        elif self.moving_left:
            self.rect.x -= 1  # шаг движения влево (логика перемещения)

    def blitme(self):
        """рисует корабль в текущей позиции"""
        self.screen.blit(self.image, self.rect)