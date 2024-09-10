from typing import Union
import game
from lib.zhongwen.number import 中文数字


objects = []


class Object():
    def __init__(self, id: str, name: str = ""):
        self.id = id
        self.name = name


class Seeds(Object):
    def __init__(self, id: str, name: str = "", value=0, crop: str = None):
        Object.__init__(self, id, name)
        self.objectType = "seeds"
        self.value = value
        self.crop = crop
        self.unit = "袋"


class Crop(Object):
    def __init__(self, id):
        Object.__init__(self, id)
        self.objectType = "crop"
        self.value = 0
        self.unit = "个"


class ItemStack():
    def __init__(self, object: Object, count=1):
        self.object = object
        self.count = count

    def to_string(self):
        return f"{中文数字(self.count)}{self.object.unit}{self.object.name}"


class Reference():
    def __init__(self, object: Object):
        self.object = object

    def delete(self):
        del self


def create_object(objectType: str, id: str):
    object: Object = None
    if objectType == "seeds":
        object = Seeds(id=id)
    elif objectType == "crop":
        object = Crop(id=id)
    if object:
        objects.append(object)
        return object


white_radish = create_object(objectType="crop", id="white_radish")
white_radish.name = "白萝卜"

white_radish_seeds = create_object(objectType="seeds", id="white_radish_seeds")
white_radish_seeds.name = "白萝卜种子"
white_radish_seeds.crop = "white_radish"

carrot = create_object(objectType="crop", id="carrot")
carrot.name = "胡萝卜"

carrot_seeds = create_object(objectType="seeds", id="carrot_seed")
carrot_seeds.name = "胡萝卜种子"
carrot_seeds.crop = "carrot"


class Player:
    def __init__(self, name="新鬼") -> None:
        self.name = name
        self.coins = 10
        self.inventory = [ItemStack(object=white_radish_seeds, count=1), ItemStack(
            object=carrot_seeds, count=1)]


item_colors = {
    "seeds": "dark_olive_green3",
    "crop": "dark_olive_green3"
}


def get_item_color(object: Object) -> str:
    return item_colors[object.objectType]


def getObject(id):
    try:
        return next(obj for obj in objects if obj.id is id)
    except:
        return None


def create_reference(object: Union[Object, str]):
    if type(object) is str:
        return Reference(object=getObject(object))
    else:
        return Reference(object=object)


def remove_item(item: Object, count=1):
    item_stack: ItemStack = next(
        i for i in game.player.inventory if i.object is item)
    item_stack.count -= count
    if item_stack.count == 0:
        game.player.inventory.remove(item_stack)


def plant(seeds: Seeds):
    remove_item(item=seeds, count=1)
    ref = create_reference(object=seeds.crop)
    game.field.append(ref)


def get_object(id):
    try:
        return next(obj for obj in objects if obj.id is id)
    except:
        return None
