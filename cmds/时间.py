from core import timer
from rich import print


def callback(args: list[str]):
    print(f"现在 游戏 时间是：[bright_yellow]{
        timer.game_time.format()}[/bright_yellow]")
