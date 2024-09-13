import game
from lib.zhongwen.number import 中文数字
from rich import print


def callback(args: list[str] = None):
    print(f"{game.player.name}摸了摸自己荷包里的[light_goldenrod1]{
        中文数字(game.player.coins)}文钱[/light_goldenrod1]")
