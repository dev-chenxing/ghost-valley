from rich import print
import game

name = "任务"


def callback(args: list[str] = None):
    game.print_quests()
