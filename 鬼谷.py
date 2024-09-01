import sys
import pygame
from item_stack import ItemStack
from lib.zhongwen.number import 中文數字
from object import Object, objects, getObject
from palette import palette
from reference import Reference
from ui import UI
from player import Player


class 鬼谷:
    def __init__(self):
        self.ui = UI()
        self.menu = self.ui.create_menu()

        self.player = Player(objId="player", name="新鬼")
        self.field = []

        self.add_item(item="white_radish_seed", count=15)

        self.menu.add.label(title=f"铜钱{中文數字(self.player.coins)}文")

        for item_stack in self.player.inventory:
            if (item_stack.count > 0):
                print(item_stack)
                self.menu.add.button(title=f"{item_stack.object.name}{中文數字(
                    item_stack.count)}颗", action=self.plant, args=item_stack.object, selection_color=palette["烟墨"])

    def add_item(self, item: str, count=1) -> int:
        obj = getObject(item)
        if not obj:
            return 0
        item_stack = ItemStack(obj=obj, count=count)
        if not item_stack:
            return 0
        self.player.inventory.append(item_stack)
        return count

    def remove_item(self, item: Object, count=1):
        item_stack = next(i for i in self.player.inventory if i.object is item)
        item_stack.count -= 1
        if item_stack.count is 0:
            self.player.inventory.remove(item_stack)

    def plant(self, seed):
        self.remove_item(item=seed, count=1)
        self.field.append(Reference(obj=seed.crop))

    def run(self):
        clock = pygame.time.Clock()
        while True:
            clock.tick(60)  # limits FPS to 60
            self.menu.mainloop(self.ui.screen)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()


def main():
    鬼谷().run()


if __name__ == '__main__':
    main()
