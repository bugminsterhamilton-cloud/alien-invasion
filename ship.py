import pygame

class Ship():
    '''класс управления кораблем'''
    def __init__(self, ai_game):
        '''создает корабль и задает начальную позицию'''
        self.screen = ai_game.screen  # тут экран присваевается атрибуту Ship.
        self.settings = ai_game.settings  # создается атрибут, что бы он мог использоваться в update()
        self.screen_rect = ai_game.screen.get_rect()  # получаем экран из игры
        # загружает изображение корабля и получает прямоугольник
        self.image = pygame.image.load('images/ship.bmp')  # метод передает местопложение корабля
        self.rect = self.image.get_rect()  # метод вызывается для позиционирования объекта. Доступны оси x/y
        # каждый новый корабль появляется у нижнего края экрана
        self.rect.midbottom = self.screen_rect.midbottom  # выравнивание объекта по центру

        self.x = float(self.rect.x)  # сохранение вещественной координаты центра кораблчя. што блядь???
        self.moving_right = False  # флаг перемещения (клавиша нажата -> True, клавишу отпустили -> False)
        self.moving_left = False

    def update(self):
        """Обновляет позицию корабля с учетом флага"""
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += self.settings.ship_speed  # логика перемещения
            # (+ вещественная координата центра корабля) + ограничение выхода за край экрана
        elif self.moving_left and self.rect.left > 0:
            self.x -= self.settings.ship_speed  # см. ком. 23-24 стр.

        self.rect.x = self.x  # обновление атрибута rect на основании self.x

    def blitme(self):
        """рисует корабль в текущей позиции"""
        self.screen.blit(self.image, self.rect)