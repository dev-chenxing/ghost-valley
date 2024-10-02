class NPC:
    def __init__(self, id: str, **kwargs) -> None:
        self.id = id
        self.name = kwargs["name"] if "name" in kwargs else ""
        self.color: str = kwargs["color"] if "color" in kwargs else ""
        self.objectType: str = "npc"
        self.female = True
