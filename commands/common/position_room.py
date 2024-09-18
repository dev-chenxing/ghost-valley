from core.room import Room
import game


def can_change_room(room_from: Room, room_to: Room):
    return room_from.can_change_room(leaving=True) and room_to.can_change_room(leaving=False)


def main(offset_x: int, offset_y: int):
    room_from: Room = game.player.room
    room_to: Room = game.get_room(
        x=room_from.grid_x+offset_x, y=room_from.grid_y+offset_y)
    if can_change_room(room_from=room_from, room_to=room_to):
        game.position_room(room_to)
