from rich import print
from commands.common.position_room import main as position_room
import game

name = "北"
alias = "north"

def callback(args: list[str] = None):
    position_room(direction="北")
