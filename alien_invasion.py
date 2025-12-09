import pygame
import sys
from time import sleep
from ship import Ship
from bullet import Bullet
from alien import Alien
from settings import Settings
from game_stats import GameStats
from parms_const import *


class AlienInvasion():
    '''класс управления ресурсами игры'''
    def __init__(self):
        """Инициализирует игру, создает ресурсы"""
        pygame.init()
        self.settings = Settings()

        self.screen = pygame.display.set_mode((0,0), pygame.FULLSCREEN)  # запуск в полноэкранном режиме
        self.game_stats = GameStats(self)
        self.settings.screen_width = self.screen.get_rect().width
        self.settings.screen_height = self.screen.get_rect().height

        # self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption('Alien Invasion')
        self.ship = Ship(self)
        self.bg_image = pygame.image.load(self.settings.bg_image_path)
        self.bg_image = pygame.transform.scale(self.bg_image,(self.settings.screen_width,self.settings.screen_height))
        self.bullets = pygame.sprite.Group()
        self.aliens = pygame.sprite.Group()
        self._create_fleet()

    def run_game(self):
        """запуск основного цикла игры"""
        while True:
            # отслеживание событий клавиатуры и мышки
            self._check_events()  # Обновляет флаги
            self.ship.update()  # Двигает корабль по флагам
            self._update_bullets()
            self._update_aliens()
            # self.bullets.update()  # обновение позиции снаряда
            self._update_screen()  # Отрисовывает новую позицию

    def _update_bullets(self):
        """обновляет позиции снарядов и уничтожает старые снаряды"""
        self.bullets.update()
        # удаление снарядов, вышедших за края экрана
        for bullet in self.bullets.copy():
            if bullet.rect.bottom <= 0:  # если снаряд вышел за верхнюю границу, он удаляется из bullet (стр. 41)
                self.bullets.remove(bullet)
            # print(len(self.bullets))  # вывод в терминал количества снярядов
        collisions = pygame.sprite.groupcollide(self.aliens, self.bullets, True, True)
        if not self.aliens:
            self.bullets.empty()
            self._create_fleet()

    def _update_aliens(self):
        """Обновляет позиции всех пришельцев"""
        self._check_fleet_edges()
        self.aliens.update()
        # проверка колизий "пришелец - корабль"
        if pygame.sprite.spritecollideany(self.ship, self.aliens):
            self._ship_hit()
        self._check_fleet_bottom()  # проверка ушли за нижний экран
        self._check_aliens_bottom()

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
        elif event.key == pygame.K_UP:
            self.ship.moving_up = True
        elif event.key == pygame.K_DOWN:
            self.ship.moving_down = True
        elif event.key == pygame.K_ESCAPE:  # добавил кнопки выхода из игры
            sys.exit()
        elif event.key == pygame.K_SPACE:
            self._fire_bullet()

    def _check_keyup_events(self, event):
        """реагирует на отпускание клавиш"""
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = False  # выключает движение
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = False
        elif event.key == pygame.K_UP:
            self.ship.moving_up = False
        elif event.key == pygame.K_DOWN:
            self.ship.moving_down = False

    def _fire_bullet(self):
        """создание нового снаряда и включение его в группу bullets"""
        if len(self.bullets) < self.settings.bullets_allowed:  # ограничение количества снарядов
            new_bullet = Bullet(self)
            self.bullets.add(new_bullet)

    def _create_fleet(self):
        """создание флота вторжения"""
        # создание пришельца
        alien = Alien(self)  # 1. создание пришельца
        alien_width, alien_height = alien.rect.size  # содержит кортеж ширина/высота
        # 3. вычисляется доступное пространство по горизнтали и количество тех, кто поместится
        available_space_x = self.settings.screen_width - (2 * alien_width)
        number_aliens_x = available_space_x // (2 * alien_width)
        """определяет количество рядов на экране"""
        ship_height = self.ship.rect.height
        available_space_y = self.settings.screen_height - (3 * alien_height) - ship_height
        number_row = available_space_y // (2 * alien_height)
        # Создание первого ряда пришельцев:
        # 4. в цикле создается новый пришелец, задается его координата "х"
        # для размещения в ряду
        for row_number in range(number_row):
            for alien_number in range(number_aliens_x):
                # создание пришельца и размещение его в ряду
                self._create_alien(alien_number, row_number)

    # для рефакторинга добавляется вспомогательный метод _create_alien:
    def _create_alien(self, alien_number, row_number):
        """создание пришельца + размещение в ряду"""
        alien = Alien(self)
        alien_width, alien_height = alien.rect.size
        # Координата X зависит от alien_number (позиция в ряду) исправлено с ИИ
        alien.x = alien_width + 2 * alien_width * alien_number
        alien.rect.x = alien.x
        # Координата Y зависит от row_number (номер ряда)
        alien.rect.y = alien_height + 2 * alien_height * row_number  # Исправлено: используем row_number вместо alien_number. исправлено с ИИ
        self.aliens.add(alien)

    def  _check_fleet_edges(self):
        """Реагирует на достижение края экрана"""
        for alien in self.aliens.sprites():
            if alien.check_edges():
                self._change_fleet_direction()
                break

    def _change_fleet_direction(self):
        """опускает весь флот и меняет направление"""
        for alien in self.aliens.sprites():
            alien.rect.y += self.settings.fleet_drop_speed
        self.settings.fleet_direction *= -1

    def _check_fleet_bottom(self):
        """Проверяет, достигли ли пришельцы нижнего края экрана"""
        screen_rect = self.screen.get_rect()
        # all_aliens_gone = True
        for alien in self.aliens.sprites():
            if alien.rect.top >= screen_rect.bottom:  # было <
                self._reset_fleet_to_top()
                # all_aliens_gone = False
                break
        # if all_aliens_gone:  # Если все пришельцы ушли за нижний край
        #     self._reset_fleet_to_top()

    def _reset_fleet_to_top(self):
        """Перемещает весь флот пришельцев наверх с новой позицией"""
        self.aliens.empty()  # Удаляем старых пришельцев
        self._create_fleet()  # Создаем новый флот сверху
        self.settings.alien_speed *= INCREASING_SPEED  # Увеличиваем скорость на 20%

    def _ship_hit(self):
        """обработка столконовение корабля с пришельцем"""
        if self.game_stats.ship_left > 0:
            self.game_stats.ship_left -= 1  # уменьшение ships_left
            # очистка списка пришельцев и снарядов
            self.aliens.empty()
            self.bullets.empty()
            # создание нового флота и размещение в центре
            self._create_fleet()
            self.ship.center_ship()
            # пауза
            sleep(1)
        else:
            self.game_active = False

    def _check_aliens_bottom(self):
        """Проверяет, добрались ли пришельцы до нижнего края экрана."""
        screen_rect = self.screen.get_rect()
        for alien in self.aliens.sprites():
            if alien.rect.bottom >= screen_rect.bottom:
            # Происходит то же, что при столкновении с кораблем.
                self._ship_hit()
                break


    def _update_screen(self):
        """Отображает изображение на экране и новый экран"""
        self.screen.blit(self.bg_image, (0, 0))  # прорисовывается экран
        self.ship.blitme()
        for bullets in self.bullets.sprites():
            bullets.draw_bullet()
        self.aliens.draw(self.screen)
        # отображение последнего прорисованного экрана
        pygame.display.flip()

if __name__ == '__main__':
    # создание экземпляра и запуск игры
    ai = AlienInvasion()
    ai.run_game()
