class Quest:
    def __init__(self, id: str, stages: dict[int, str], description: str):
        self.id: str = id
        self.stage: int = None
        self.stages: dict[int, str] = stages
        self.finished: bool = False
        self.description: str = description
