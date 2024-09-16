

class Room:
    def __init__(self, id: str):
        self.id: str = id
        self.name = id
        self.plants: list = []

    def to_json(self):
        plants = list(map(lambda plant: plant.to_json(), self.plants))
        return {
            "id": self.id,
            "plants": plants
        }
