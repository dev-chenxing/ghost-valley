from core.item_stack import ItemStack


class Player:
    def __init__(self) -> None:
        self.surname = "玩"
        self.given_name = "家"
        self.name = "玩家"
        self.female = True
        self.intellect = 0  # 才智
        self.physique = 0  # 体魄
        self.agility = 0  # 身手
        self.perception = 0  # 六识
        self.coins = 10
        self.inventory: list[ItemStack] = []
