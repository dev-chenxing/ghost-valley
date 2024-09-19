import game
from rich import print

name = "存档"


def callback(args: list[str] = None):
    game.save_game()
    print("[green]已存档[/green]")
