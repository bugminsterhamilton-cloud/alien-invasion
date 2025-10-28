import pygame

class Ship():
    '''класс управления кораблем'''
    def __init__(self, ai_game):  # self и
        # ссылку на текущий экземдпляр класса.
        # Как класс ship получает доступ к игровым ресурсам? через ai_game?
        '''создает корабль и задает начальную позицию'''
        self.screen = ai_game.screen  # тут экран присваевается атрибуту Ship.
        # Легко обращаться во всех модулях класса
        self.settings = ai_game.settings  # принимаем экземпляр игры
        self.screen_rect = ai_game.screen.get_rect()  # получаем экран из игры
        # загружает изображение корабля и получает прямоугольник
        self.image = pygame.image.load('images/ship.bmp')  # метод передает местопложение корабля
        self.rect = self.image.get_rect()  # метод вызывается для позиционирования объекта. Доступны оси x/y

        self.rect.midbottom = self.screen_rect.midbottom  # выравнивание объекта по центру

    def blitme(self):
        # рисует корабль в текущей позиции
        self.screen.blit(self.image, self.rect)