import pygame
from pygame.sprite import Sprite


class Alien(Sprite):
    """класс, выводящий одного пришельца"""
    def __init__(self, ai_game):
        """инициализация пришельца и задача начальной позиции"""
        super().__init__()
        self.screen = ai_game.screen

        # загрузка картинки и назначение атрибута rect
        original_image = pygame.image.load('images/alien_1.bmp')
        new_width = 80
        new_height = 80
        scaled_image = pygame.transform.scale(original_image, (new_width, new_height))  # это не из книги
        self.image = pygame.transform.rotate(scaled_image, 180)  # это не из книги
        self.rect = self.image.get_rect()

        # каждый новый пришелец появляется в левом верхнем углу
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        # сохраниние точной горизонтальной позиции пришельца
        self.x = float(self.rect.x)