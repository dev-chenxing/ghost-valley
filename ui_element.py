from typing import Callable

import pygame

from game import Game

ui_events = ["mouse_click"]


class UIElement:
    def __init__(self, element_type, text, font, color, x, y, game: Game):
        self.game = game
        self.display_surface = pygame.display.get_surface()
        if element_type == "text":
            self.surface = font.render(
                text, False, color)
            self.rect = self.surface.get_rect(
                center=(x, y))

    def render(self):
        self.display_surface.blit(self.surface, self.rect)

    def register(self, event: str, callback: Callable):
        if (event in ui_events):
            def mouse_over_callback(button):
                if self.rect.collidepoint(pygame.mouse.get_pos()):
                    callback(button)
            if 0 not in self.game.eventCallbacks[event]:
                print("register")
                self.game.eventCallbacks[event][0] = mouse_over_callback
