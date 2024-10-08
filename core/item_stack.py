from core.object import Object
from lib.chinese_number import 中文数字


class ItemStack():
    def __init__(self, object: Object, count=1):
        self.object = object
        self.count = count

    def to_string(self):
        return f"{中文数字(self.count)}{self.object.unit}{self.object.name}"

    def to_json(self):
        return {
            "object": self.object.id,
            "count": self.count
        }
