class Npc:
    def __init__(self, name: str, description: str, health: int, dialogue: str, room: str):
        self.name = name
        self.health = health
        self.description = description
        self.dialogue = dialogue
        self.room = room

    def conversation(self, player):
        print(f"{self.name}\n{self.description}\n\"{self.dialogue}\n\"")



    def __str__(self):
        return self.description
