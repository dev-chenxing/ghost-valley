from core.object import Object
import game
from lib.zhongwen.number import 中文数字
from rich import print


def callback(args: list[str] = None):
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
