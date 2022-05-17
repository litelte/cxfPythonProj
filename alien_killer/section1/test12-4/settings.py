class Settings:
    # 存储玩火箭所有的设置
    def __init__(self) -> None:
        self.screen_width = 1200
        self.screen_height = 600
        # 设置背景为蓝色
        self.bg_color = (0, 128, 255)
        # 设置速度
        self.rocket_speed = 1.5
