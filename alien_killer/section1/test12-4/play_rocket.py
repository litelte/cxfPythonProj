# 主文件，运行程序
import sys

import pygame
from rocket import Rocket
from settings import Settings


class PlayRocket:
    def __init__(self) -> None:
        # 初始化界面
        pygame.init()
        self.settings = Settings()
        self.screen = pygame.display.set_mode(
            (self.settings.screen_width, self.settings.screen_height)
        )
        # 标题文字
        pygame.display.set_caption("玩火箭，上下左右都可以版")
        # 加载火箭
        self.rocket = Rocket(self)

    def run_game(self):
        while True:
            self._check_events()
            self.rocket.update()
            self._update_screen()

    def _check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._check_event_keydown(event)
            elif event.type == pygame.KEYUP:
                self._check_event_keyup(event)

    def _check_event_keydown(self, event):
        # 按下按键
        if event.key == pygame.K_RIGHT:
            self.rocket.moving_right = True
        elif event.key == pygame.K_LEFT:
            self.rocket.moving_left = True
        elif event.key == pygame.K_UP:
            self.rocket.moving_up = True
        elif event.key == pygame.K_DOWN:
            self.rocket.moving_down = True
        # 按q退出程序
        elif event.key == pygame.K_q:
            sys.exit()

    def _check_event_keyup(self, event):
        if event.key == pygame.K_RIGHT:
            self.rocket.moving_right = False
        elif event.key == pygame.K_LEFT:
            self.rocket.moving_left = False
        elif event.key == pygame.K_UP:
            self.rocket.moving_up = False
        elif event.key == pygame.K_DOWN:
            self.rocket.moving_down = False

    def _update_screen(self):
        self.screen.fill(self.settings.bg_color)
        self.rocket.blitme()
        # 让界面常驻
        pygame.display.flip()


if __name__ == "__main__":
    pr = PlayRocket()
    pr.run_game()
