from typing import Union
from core.item_stack import ItemStack
from core.object import Crop, Object, Seeds
from core.player import Player
from core.reference import Reference

objects: list[Object] = []
player: Player = None
field: list[Reference] = []


def get_item_count(item: Object):
    generator = (i for i in player.inventory if i.object is item)
    try:
        item_stack: ItemStack = next(generator)
        return item_stack.count
    except StopIteration:
        return 0


def get_object(id):
    try:
        return next(obj for obj in objects if obj.id is id)
    except:
        return None


def remove_item(item: Object, count=1):
    item_stack: ItemStack = next(
        i for i in player.inventory if i.object is item)
    item_stack.count -= count
    if item_stack.count == 0:
        player.inventory.remove(item_stack)


def create_reference(object: Union[Object, str]):
    if type(object) is str:
        return Reference(object=get_object(object))
    else:
        return Reference(object=object)


def plant(seeds: Seeds):
    remove_item(item=seeds, count=1)
    ref = create_reference(object=seeds.crop)
    field.append(ref)


def create_object(objectType: str, id: str):
    object: Object = None
    if objectType == "seeds":
        object = Seeds(id=id)
    elif objectType == "crop":
        object = Crop(id=id)
    if object:
        objects.append(object)
        return object


def add_item(item: Union[Object, str], count: int = 1):
    if isinstance(item, Object):
        object = item
    else:
        object = get_object(id=item)
    if object:
        player.inventory.append(ItemStack(object=object, count=count))
