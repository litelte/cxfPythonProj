import sys

import pygame
from bullet import Bullet
from rocket import Rocket
from settings import Settings


class PlayRocket:
    def __init__(self) -> None:
        self.settings = Settings()
        self.screen = pygame.display.set_mode(
            (self.settings.screen_width, self.settings.screen_height)
        )
        pygame.display.set_caption("玩火箭，只能上下移动")
        self.rocket = Rocket(self)
        # 子弹存储在编组中
        self.bullets = pygame.sprite.Group()

    def run_game(self):
        while True:
            self._check_events()
            self.rocket.update()
            self._update_bullets()
            # 默认进图就自动设计
            # self._fire_bullet()
            self._update_screen()

    def _update_bullets(self):
        # 更新子弹的位置并删除消失的子弹
        # 更新子弹的位置
        self.bullets.update()
        # 将消失的子弹删除
        for bullet in self.bullets.copy():
            # if bullet.rect.bottom <= self.screen_rect.bottom:
            if bullet.rect.right > self.settings.screen_width:
                self.bullets.remove(bullet)
        print(len(self.bullets))

    def _check_events(self):
        # 响应鼠标和按键事件
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)

    def _check_keydown_events(self, event):
        # 响应按键
        # if event.key == pygame.K_RIGHT:
        #     self.rocket.moving_right = True
        # elif event.key == pygame.K_LEFT:
        #     self.rocket.moving_left = True
        if event.key == pygame.K_UP:
            self.rocket.moving_up = True
        elif event.key == pygame.K_DOWN:
            self.rocket.moving_down = True
        elif event.key == pygame.K_SPACE:
            self._fire_bullet()
        # 按q键退出
        elif event.key == pygame.K_q:
            sys.exit()

    def _check_keyup_events(self, event):
        # 按键松开
        if event.key == pygame.K_RIGHT:
            self.rocket.moving_right = False
        elif event.key == pygame.K_LEFT:
            self.rocket.moving_left = False
        elif event.key == pygame.K_UP:
            self.rocket.moving_up = False
        elif event.key == pygame.K_DOWN:
            self.rocket.moving_down = False

    # 开火
    def _fire_bullet(self):
        # 创建一颗子弹，并将其加入编组bullets中
        if len(self.bullets) < self.settings.bullets_allowed:
            new_bullet = Bullet(self)
            self.bullets.add(new_bullet)
            # 如果屏幕的子弹等于3颗，那么用户按空格，啥都不发生

    def _update_screen(self):
        self.screen.fill(self.settings.bg_color_blue)
        self.rocket.blitme()
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()
        pygame.display.flip()


if __name__ == "__main__":
    ai = PlayRocket()
    ai.run_game()
