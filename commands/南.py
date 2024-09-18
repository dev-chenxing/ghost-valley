from rich import print
from core.room import Room
import game


def callback(args: list[str] = None):
    room: Room = game.player.room
    if room.can_change_room():
        game.position_room([room.grid_x, room.grid_y-1])
