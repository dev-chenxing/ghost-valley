from core.object import Object
from core.room import Room


def get_reference_index(room: Room, object: Object):
    index = 0
    return str(index).zfill(6)


class Reference():
    def __init__(self, object: Object, room: Room):
        index = get_reference_index(room=room, object=object)
        self.id = f"{object.id}{index}"
        self.object = object

    def delete(self):
        del self

    def to_json(self):
        return {
            "id": self.id,
            "object": self.object.id
        }
