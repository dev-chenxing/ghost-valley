import sys
import threading
import time
from rich import print as rprint


from command import process_input
import game
from core.prompt import select
from content.title import title
from utils import get_saves, save_file_exists


def load_game():
    save = select(text="读取进度", choices=get_saves())
    game.load_game(file=save)


def continue_game():
    save = get_saves()[0]["value"]
    game.load_game(file=save)


def main_menu():
    rprint(title, end="")
    main_menu_options = {
        "continue": {
            "name": "再续前缘",
            "callback": continue_game,
            "condition": save_file_exists
        },
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


def rumor():
    msg = "something"
    while True:
        with threading.Lock():
            print("\x1b[s\x1b[1A\x1b[999D\x1b[1S\x1b[L" +
                  msg+"\x1b[u", end="", flush=True)
            time.sleep(2)


def user_input():
    try:
        while True:
            cmd = input("> ")
            process_input(cmd)
    except EOFError as e:
        rprint(":x: 退出")
        sys.exit(1)


try:
    main_menu()

    rumor_thread = threading.Thread(target=rumor, daemon=True)
    input_thread = threading.Thread(target=user_input, daemon=True)

    # rumor_thread.start()
    input_thread.start()

    while True:
        pass

except (KeyboardInterrupt, SystemExit):
    rprint(":x: 退出")
    sys.exit(1)
