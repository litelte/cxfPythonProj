class Settings:
    """存储游戏《外星人入侵》中所有设置的类"""

    def __init__(self) -> None:
        # 初始化游戏的设置
        self.screen_width = 1200
        self.screen_height = 600
        self.bg_color = (230, 230, 230)
        self.bg_color_blue = (0, 128, 255)
        # 调整飞船速度
        self.ship_speed = 1.5

        # 更新Bullet所需的值：
        # 子弹设置
        self.bullet_speed = 1.5
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (60, 60, 60)
        # 限制子弹的数量
        self.bullets_allowed = 20
        # 外星人设置
        self.alien_speed = 1.0
        self.fleet_drop_speed = 10
        # fleet_direction为1表示向右移动，为-1表示向左移动
        self.fleet_direction = 1
        # 飞船设置
        self.ship_speed = 1.5
        self.ship_limit = 3
