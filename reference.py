from object import getObject


class Reference():
    def __init__(self, obj):
        if type(obj) is str:
            self.object = getObject(obj)
        else:
            self.object = obj

    def delete(self):
        del self
