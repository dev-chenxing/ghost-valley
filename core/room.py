

class Room:
    def __init__(self, id: str, **kwargs):
        self.id: str = id
        self.name = id
        self.plants: list = []
        self.x = kwargs["x"] if "x" in kwargs else None
        self.y = kwargs["y"] if "y" in kwargs else None

    def to_json(self):
        plants = list(map(lambda plant: plant.to_json(), self.plants))
        return {
            "id": self.id,
            "plants": plants
        }
