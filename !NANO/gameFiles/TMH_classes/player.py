# Ideas to extend functionality:
# Add health & resource management:
# - add health attribute
# - health decreases when you pass through the fire room
# - health increases when you find a health item
# - use your creativity
# Define a class for the Player

class Player:
    def __init__(self, name, current_room, rooms):
        self.name = name
        self.current_room = current_room
        self.inventory = []
        self.rooms = rooms
        self.can_access_tea_house = False

    def move(self, direction):
        new_x, new_y = self.current_room.x, self.current_room.y

        # Adjust coordinates based on direction
        if direction == "left":
            new_x -= 1
        elif direction == "right":
            new_x += 1
        elif direction == "up":
            new_y -= 1
        elif direction == "down":
            new_y += 1
        else:
            print("Invalid direction.")
            return

        # Find the room at the new coordinates
        new_room = None
        for room in self.rooms:
            if room.x == new_x and room.y == new_y:
                new_room = room
                break

        #controleert of de nieuwe kamer een deur heeft
        if new_room:
            if new_room.door:  # Controleer of er een deur is
                if new_room.door.is_locked():
                    print("The door is locked. You need to enter the 4 digit code in order to enter this room.")
                    attempt = input("Enter the code to unlock the door: ")
                    if new_room.door.unlock(attempt):
                        self.current_room = new_room
                        print(f"You are now in the {new_room.name}.")
                else:
                    self.current_room = new_room
                    print(f"You are now in the {new_room.name}.")
            else:
                self.current_room = new_room
                print(f"You are now in the {new_room.name}.")
        else:
            print("You can't go that way.")

    def pick_up(self, chosen_item_name):
        for item in self.current_room.items:
            if item.name == chosen_item_name:
                self.inventory.append(item)
                self.current_room.remove_item(item)
                print(f"You picked up the {chosen_item_name}.")
                return
        print(f"There is no {chosen_item_name} here.")

    def show_inventory(self):
        if self.inventory:
            print("You are carrying:")
            for item in self.inventory:
                print(f"- {item.name}\n{item.description}\n")
        else:
            print("Your inventory is empty.")

    def show_map(self):
        self.display_map()

    def display_map(self):
        print(f'You are currently in the {self.current_room}\n\n'
              '	            [ library ]\n'
              '[ ballroom    ] [ kitchen ] [ garden ] [ tea house ]\n'
              '[ dining hall ] [ study   ]\n')
