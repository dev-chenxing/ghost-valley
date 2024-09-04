import sys
import pygame
from crop import Crop
from item_stack import ItemStack
from object import Object
from palette import palette
from reference import Reference
from seeds import Seeds
from ui import UI
from player import Player


class 鬼谷:
    def __init__(self):
        pygame.init()
        
        pygame.display.set_caption('鬼谷三家村')
        self.clock = pygame.time.Clock()
        self.running = True

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
        if item_stack.count == 0:
            self.player.inventory.remove(item_stack)

    def create_reference(self, object):
        if type(object) is str:
            return Reference(object=self.getObject(object))
        else:
            return Reference(object=object)

    def plant(self, seed):
        self.remove_item(item=seed, count=1)
        ref = self.create_reference(object=seed.crop)
        self.field.append(ref)

    def calculatePrice(item, count=1):
        return item.value * count

    def sell(self, ref):
        self.player.coins += self.calculatePrice(ref.object, count=1)

    def harvest(self, ref: Reference):
        self.field.remove(ref)
        self.sell(ref)
        ref.delete()

    def run(self):

        while True:
            self.deltaTime = self.clock.tick() / 1000
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
            self.ui.update(self.deltaTime)

            pygame.display.update()

            # for item_stack in self.player.inventory:
            #     button = self.menu.add.button(f"{item_stack.object.name}{中文數字(
            #         item_stack.count)}颗", selection_color=palette["烟墨"])

            #     def _update_button() -> None:
            #         self.plant(item_stack.object)
            #         if (item_stack.count > 0):
            #             button.set_title(f"{item_stack.object.name}{
            #                              中文數字(item_stack.count)}颗")
            #         else:
            #             self.menu.remove_widget(button)
            #     button.update_callback(_update_button)

            # for plant_ref in self.field:
            #     button = self.menu.add.button(
            #         plant_ref.object.name, selection_color=palette["烟墨"])

            #     def _update_button():
            #         self.harvest(plant_ref)
            #         self.menu.remove_widget(button)
            #     button.update_callback(_update_button)


def main():
    鬼谷().run()


if __name__ == '__main__':
    main()
