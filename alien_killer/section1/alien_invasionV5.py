import sys

import pygame
from settings import Settings
from ship import Ship


# 再一次重构，把重绘画面函数也给整理了
class AlienInvasion:
    def __init__(self) -> None:
        pygame.init()
        self.settings = Settings()
        self.screen = pygame.display.set_mode(
            (self.settings.screen_width, self.settings.screen_height)
        )
        # 忘了标题了
        pygame.display.set_caption("杀死那个外星人")
        # 绘制飞船
        self.ship = Ship(self)

    def run_game(self):
        # 开启游戏主循环
        while True:
            # 监听鼠标键盘事件
            self._check_events()
            # 更新屏幕内容
            self._update_screen()

    def _check_events(self):
        # 相应案件和鼠标事件
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

    def _update_screen(self):
        """更新屏幕上的图像，并切换到新屏幕"""
        self.screen.fill(self.settings.bg_color)
        # 在指定位置绘制飞船
        self.ship.blitme()

        # 让画面停留
        pygame.display.flip()


if __name__ == "__main__":
    ai = AlienInvasion()
    ai.run_game()
