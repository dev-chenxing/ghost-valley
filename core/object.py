

class Object():
    def __init__(self, id: str, **kwargs):
        self.id = id
        self.name = kwargs["name"] if "name" in kwargs else ""
        self.color: str = None
        self.unit: str = kwargs["unit"] if "unit" in kwargs else ""
        self.objectType: str = "crop"


class Seed(Object):
    def __init__(self, id: str, **kwargs):
        Object.__init__(self, id, **kwargs)
        self.objectType: str = "seed"
        self.color: str = "dark_olive_green3"
        self.value: int = 0
        self.crop: str = kwargs["crop"] if "crop" in kwargs else None
        self.unit: str = "颗"


class Resource(Object):
    def __init__(self, id: str, **kwargs):
        Object.__init__(self, id, **kwargs)
        self.objectType: str = "resource"
        self.color: str = "wheat4"
        self.value: int = 0


class Crop(Object):
    def __init__(self, id, **kwargs):
        Object.__init__(self, id, **kwargs)
        self.objectType: str = "crop"
        self.value: int = 0
        self.unit: str = "个"
        self.color: str = "dark_olive_green3"
