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

        self.screen = pygame.display.set_mode((0,0), pygame.FULLSCREEN)  # запуск в полноэкранном режиме
        self.settings.screen_width = self.screen.get_rect().width
        self.settings.screen_height = self.screen.get_rect().height

        # self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption('Alien Invasion')
        self.ship = Ship(self)

        self.bg_image = pygame.image.load(self.settings.bg_image_path)
        self.bg_image = pygame.transform.scale(self.bg_image,(self.settings.screen_width,self.settings.screen_height))

    def run_game(self):
        """запуск основного цикла игры"""
        while True:
            # отслеживание событий клавиатуры и мышки
            self._check_events()  # Обновляет флаги
            self.ship.update()  # Двигает корабль по флагам
            self._update_screen()  # Отрисовывает новую позицию

    # Рефакторинг: 2 (249 стр.)
    def _check_events(self):
        """Обрабатывает нажатия клавиш и события мыши"""
        for event in pygame.event.get():  # для получения доступа к событиям
            if event.type == pygame.QUIT:
                sys.exit()
            # уезжает за пределы экрана и не останавливается
            elif event.type == pygame.KEYDOWN:  # начал отсюда 5.11.25 (движение работает)
                self._check_keydown_events(event)  #???
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)

    def _check_keydown_events(self, event):
        """реагигирует на нажатие клавиш"""
        # right:
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = True  # ВКЛЮЧАЕТ движение
        # left:
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = True
        elif event.key == pygame.K_ESCAPE:  # добавил кнопки выхода из игры
            sys.exit()
        elif event.key == pygame.K_UP:
            self.ship.moving_up = True
        elif event.key == pygame.K_DOWN:
            self.ship.moving_down = True

    def _check_keyup_events(self, event):
        """реагирует на отпускание клавиш"""
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = False  # ВЫКЛЮЧАЕТ движение

        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = False

        elif event.key == pygame.K_UP:
            self.ship.moving_up = False

        elif event.key == pygame.K_DOWN:
            self.ship.moving_down = False








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