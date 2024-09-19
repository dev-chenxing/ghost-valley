import game
from lib.chinese_number import 中文数字
from rich import print

name = "荷包"


def callback(args: list[str] = None):
    print(f"{game.player.name}摸了摸自己荷包里的[light_goldenrod1]{
        中文数字(game.player.coins)}文钱[/light_goldenrod1]")
