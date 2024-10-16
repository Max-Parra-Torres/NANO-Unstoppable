# Defined a class for Items
# Expand items with superpower actions
class Item:
    def __init__(self,name: str, location: str, description: str, damage: int):
        self.name = name
        self.location = location
        self.description = description
        self.damage = damage

    def __str__(self):
        return self.location
