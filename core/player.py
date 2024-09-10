from lib.zhongwen.number import 中文数字


class Object():
    def __init__(self, id: str, name: str):
        self.id = id
        self.name = name


class Seeds(Object):
    def __init__(self, id: str, name: str, value=0, crop: str=None):
        Object.__init__(self, id, name)
        self.objectType = "seeds"
        self.value = value
        self.crop = crop
        self.unit = "袋"


class ItemStack():
    def __init__(self, object: Object, count=1):
        self.object = object
        self.count = count

    def to_string(self):
        return f"{中文数字(self.count)}{self.object.unit}{self.object.name}"



class Reference():
    def __init__(self, object: Object):
        self.object = object

    def delete(self):
        del self

white_radish_seed = Seeds(id="white_radish_seed",
                          name="白萝卜种子", crop="white_radish")
carrot_seed = Seeds(id="carrot_seed",
                    name="胡萝卜种子", crop="carrot")


class Player:
    def __init__(self, name="新鬼") -> None:
        self.name = name
        self.coins = 10
        self.inventory = [ItemStack(object=white_radish_seed, count=1), ItemStack(
            object=carrot_seed, count=1)]


item_colors = {
    "seeds": "dark_olive_green3"
}


def get_item_color(object: Object) -> str:
    return item_colors[object.objectType]
