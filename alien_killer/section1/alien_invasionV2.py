import sys

import pygame
from settings import Settings


class AlienInvasion:
    # 管理游戏资源和行为的类
    def __init__(self) -> None:

        pygame.init()
        # 把函数做属性
        self.settings = Settings()
        self.screen = pygame.display.set_mode(
            (self.settings.screen_width, self.settings.screen_height)
        )
        # 有了设置文件里的配置，这里就不需要再定义了
        # self.bg_color = self.settings.bg_color
        pygame.display.set_caption("Alien Invasion")

    def run_game(self):
        # 开始游戏主循环
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

            # 每次循环时都重绘屏幕
            self.screen.fill(self.settings.bg_color)
            # 让最近绘制的屏幕可见
            pygame.display.flip()


if __name__ == "__main__":
    ai = AlienInvasion()
    ai.run_game()
