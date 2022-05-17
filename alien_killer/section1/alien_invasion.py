import sys

import pygame


class AlienInvasion:
    """
    管理游戏资源和行为的类
    """

    def __init__(self):
        #  初始化游戏并创建游戏资源
        pygame.init()
        # 这里算是把类属性
        self.screen = pygame.display.set_mode((1200, 600))

    def run_game(self):
        """开始游戏主循环"""
        while True:
            # 监视键盘和鼠标事件
            for event in pygame.event.get():
                # pygame的窗体是退出的状态，就马上结束进程
                if event.type == pygame.QUIT:
                    sys.exit()

            # 让最近绘制的屏幕可见
            pygame.display.flip()


if __name__ == "__main__":
    # 创建游戏实例并运行游戏
    ai = AlienInvasion()
    ai.run_game()
