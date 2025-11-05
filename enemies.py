import pygame

class Enemies():
    '''класс управления врагами'''
    def __init__(self, ai_game):  # self и
        # ссылку на текущий экземдпляр класса.
        # Как класс ship получает доступ к игровым ресурсам? через ai_game?
        '''создает корабль и задает начальную позицию'''
        self.screen = ai_game.screen  # тут экран присваевается атрибуту Ship.
        # Легко обращаться во всех модулях класса
        self.settings = ai_game.settings  # принимаем экземпляр игры
        self.screen_rect = ai_game.screen.get_rect()  # получаем экран из игры
        # загружает изображение корабля и получает прямоугольник
        self.image = pygame.image.load('images/ufo.bmp')  # метод передает местопложение корабля
        self.rect = self.image.get_rect()  # метод вызывается для позиционирования объекта. Доступны оси x/y

        original_image = pygame.image.load('images/ufo.bmp')
        # Уменьшаем в 2 раза (50% от оригинала)
        scale_factor = 0.01
        original_rect = original_image.get_rect()
        new_width = int(original_rect.width * scale_factor)
        new_height = int(original_rect.height * scale_factor)
        self.image = pygame.transform.scale(original_image,
                                            (new_width, new_height))
        self.rect = self.image.get_rect()
        self.rect.midtop = self.screen_rect.midtop

        # Размещаем по центру вверху
        self.rect.midtop = self.screen_rect.midtop

    def blitme(self):
        self.screen.blit(self.image, self.rect)
        self.rect.midbottom = self.screen_rect.midbottom  # выравнивание объекта по центру

    def blitme(self):
        # рисует корабль в текущей позиции
        self.screen.blit(self.image, self.rect)