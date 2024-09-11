from rich import print
from core import timer
from core.object import Object
import game
from lib.zhongwen.number import 中文数字


def process_input(cmd):
    if cmd == "时间":
        print(f"现在 游戏 时间是：[bright_yellow]{
            timer.game_time.format()}[/bright_yellow]")
    elif cmd == "荷包":
        print(f"{game.player.name}摸了摸自己荷包里的[light_goldenrod1]{
              中文数字(game.player.coins)}文钱[/light_goldenrod1]")
    elif cmd == "背篓":
        item_stack_strings: list[str] = []
        for item_stack in game.player.inventory:
            color = item_stack.object.color
            item_stack_strings.append(
                f"[{color}]{item_stack.to_string()}[/{color}]")
        print(f"背篓里放了{"，".join(item_stack_strings)}")
    elif cmd == "种白萝卜种子":
        item = game.get_object("white_radish_seed")
        game.plant(seed=item, room=game.get_room(id="farm"))
    elif cmd == "种下全部白萝卜种子":
        item = game.get_object("white_radish_seed")
        for _ in range(game.get_item_count(item)):
            game.plant(seed=item)
    elif cmd == "田":
        if not game.get_room(id="farm").plants:
            print("田里还荒着，没种东西")
        else:
            plant_strings = []
            plants: dict[Object, int] = {}
            for ref in game.get_room(id="farm").plants:
                if ref.object not in plants:
                    plants[ref.object] = 1
                else:
                    plants[ref.object] += 1
            for plant, count in plants.items():
                color = plant.color
                plant_strings.append(
                    f"[{color}]{中文数字(count, 两=True)}{plant.unit}{plant.name}[/{color}]")
            print(f"田里种着{"，".join(plant_strings)}")
    elif cmd == "保存":
        game.save_game()
