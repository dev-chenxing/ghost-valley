import pygame

from palette import palette
from lib.zhongwen.number import 中文數字


class UI:
    def __init__(self):
        self.viewport_width = 1280
        self.viewport_height = 720
        self.screen = pygame.display.set_mode(
            (self.viewport_width, self.viewport_height))
        self.font = pygame.font.Font("fonts/AlimamaDaoLiTi.ttf", 36)
        self.surface = pygame.display.get_surface()

    def create_menu(self):
        self.screen.fill(palette["山矾"])
        return self.surface

    def update(self, deltaTime):
        text_surface = self.font.render(
            f"铜钱{中文數字(self.player.coins)}文", False, palette["烟墨"])
        text_rect = text_surface.get_rect(
            center=(self.viewport_width/2, self.viewport_height/2))
        self.surface.blit(text_surface, text_rect)
