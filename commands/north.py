from rich import print
from commands.common.position_room import main as position_room
import game

name = "北"


def callback(args: list[str] = None):
    position_room(offset_x=0, offset_y=1)
