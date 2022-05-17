import sys

import pygame
from settings import Settings
from ship import Ship


class AlienInvasion:
    # 管理游戏资源和行为的类
    def __init__(self) -> None:
        pygame.init()
        # 先导入
        self.settings = Settings()
        self.screen = pygame.display.set_mode(
            (self.settings.screen_width, self.settings.screen_height)
        )
        pygame.display.set_caption("杀死那个外星人")
        # 啥意思？类做属性？
        self.ship = Ship(self)

    def run_game(self):
        # 开始游戏主循环
        while True:
            # 监听系统事件
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
            # 每次循环都重绘屏幕
            self.screen.fill(self.settings.bg_color)
            self.ship.blitme()

            # 让最近绘制的屏幕可见
            pygame.display.flip()


if __name__ == "__main__":
    ai = AlienInvasion()
    ai.run_game()
