from core import timer
from rich import print

name = "时间"


def callback(args: list[str] = None):
    print(f"现在 游戏 时间是：[bright_yellow]{
        timer.game_time.format()}[/bright_yellow]")
