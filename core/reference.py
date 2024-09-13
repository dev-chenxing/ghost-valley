from core.object import Object
from core.room import Room


class Reference():
    def __init__(self, object: Object, room: Room):
        self.room = room
        self.object = object
        if self.object.objectType == "crop":
            self.reference_list = self.room.plants
        self.index = self.get_index()
        self.id = f"{object.id}{str(self.index).zfill(6)}"

    def get_index(self) -> str:
        index = 0
        for ref in self.reference_list:
            if ref.object == self.object:
                index = ref.index + 1
        return index

    def delete(self):
        self.reference_list.remove(self)
        del self

    def to_json(self):
        return {
            "id": self.id,
            "object": self.object.id
        }
