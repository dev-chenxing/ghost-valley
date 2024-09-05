import pygame

from game import Game
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

    def create_label(self, text, color, x, y):
        text_surface = self.font.render(
            text, False, color)
        text_rect = text_surface.get_rect(
            center=(x, y))
        self.surface.blit(text_surface, text_rect)

    def update(self, deltaTime: float, game: Game):
        self.create_label(text=f"铜钱{中文數字(game.player.coins)}文", color=palette["烟墨"],
                          x=self.viewport_width/2, y=128)

        for item_stack in game.player.inventory:
            if (item_stack.count > 0):
                self.create_label(text=f"{item_stack.object.name}{中文數字(
                    item_stack.count)}颗", color=palette["烟墨"],
                    x=self.viewport_width/2, y=256)
                # game.plant(item_stack.object)

        for plant_ref in game.field:
            self.create_label(text=plant_ref.object.name, color=palette["烟墨"],
                              x=self.viewport_width/2, y=384)

            # game.harvest(plant_ref)
