import threading
import time
from rich import print
import json
from typing import Union
from pathlib import Path
import os
import importlib
from content import intro
from core import timer
from core.item_stack import ItemStack
from core.npc import NPC
from core.object import Crop, Object, Resource, Seed
from core.player import Player
from core.prompt import prompt, select, spinner
from core.quest import Quest
from core.reference import Reference
from core.room import Room
from utils import i18n

objects: list[Object] = []
player: Player = Player()
rooms: list[Room] = []
quests: list[Quest] = []
idle_talk: list[dict] = []


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
    if objectType == "npc":
        object = NPC(id=id, **kwargs)
    elif objectType == "seed":
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


def get_quests_json():
    return list(map(lambda quest: quest.to_json(), quests))


def save_game(file: str):
    data = {
        "player": {"surname": player.surname, "given_name": player.given_name, "name": player.name, "room": player.room.id},
        "quests": get_quests_json(),
        "game_time": timer.game_time.time,
        "timestamp": int(time.time())
    }
    with open(f'saves/{file}-{timer.game_time.time}.json', "w", encoding='utf8') as save_file:
        json.dump(data, save_file, ensure_ascii=False)
    print(i18n("saved"))


def print_quests():
    for quest in quests:
        if not quest.finished:
            print(f"[bold]{quest.id}[/bold]：{quest.stages[quest.stage]}")


def load_game(file: str):
    load()
    with open(f'saves/{file}.json', encoding='utf8') as save_file:
        data = json.load(save_file)
    player.surname = data["player"]["surname"]
    player.given_name = data["player"]["given_name"]
    player.name = data["player"]["name"]
    for quest_data in data["quests"]:
        quest = get_quest(quest_data["id"])
        quest.stage = quest_data["stage"]
        quest.finished = quest_data["finished"]
    timer.game_time = timer.Time(init_time=data["game_time"])
    timer.real_time = timer.Time()
    game_time_thread = threading.Thread(
        target=timer.game_time_thread, daemon=True)
    real_time_thread = threading.Thread(
        target=timer.real_time_thread, daemon=True)
    game_time_thread.start()
    real_time_thread.start()
    position_room(get_room(data["player"]["room"]))


def create_room(id: str, **kwargs):
    room = Room(id=id, **kwargs)
    rooms.append(room)
    return room


def get_room(id: str = None, x: int = None, y: int = None):
    try:
        if id or (x != None) and (y != None):
            for room in rooms:
                if (id and id == room.id):
                    return room
                elif (x == room.grid_x and y == room.grid_y):
                    return room
    except:
        return None


def character_creation():
    print(f"[bold]{i18n("character_creation")}[/bold]")
    genders = [{"name": i18n("character_creation_male"), "value": False}, {
        "name": i18n("character_creation_female"), "value": True}]
    player.female = select(
        text=i18n("character_creation_gender"), choices=genders)
    player.surname = prompt(
        i18n("character_creation_last_name"), same_line=True, bold=True)
    player.given_name = prompt(
        i18n("character_creation_first_name"), same_line=True, bold=True)
    player.name = i18n("_get_character_name", surname=player.surname,
                       given_name=player.given_name)


def load():
    for dir_entry in os.scandir("content/npcs"):
        if dir_entry.is_file():
            path = Path(dir_entry.name)
            if path.suffix == ".py":
                stem = path.stem
                npc = importlib.import_module(f"content.npcs.{stem}")
                create_object(
                    objectType="npc",
                    id=npc.id,
                    name=npc.name,
                    color=npc.color,
                    female=npc.female
                )
    for dir_entry in os.scandir("content/rooms"):
        if dir_entry.is_file():
            path = Path(dir_entry.name)
            if path.suffix == ".py":
                stem = path.stem
                room = importlib.import_module(f"content.rooms.{stem}")
                create_room(
                    id=room.id,
                    grid_x=room.grid_x,
                    grid_y=room.grid_y,
                    callback=room.callback,
                    can_change_room=room.can_change_room if hasattr(
                        room, "can_change_room") else lambda room_from=None, room_to=None: True
                )
    for dir_entry in os.scandir("content/quests"):
        if dir_entry.is_file():
            path = Path(dir_entry.name)
            if path.suffix == ".py":
                stem = path.stem
                quest = importlib.import_module(f"content.quests.{stem}")
                create_quest(
                    id=quest.id,
                    description=quest.description,
                    stages=quest.stages
                )


def new_game():
    load()
    timer.game_time = timer.Time()
    timer.real_time = timer.Time()
    game_time_thread = threading.Thread(
        target=timer.game_time_thread, daemon=True)
    real_time_thread = threading.Thread(
        target=timer.real_time_thread, daemon=True)
    game_time_thread.start()
    real_time_thread.start()
    character_creation()
    intro.cutscene()


def get_quest(id: str):
    global quests
    try:
        for quest in quests:
            if quest.id == id:
                return quest
    except:
        return None


def get_quest_stage(id: str):
    quest = get_quest(id=id)
    return quest.stage if quest else 0


def update_quest(id: str, stage: int = None, finished: bool = False):
    quest = get_quest(id)
    if finished:
        print(f"[yellow1]！【{quest.id}】{i18n("quest_finished")}[/yellow1]")
        quest.finished = True
    else:
        print(f"[yellow1]！{i18n("quest_received")}【{
              i18n(quest.id)}】[/yellow1]：{quest.stages[stage]}")
        quest.stage = stage


def create_quest(id: str, stages: dict[int, str], description: str = None):
    global quests
    quests.append(Quest(id=id, stages=stages, description=description))


def position_room(room: Union[Room, str, list[int]]):
    if isinstance(room, Room):
        player.room = room
    elif isinstance(room, str):
        player.room = get_room(id=room)
    elif isinstance(room, list):
        player.room = get_room(x=room[0], y=room[1])
    print("")
    spinner(text=f"{i18n("loading")}...", seconds=1)
    print(f"[bold]{i18n(player.room.name)}[/bold]")
    player.room.callback()
