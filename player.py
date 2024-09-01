from object import Object


class Player(Object):
    def __init__(self, objId, name):
        Object.__init__(self, objId, name)
        self.coins = 0
        self.inventory = []
