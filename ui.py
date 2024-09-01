import pygame
import pygame_menu

from palette import palette


class UI:
    def __init__(self):
        """ initialize graphics """
        pygame.init()
        self.viewport_width = 1280
        self.viewport_height = 720
        self.screen = pygame.display.set_mode(
            (self.viewport_width, self.viewport_height))
        self.font = pygame.font.Font("fonts/AlimamaDaoLiTi.ttf", 36)

    def create_menu(self):
        theme = pygame_menu.Theme(
            background_color=palette["山矾"],
            title_font=self.font,
            title_font_color=palette["烟墨"],
            title_background_color=palette["玛瑙"],
            widget_font=self.font,
        )
        self.menu = pygame_menu.Menu(title="鬼谷三家村", width=self.viewport_width, height=self.viewport_height,
                                     theme=theme)
        return self.menu
