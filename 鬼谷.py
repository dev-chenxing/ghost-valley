import sys
import pygame
from game import Game
from ui import UI


class 鬼谷:
    def __init__(self):
        pygame.init()

        pygame.display.set_caption('鬼谷三家村')
        self.clock = pygame.time.Clock()
        self.running = True

        self.game = Game()
        self.ui = UI(game=self.game)

    def run(self):
        while True:
            self.deltaTime = self.clock.tick(60) / 1000
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    button = pygame.mouse.get_pressed().index(True)
                    for callback in self.game.eventCallbacks["mouse_click"].values():
                        print("callback")
                        callback(button=button)
            self.ui.update(self.deltaTime)

            pygame.display.update()


def main():
    鬼谷().run()


if __name__ == '__main__':
    main()
