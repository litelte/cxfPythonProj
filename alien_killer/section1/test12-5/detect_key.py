import sys

import pygame


# 检测按键的输入
class DetectKey:
    def __init__(self) -> None:
        pygame.init()
        self.screen = pygame.display.set_mode((1200, 600))

    def run_screen(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                elif event.type == pygame.KEYDOWN:
                    print(event.key)
                # if event.key == pygame.K_q:
                #     sys.exit()
            pygame.display.flip()


if __name__ == "__main__":
    ai = DetectKey()
    ai.run_screen()
