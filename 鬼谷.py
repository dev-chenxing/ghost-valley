import sys
import pygame
from crop import Crop
from item_stack import ItemStack
from lib.zhongwen.number import 中文數字
from object import Object
from palette import palette
from reference import Reference
from seeds import Seeds
from ui import UI
from player import Player


class 鬼谷:
    def __init__(self):
        self.ui = UI()
        self.menu = self.ui.create_menu()
        self.objects = []

        self.player = Player(id="player", name="新鬼")
        self.field = []

        white_radish = self.create_object(
            id="white_radish", name="白萝卜", objectType="crop")
        white_radish_seed = self.create_object(id="white_radish_seed",
                                               name="白萝卜种子", objectType="seeds")
        white_radish_seed.crop = "white_radish"
        self.add_item(item="white_radish_seed", count=15)

    def create_object(self, id, objectType, name):
        if objectType == "seeds":
            object = Seeds(id=id, name=name)
        elif objectType == "crop":
            object = Crop(id=id, name=name)
        else:
            object = Object(id=id, name=name, objectType=objectType)
        self.objects.append(object)
        return object

    def getObject(self, id):
        try:
            return next(obj for obj in self.objects if obj.id is id)
        except:
            return None

    def add_item(self, item: str, count=1) -> int:
        obj = self.getObject(item)
        if not obj:
            return 0
        item_stack = ItemStack(obj=obj, count=count)
        if not item_stack:
            return 0
        self.player.inventory.append(item_stack)
        return count

    def remove_item(self, item: Object, count=1):
        item_stack: ItemStack = next(
            i for i in self.player.inventory if i.object is item)
        item_stack.count -= count
        print("removed", count)
        print(item_stack.count)
        if item_stack.count == 0:
            self.player.inventory.remove(item_stack)

    def create_reference(self, object):
        if type(object) is str:
            return Reference(object=self.getObject(object))
        else:
            return Reference(object=object)

    def plant(self, seed):
        print("plant")
        self.remove_item(item=seed, count=1)
        ref = self.create_reference(object=seed.crop)
        self.field.append(ref)

    def helloworld(self):
        print("hello world")

    def run(self):
        clock = pygame.time.Clock()
        while True:
            print("run")
            self.menu.add.label(title=f"铜钱{中文數字(self.player.coins)}文")

            for item_stack in self.player.inventory:
                if (item_stack.count > 0):
                    button = self.menu.add.button(f"{item_stack.object.name}{中文數字(
                        item_stack.count)}颗", selection_color=palette["烟墨"])

                    def _update_button() -> None:
                        print("button updating")
                        self.plant(item_stack.object)
                        print(item_stack.count)
                        button.set_title(f"{item_stack.object.name}{中文數字(
                            item_stack.count)}颗")
                    button.update_callback(_update_button)
            self.menu.mainloop(self.ui.screen)
            pygame.display.update()
            clock.tick(60)  # limits FPS to 60


def main():
    鬼谷().run()


if __name__ == '__main__':
    main()
