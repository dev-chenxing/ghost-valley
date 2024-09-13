from core.item_stack import ItemStack


class Player:
    def __init__(self, name="新鬼") -> None:
        self.name = name
        self.female = True
        self.intellect = 0  # 才智
        self.physique = 0  # 体魄
        self.agility = 0  # 身手
        self.perception = 0  # 六识
        self.coins = 10
        self.inventory: list[ItemStack] = []
        self.title = "鬼众"
        # self.potential = 99  # 资质平平
