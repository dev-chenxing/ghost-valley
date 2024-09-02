from object import Object


class Crop(Object):
    def __init__(self, id, name):
        Object.__init__(self, id, name, objectType="crop")
        self.value = 0
