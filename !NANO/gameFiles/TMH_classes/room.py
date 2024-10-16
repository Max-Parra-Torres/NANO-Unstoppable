class Room:
    def __init__(self, name, description, x=0, y=0, door=None):
        self.name = name
        self.description = description
        self.exits = {}
        self.items = []
        self.npcs = []
        self.x = x
        self.y = y
        self.door = door

    def add_item(self, item):
        self.items.append(item)

    def remove_item(self, item):
        self.items.remove(item)

    def get_items(self):
        return self.items

    def add_npc(self, npc):
        self.npcs.append(npc)  # NPC's worden toegevoegd aan de lijst 'npcs'

    def get_npcs(self):
        return self.npcs  # Retourneer de correcte lijst van NPC's

    def __str__(self):
        return f"{self.name}\n\n{self.description}\n"
