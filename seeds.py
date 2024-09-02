from object import Object


class Seeds(Object):
    def __init__(self, id, name):
        Object.__init__(self, id, name, objectType="seeds")
        self.value = 0
        self.crop = None
