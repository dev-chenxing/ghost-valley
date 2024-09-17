class Quest:
    def __init__(self, id: str, stages: dict[int, str]):
        self.id = id
        self.stages = stages
