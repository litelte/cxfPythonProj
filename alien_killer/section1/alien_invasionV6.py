import sys

import pygame
from settings import Settings
from ship import Ship


class AlienInvasion:
    def __init__(self) -> None:
        pygame.init()
        self.settings = Settings()
        self.screen = pygame.display.set_mode(
            (self.settings.screen_width, self.settings.screen_height)
        )
        self.ship = Ship(self)
        # 标题
        pygame.display.set_caption("杀死那个外星人")

    def run_game(self):
        while True:
            self._check_event()
            self._update_screen()

    def _check_event(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

    def _update_screen(self):
        # 重绘屏幕
        self.screen.fill(self.settings.bg_color_blue)
        # 加载飞船在任意位置
        pygame.display.flip()
        self.ship.blitme()
        # 让桌面端常显示


if __name__ == "__main__":
    ai = AlienInvasion()
    ai.run_game()
