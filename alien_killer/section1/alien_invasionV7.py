import sys

import pygame
from settings import Settings
from ship import Ship


# 更新了响应按键的属性
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
        # 响应按键和鼠标事件
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    # 向右移动飞船
                    self.ship.rect.x += 1

    def _update_screen(self):
        self.screen.fill(self.settings.bg_color_blue)
        # 加载飞船在任意位置
        self.ship.blitme()
        # 最后让这个屏幕可见
        pygame.display.flip()


if __name__ == "__main__":
    ai = AlienInvasion()
    ai.run_game()
