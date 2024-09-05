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

        self.ui = UI()

        self.game = Game()

    def run(self):

        while True:
            self.deltaTime = self.clock.tick() / 1000
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
            self.ui.update(self.deltaTime, self.game)

            pygame.display.update()


def main():
    鬼谷().run()


if __name__ == '__main__':
    main()
