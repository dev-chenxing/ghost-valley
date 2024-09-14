import game
from rich import print


def callback(args: list[str] = None):
    game.save_game()
    print("[green]已存档[/green]")
