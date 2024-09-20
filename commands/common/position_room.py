from core.room import Room
import game


def can_change_room(room_from: Room = None, room_to: Room = None):
    return room_from.can_change_room(room_to=room_to) and room_to.can_change_room(room_from=room_from)


def get_offset(direction: str):
    match direction:
        case "东":
            return (1, 0)
        case "南":
            return (0, -1)
        case "西":
            return (-1, 0)
        case "北":
            return (0, 1)
        case _:
            return None


def main(direction: str):
    offset = get_offset(direction)
    room_from: Room = game.player.room
    room_to: Room = game.get_room(
        x=room_from.grid_x+offset[0], y=room_from.grid_y+offset[1])
    if not room_to:
        print(f"{direction}边没有路可走")
        return
    if can_change_room(room_from=room_from, room_to=room_to):
        game.position_room(room_to)
