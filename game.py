import json
from typing import Union
from core import timer
from core.item_stack import ItemStack
from core.object import Crop, Object, Resource, Seed
from core.player import Player
from core.reference import Reference
from core.room import Room

objects: list[Object] = []
player: Player = None
rooms: list[Room] = []


def get_item_count(item: Object):
    generator = (i for i in player.inventory if i.object is item)
    try:
        item_stack: ItemStack = next(generator)
        return item_stack.count
    except StopIteration:
        return 0


def get_object(id: str = None, name: str = None):
    try:
        if id:
            return next(obj for obj in objects if obj.id == id)
        elif name:
            return next(obj for obj in objects if obj.name == name)
    except:
        return None


def remove_item(item: Object, count=1):
    item_stack: ItemStack = next(
        i for i in player.inventory if i.object == item)
    item_stack.count -= count
    if item_stack.count == 0:
        player.inventory.remove(item_stack)


def create_reference(object: Union[Object, str], room: Room):
    if type(object) is str:
        return Reference(object=get_object(object), room=room)
    else:
        return Reference(object=object, room=room)


def plant(seed: Seed, room: Room):
    remove_item(item=seed, count=1)
    ref = create_reference(object=seed.crop, room=room)
    room.plants.append(ref)


def harvest(plant: Reference):
    plant.delete()
    player.coins += 100


def create_object(objectType: str, id: str, **kwargs):
    object: Object = None
    if objectType == "seed":
        object = Seed(id=id, **kwargs)
    elif objectType == "crop":
        object = Crop(id=id, **kwargs)
    elif objectType == "resource":
        object = Resource(id=id, **kwargs)
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


def get_inventory_json(inventory: list[ItemStack]):
    return list(map(lambda item_stack: item_stack.to_json(), inventory))


def get_rooms_json():
    return list(map(lambda room: room.to_json(), rooms))


def save_game(file: str = "quicksave"):
    data = {
        "player": {"coins": player.coins,
                   "inventory": get_inventory_json(player.inventory)},
        "rooms": get_rooms_json(),
        "game_time": timer.game_time.time,
        "real_time": timer.real_time.time
    }
    with open(f'saves/{file}.json', "w") as save_file:
        json.dump(data, save_file)


def create_room(id: str):
    room = Room(id=id)
    rooms.append(room)


def get_room(id: str):
    try:
        return next(room for room in rooms if room.id is id)
    except:
        return None
