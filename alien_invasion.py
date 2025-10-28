import pygame
import sys

from parms_const import SCREEN_WIDTH, SCREEN_HEIGHT
from settings import Settings
from ship import Ship

class AlienInvasion():
    '''класс управления ресурсами игры'''
    def __init__(self):
        # инициализирует игру и создает ресурсы
        pygame.init()
        self.settings = Settings()  # класс Settings импортирован в
        # основной файл.
        # Создан экземпляр класса Settings и сохранен в self.settings

        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pygame.display.set_caption('Alien Invasion')
        self.ship = Ship(self)  # в книге Ship(screen)

    def run_game(self):
        '''запуск основного цикла игры'''
        while True:
            # Отслеживание событий клавиатуры и мыши
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
            # прорисовывает экран при каждом цикле
            self.screen.fill(self.settings.bg_color)
            self.ship.blitme()  # при каждом проходе цикла перерисовывается экран
            pygame.display.flip()

if __name__ == '__main__':
    # создание экземпляра и запуск игры
    ai = AlienInvasion()
    ai.run_game()