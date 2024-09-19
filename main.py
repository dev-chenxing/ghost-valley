import os
from pathlib import Path
import threading
from rich import print
from InquirerPy.utils import color_print


from command import process_input
import game
from core.player import Player
from core import timer
from core.prompt import select
from content.title import title


def get_saves() -> list:
    saves = []
    saves_dir = "saves"
    if not os.path.isdir(saves_dir):
        os.makedirs(saves_dir)
    for dir_entry in os.scandir(saves_dir):
        if dir_entry.is_file():
            path = Path(dir_entry.name)
            if path.suffix == ".json":
                saves.append({"value": path.stem, "name": path.stem})
    return saves


def load_game():
    save = select(text="读取进度", choices=get_saves())
    game.load_game(file=save)


def save_file_exists():
    saves = get_saves()
    if saves == []:
        return False
    else:
        return True


def main_menu():
    print(title, end="")
    main_menu_options = {
        "new": {
            "name": "初入仙山",
            "callback": game.new_game
        },
        "load": {
            "name": "读取进度",
            "callback": load_game,
            "condition": save_file_exists
        },
        "exit": {
            "name": "退出游戏",
            "callback": exit
        }
    }
    choices = []
    for value, choice in main_menu_options.items():
        if ("condition" not in choice) or choice["condition"]():
            choices.append({"name": choice["name"], "value": value})
    action = select(choices=choices, default="new")
    if action:
        main_menu_options[action]["callback"]()


try:
    main_menu()

    # white_radish = game.create_object(
    #     objectType="crop", id="white_radish", name="白萝卜")
    # white_radish_seed = game.create_object(
    #     objectType="seed", id="white_radish_seed", name="白萝卜种子", crop="white_radish")
    # carrot = game.create_object(objectType="crop", id="carrot", name="胡萝卜")
    # carrot_seed = game.create_object(
    #     objectType="seed", id="carrot_seed", name="胡萝卜种子", crop="carrot")
    # twig = game.create_object(objectType="resource",
    #                           id="twig", name="树枝", unit="根")
    # game.add_item(item=white_radish_seed, count=15)
    # game.add_item(item=carrot_seed)

    while True:
        cmd = input("> ")
        process_input(cmd)

except (KeyboardInterrupt, SystemExit):
    print(":x: 退出")
