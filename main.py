from rich.text import Text
from rich import print as rprint
import sys
import threading
import time

from command import process_input
import game
from core.prompt import get_character_color, select
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
    action = select(choices=choices, default="continue")
    if action:
        main_menu_options[action]["callback"]()


save_pos = "\x1b[s"
restore_pos = "\x1b[u"
insert_line = "\x1b[L"
def cursor_up(n: int): return f"\x1b[{n}A"
def cursor_left(n: int): return f"\x1b[{n}D"
def scroll_up(n: int): return f"\x1b[{n}S"


def idle_talk():
    while True:
        if game.idle_talk:
            idle_talk_info = game.idle_talk.pop(0)
            who, text = idle_talk_info["who"], idle_talk_info["text"]
            with threading.Lock():
                time.sleep(1)
                rprint(Text(f"{save_pos}{cursor_up(1)}{cursor_left(999)}{
                       scroll_up(1)}{insert_line}"), end="")
                if who:
                    rprint(
                        Text(f"{who}：", style=get_character_color(who)), end="")
                rprint(Text(text + restore_pos), end="", flush=True)
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

    idle_talk_thread = threading.Thread(target=idle_talk, daemon=True)
    input_thread = threading.Thread(target=user_input, daemon=True)

    idle_talk_thread.start()
    input_thread.start()

    while True:
        pass

except (KeyboardInterrupt, SystemExit):
    rprint(":x: 退出")
    sys.exit(1)
