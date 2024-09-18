

class Room:
    def __init__(self, id: str, **kwargs):
        self.id: str = id
        self.name = id
        self.plants: list = []
        self.grid_x = kwargs["grid_x"]
        self.grid_y = kwargs["grid_y"]
        self.callback =  kwargs["callback"]
        self.can_change_room = kwargs["can_change_room"]

    def to_json(self):
        plants = list(map(lambda plant: plant.to_json(), self.plants))
        return {
            "id": self.id,
            "plants": plants
        }
