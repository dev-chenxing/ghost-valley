

class Object():
    def __init__(self, id: str, name: str = ""):
        self.id = id
        self.name = name
        self.color: str = None
        self.unit: str = ""
        self.objectType: str = "crop"

class Seed(Object):
    def __init__(self, id: str, name: str = "", value=0, crop: str = None):
        Object.__init__(self, id, name)
        self.objectType: str = "seed"
        self.color: str = "dark_olive_green3"
        self.value: int = value
        self.crop: str = crop
        self.unit: str = "颗"


class Crop(Object):
    def __init__(self, id):
        Object.__init__(self, id)
        self.objectType: str = "crop"
        self.value: int = 0
        self.unit: str = "个"
        self.color: str = "dark_olive_green3"
