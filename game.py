from crop import Crop
from item_stack import ItemStack
from object import Object
from player import Player
from reference import Reference
from seeds import Seeds


class Game:
    def __init__(self) -> None:
        self.objects = []
        self.eventCallbacks = {
            "mouse_click": []
        }
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
        print("remove_item", item.id, count)
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
        print("plant", seed.name)
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
