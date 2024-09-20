from rich import print
from core.room import Room
import game
from commands.common.position_room import main as position_room


name = "西"


def callback(args: list[str] = None):
    position_room(direction="西")
