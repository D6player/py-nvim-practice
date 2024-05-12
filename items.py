""" Items implementation """

class Item():
    def __init__(self, name: str):
        self.name = name
        
class Armor(Item):
    def __init__(self, name: str, armor: int, weight: int):
        super().__init__(name)
        self.armor = armor
        self.weight = weight

    def value(self):
        return self.armor - self.weight

class Weapon(Item):
    def __init__(self, name: str, damage: int, accuracy: int, firerate: int):
        super().__init__(name)
        self.damage = damage
        self.accuracy = accuracy
        self.firerate = firerate

    def value(self):
        return self.damage + self.accuracy + self.firerate

class Usable(Item):
    def __init__(self, name: str):
        super().__init__(name)

# Armor
basic_vest = Armor("Basic vest", 1, 1)
heavy_armor = Armor("Heavy armor", 4, 3)

# Weapons
pistol = Weapon("Pistol", 1, 1, 1) 
ak_47 = Weapon("AK47", 3, 1, 2)

# Usables
lucky_charm = Usable("Lucky charm")

# All items
items: list[Item] = [
    lucky_charm,
    heavy_armor,
    ak_47,
]

