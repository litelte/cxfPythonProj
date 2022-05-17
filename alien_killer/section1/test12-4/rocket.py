import pygame


class Rocket:
    def __init__(self, pr_game) -> None:
        # 初始化火箭
        self.screen = pr_game.screen
        self.settings = pr_game.settings
        # 给背景建立坐标
        # self.screen_rect = pr_game.screen.get_rect()
        self.screen_rect = self.screen.get_rect()

        # 加载飞船图像并获取其外接矩形
        self.image = pygame.image.load("section1/test1/rocketimg.bmp")
        # 给图片添加到背景坐标系上
        self.rect = self.image.get_rect()

        # 对于每一个火箭，都将其放在屏幕底部的中央
        self.rect.midbottom = self.screen_rect.midbottom

        # 在火箭的属性x中存储小数值
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)
        self.moving_right = False
        self.moving_left = False
        # 下来是y值
        self.moving_up = False
        self.moving_down = False

    def update(self):
        """根据移动标志调整飞船的位置"""

        # right就是矩形右边的x坐标距离背景左边框的距离
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += self.settings.rocket_speed
        # left就是矩形左边x的坐标距离背景左边框的距离
        elif self.moving_left and self.rect.left > 0:
            self.x -= self.settings.rocket_speed
        # 同理，top就是矩形上边的y距离背景上边框的距离
        elif self.moving_up and self.rect.top > 0:
            self.y -= self.settings.rocket_speed
        # bottom就是矩形下边的y距离背景上边框的距离
        elif self.moving_down and self.rect.bottom < self.screen_rect.bottom:
            self.y += self.settings.rocket_speed

        # 根据self.x更新rect对象
        self.rect.x = self.x
        self.rect.y = self.y

    def blitme(self):
        # 在指定位置绘制飞船
        self.screen.blit(self.image, self.rect)
