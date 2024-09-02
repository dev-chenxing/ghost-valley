from object import Object


class Player(Object):
    def __init__(self, id, name):
        Object.__init__(self, id, name, objectType="player")
        self.coins = 0
        self.inventory = []
