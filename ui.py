import pygame

from game import Game
from palette import palette
from lib.zhongwen.number import 中文數字
from ui_element import UIElement


class UI:
    def __init__(self, game: Game):
        self.viewport_width = 1280
        self.viewport_height = 720
        self.screen = pygame.display.set_mode(
            (self.viewport_width, self.viewport_height))
        self.screen.fill(palette["山矾"])
        self.font = pygame.font.Font("fonts/AlimamaDaoLiTi.ttf", 36)
        self.display_surface = pygame.display.get_surface()
        self.game = game

    def create_label(self, text, color, x, y):
        label = UIElement(element_type="text", text=text,
                          font=self.font, color=color, x=x, y=y, game=self.game)
        label.render()
        return label

    def create_text_select(self, text, color, x, y):
        text_select = UIElement(element_type="text", text=text,
                                font=self.font, color=color, x=x, y=y, game=self.game)
        text_select.render()
        return text_select

    def update(self, deltaTime: float):
        self.create_label(text=f"铜钱{中文數字(self.game.player.coins)}文", color=palette["烟墨"],
                          x=self.viewport_width/2, y=128)

        for item_stack in self.game.player.inventory:
            if (item_stack.count > 0):
                text_select = self.create_text_select(text=f"{item_stack.object.name}{中文數字(
                    item_stack.count)}颗", color=palette["烟墨"],
                    x=self.viewport_width/2, y=256)
                text_select.register(event="mouse_click",
                                     callback=lambda button: self.game.plant(item_stack.object))

        for plant_ref in self.game.field:
            self.create_text_select(text=plant_ref.object.name, color=palette["烟墨"],
                                    x=self.viewport_width/2, y=384)

            # game.harvest(plant_ref)
