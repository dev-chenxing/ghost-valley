objects = []


class Object:
    def __init__(self, objId, name):
        self.id = objId
        self.name = name
        objects.append(self)


def getObject(objId):
    try:
        return next(obj for obj in objects if obj.id is objId)
    except:
        return None
