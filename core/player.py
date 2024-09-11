class Player:
    def __init__(self, name="新鬼") -> None:
        self.name = name
        self.female = True
        self.attributes = [19, 26, 0, 2, 30, 18]
        self.coins = 10
        self.inventory = []
        self.title = "鬼众"
        self.potential = 99  # 资质平平
