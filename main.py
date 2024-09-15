import threading
from rich import print
from InquirerPy import inquirer
from InquirerPy.base.control import Choice

from command import process_input
import game
from core.player import Player
from core import timer

from content.character_creation import character_creation

from content.title import title
print(title)


def main_menu():
    action = inquirer.select(
        message="",
        choices=[
            "新游戏",
            "载入",
            Choice(value=None, name="离开"),
        ],
        default=None,
        qmark="",
        amark="",
        show_cursor=False,
        transformer=lambda _: ""
    ).execute()



try:
    main_menu()

    timer.game_time = timer.Time()
    timer.real_time = timer.Time()
    game_time_thread = threading.Thread(
        target=timer.game_time_thread, daemon=True)
    real_time_thread = threading.Thread(
        target=timer.real_time_thread, daemon=True)

    farm = game.create_room(id="farm")
    game.player = Player()
    # character_creation()

    white_radish = game.create_object(
        objectType="crop", id="white_radish", name="白萝卜")
    white_radish_seed = game.create_object(
        objectType="seed", id="white_radish_seed", name="白萝卜种子", crop="white_radish")
    carrot = game.create_object(objectType="crop", id="carrot", name="胡萝卜")
    carrot_seed = game.create_object(
        objectType="seed", id="carrot_seed", name="胡萝卜种子", crop="carrot")
    twig = game.create_object(objectType="resource",
                              id="twig", name="树枝", unit="根")
    game.add_item(item=white_radish_seed, count=15)
    game.add_item(item=carrot_seed)

    game.save_game()

    game_time_thread.start()
    real_time_thread.start()

    while True:
        cmd = input("> ")
        process_input(cmd)

except (KeyboardInterrupt, SystemExit):
    print(":x: 退出")
