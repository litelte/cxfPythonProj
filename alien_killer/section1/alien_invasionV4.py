# 拆分原来的run_game方法
import sys

import pygame
from settings import Settings
from ship import Ship


class AlienInvasion:
    def __init__(self) -> None:
        # 管理游戏行为的类
        pygame.init()
        # 导入游戏相关的设置
        self.settings = Settings()
        # 设置游戏基本参数
        self.screen = pygame.display.set_mode(
            (self.settings.screen_width, self.settings.screen_height)
        )
        # 框体标题
        pygame.display.set_caption("杀死那个外星人")
        # 加载游戏预设飞船图标，创建一个Ship实例，实例必须提供一个参数
        # 这个参数就是类名AlienInvasion
        # 这个参数让Ship能够访问游戏资源，如对象screen
        # 将这个Ship实例赋给了self.ship
        self.ship = Ship(self)

    def run_game(self):
        """开始游戏主循环"""
        while True:
            self._check_events()
            # 每次循环时重绘屏幕
            self.screen.fill(self.settings.bg_color)
            self.ship.blitme()

            # 让最近的屏幕可见
            pygame.display.flip()

    def _check_events(self):
        """响应按键和鼠标事件"""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()


if __name__ == "__main__":
    ai = AlienInvasion()
    ai.run_game()
