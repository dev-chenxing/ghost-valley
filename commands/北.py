from rich import print
import game


def callback(args: list[str] = None):
    room = game.player.room
    game.position_room([room.x, room.y+1])
