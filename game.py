from rich import print
import json
from typing import Union
from content import intro
from core import timer
from core.item_stack import ItemStack
from core.object import Crop, Object, Resource, Seed
from core.player import Player
from core.prompt import prompt, select
from core.quest import Quest
from core.reference import Reference
from core.room import Room

objects: list[Object] = []
player: Player = None
rooms: list[Room] = []
farm: Room
quests: list[Quest] = []


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
    return room


def get_room(id: str):
    try:
        return next(room for room in rooms if room.id is id)
    except:
        return None


def character_creation():
    print("[bold]主角设定[/bold]")
    genders = [{"name": "男", "value": False}, {"name": "女", "value": True}]
    player.female = select(message="性别", choices=genders)
    player.surname = prompt("姓", same_line=True, bold=True)
    player.given_name = prompt("名", same_line=True, bold=True)
    player.name = f"{player.surname}{player.given_name}"
    # player.favourite_thing = prompt("请输入你最喜欢的东西", same_line=True, bold=True)
    # pet = select(message="喜好的动物", choices=[
    #              {"name": "🐈 猫", "value": "cat"}, {"name": "🐕 狗", "value": "dog"}])
    return select(message="是否跳过开场剧情", suffix="？", choices=[
        {"name": "是", "value": True}, {"name": "否", "value": False}])


def new_game():
    global farm, player
    farm = create_room(id="farm")
    player = Player()
    # skip_intro = character_creation()
    # if not skip_intro:
    if True:
        intro.cutscene()


def get_quest(id: str):
    try:
        return next(quest for quest in quests if quest.id == id)
    except:
        return None


def update_quest(id: str, stage: int):
    quest = get_quest(id)
    print(f"[yellow1]！接取任务【{quest.id}】[/yellow1]：{quest.stages[stage]}")


def create_quest(id: str, stages: dict[int, str]):
    global quests
    quests.append(Quest(id=id, stages=stages))


def position_room(room: Union[Room, str, list[int]]):
    if isinstance(room, Room):
        player.room = room
    elif isinstance(room, str):
        player.room = get_room(id=room)
    print(f"[bold]{player.room.id}[/bold]")
