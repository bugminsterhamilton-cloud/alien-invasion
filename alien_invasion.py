import pygame
import sys
from ship import Ship
from settings import Settings


class AlienInvasion():
    '''класс управления ресурсами игры'''

    def __init__(self):
        """Инициализирует игру, создает ресурсы"""
        pygame.init()
        self.settings = Settings()

        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption('Alien Invasion')
        self.ship = Ship(self)

        self.bg_image = pygame.image.load(self.settings.bg_image_path)
        self.bg_image = pygame.transform.scale(self.bg_image,(self.settings.screen_width,self.settings.screen_height))

    def run_game(self):
        """запуск основного цикла игры"""
        while True:
            # отслеживание событий клавиатуры и мышки
            self._check_events()
            self._update_screen()

    # Рефакторинг: 2 249 стр.
    def _check_events(self):
        """Обрабатывает нажатия клавиш и события мыши"""
        for event in pygame.event.get():  # для получения доступа к событиям
            if event.type == pygame.QUIT:
                sys.exit()

    # Рефакторинг: 3
    def _update_screen(self):
        """Отображает изображение на экране и новый экран"""
        self.screen.blit(self.bg_image, (0, 0))  # прорисовывается экран
        self.ship.blitme()
        # отображение последнего прорисованного экрана
        pygame.display.flip()

if __name__ == '__main__':
    # создание экземпляра и запуск игры
    ai = AlienInvasion()
    ai.run_game()