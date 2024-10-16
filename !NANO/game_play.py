from gameFiles.TMH_classes.room import Room
from gameFiles.TMH_classes.item import Item
from gameFiles.TMH_classes.player import Player
from gameFiles.TMH_classes.npc import Npc
from gameFiles.TMH_classes.door import Door
from enum import Enum


class Option(Enum):
    MOVE = 1
    TALK = 2
    PICK_UP = 3
    INVENTORY = 4
    PRINT_MAP = 5
    ACCUSE = 6
    QUIT = 7


# Game Setup
def setup_game(player_name):
    # Create rooms
    kitchen = Room(f"Kitchen",
                   f"You walk into the kitchen. \n"
                   f"{player_name}: 'What a mess.' you think to yourself.\n"
                   f"Even after such a big dinner party you didn't expect this much of a mess.\n"
                   f"After all, Helen and Marge are not the types to leave dirty dishes laying around."
                   f"{player_name}: 'Maybe I should look around to see if I can find something useful.'\n",
                   x=0, y=0)

    ballroom = Room("Ballroom",
                    "A large room with shiny wooden floors.\n"
                    "It looks like a nice place to dance. Although nobody is dancing.\n"
                    "The ceiling is so far up that I can barely see all the details of the beautiful painting- \n"
                    "That someone so meticulously painted.\n"
                    f"{player_name}: 'How did they even get all the way up there?' you think to yourself.\n",
                    x=-1, y=0)

    dining_hall = Room("Dining Hall",
                       "A vast room with a long table where a feast could be held.\n"
                       "Marge, one of the cooks, is sitting in a corner and looks quite stressed.\n"
                       "You notice something under the chair leg of where Helen was sitting.\n",
                       x=-1, y=1)

    library = Room("Library",
                   "A quiet place filled with books.\n"
                   "There is not much to see here.\n"
                   "Except for a small card that is laying in the fireplace.\n",
                   x=0, y=-1)

    garden = Room("Garden",
                  "there is a path leading to the tea house.\n"
                  "Along the path there is beds of different colored flowers.\n"
                  "You look at them while David is working on them.\n"
                  "If you look at it from the kitchen the gradient of flowers shifts from pink to orange to blue to purple.",
                  x=1, y=0)

    study = Room("Study",
                 "You've entered a dimly lit Study Room, the scent of old books  filling the air as you open the door.\n"
                 "You see mark reading a book in one of the chairs.",
                 x=0, y=1)

    tea_house = Room("Tea House",
                     "You open the glass door and are immediately hit with the stuffy atmosphere inside.\n"
                     "To your horror you see Helen passed out on a bench.\n"
                     "You look over to your left and see the missing heirloom on a small round table.\n"
                     f"{player_name}: 'I could make a judgement now.' You think to yourself\n"
                     "But you know you could also keep quite for now and keep looking for more clues...",
                     x=2, y=0, door = Door(code = "1234"))


    # List of all rooms
    rooms = [kitchen, ballroom, dining_hall, library, garden, study, tea_house]



    # Create items
        #kitchen
    recipe_card = Item("Recipe card ",
                       "A recipe card is laying next to the stove.\n",
                                      f"{player_name}: 'Wait a second.'\n"
                                      "you mumble to yourself.\n"
                                       f"{player_name}: 'This isn't what was served to the guests.\n"
                                       "I might be looking into this a bit too hard.'\n"
                                       "You start to question yourself as you look at the card you are holding.\n"
                                       f"{player_name}: 'I might be...'", 0)

    note_to_marge = Item("Note to Marge ", "You see a piece of paper in the trashcan.\n",
                         "The letter reads:\n\n"
                                           "You know what I told you Marge.\n"
                                           "There is no choice for you to make\n"
                                           "You either follow our request or you will be fired!\n"
                                           "And don't you dare bring our little agreement up to anyone else.\n"
                                           "~ Francis\n\n"
                                           f"{player_name}: 'What is Francis talking about?\n"
                                          f"This letter does not sound very friendly.'", 0)

        #ballroom
    card_with_names = Item("Card with names ", "A small card is laying on one of the tables that are off to the side of the room.\n",
                                              "It has the names of all the guests on it.\n"
                                              "One of them is circled with red marker... Helen.\n"
                                              f"{player_name}: 'Now that I think about it.\n"
                                              "I haven't seen Helen at all after we finished up in the dining hall.' you think to yourself.", 0)

        #dining hall
    torn_fabric = Item("Torn piece of fabric ", "A torn piece of fabric is stuck under one of the chair's legs.\n",
                                               f"{player_name}: 'This is from Helen's dress.'"
                                               "You wonder what went down here when you were in the ballroom with the rest of the guests."
                                               f"{player_name}: 'I need to get to the bottom of this.'", 0)

        #library
    burnt_card = Item("Burnt card", "You see a card in the fireplace.",
                      "The card is partially burnt, but you can make up some of the words:\n"
                                    "#### and it will work Fra#######\n"
                                    "Believe m######### and no one will know\n"
                                    "##### was us######################\n"
                                    "##rk\n"
                      f"{player_name}: 'Mark?' You think to yourself.", 0)

        # study
    diary_mark = Item("Mark's diary", "You see Mark's diary open on a shelve behind him.", "The diary reads:\n"
                                                                                           "Dear diary,\n"
                                                                                           "I have a new favorite color\n"
                                                                                           "My list of favorite colors as of now is as follows\n"
                                                                                           "1. pink\n"
                                                                                           "2. orange\n"
                                                                                           "3. blue\n"
                                                                                           "4. purple\n"
                                                                                           "5. red\n"
                                                                                           "6. beige\n"
                                                                                           "7. green\n\n"
                                                                                           f"{player_name}: 'Who actually keeps a diary?'", 0)

    # Place items in rooms
    kitchen.add_item(recipe_card)
    kitchen.add_item(note_to_marge)
    ballroom.add_item(card_with_names)
    dining_hall.add_item(torn_fabric)
    library.add_item(burnt_card)
    study.add_item(diary_mark)


    #create npc's
    mark = Npc("Mark", "A very... Lets just say big man.\n"
                       "Mark is wearing very expensive looking clothes and has a stern look on his face.\n"
                       "He is looking right at you.", 1, "I don't care what you do just make sure this gets solved quickly.", "Study")

    marge = Npc("Marge", "A pretty young woman, probably in her mid 20's.\n"
                         "Her clothes are covered in pieces of food and flour.\n"
                         "She does not look up at you", 1, "I can't talk to you. I'm sorry.", "Dining Hall")

    francis = Npc("Francis", "Francis looks like a bouncer.\n"
                             "He has a very large and muscular build.\n"
                             "Definitely not someone you would want to be in a fist fight with.", 1, "Don't try to do anything foolish detective. \nI'll be watching you.", "Garden")

    david = Npc("David", "David is not a people person.\n"
                         "He does not like talking.\n"
                         "The only thing that makes him excited is his job, gardening.", 1, "Please just let me do my work.", "Garden")


    #add npc to room
    dining_hall.add_npc(marge)
    study.add_npc(mark)
    ballroom.add_npc(francis)
    garden.add_npc(david)


    # Create a player and start the TMH_classes in the ballroom
    player_in_the_ballroom = Player(player_name, ballroom, rooms)

    return player_in_the_ballroom



# Main TMH_classes loop
def play_game(user):
    while True:
        print(f"\n\n{user.name}, you are in the {user.current_room}")
        command = int(input("Choose an option:"
                            "\n1: Move\n2: Talk to someone\n3: Look for clue's"
                            "\n4: Inventory\n5: Display map\n6: Accuse someone"
                            "\n7: Quit\n\nOption: "))

        if command == Option.MOVE.value:
            direction = input("Provide direction (left|right|up|down): ")
            user.move(direction)

        elif command == Option.TALK.value:
            npcs_in_room = user.current_room.get_npcs()

            if npcs_in_room:
                for npc in npcs_in_room:
                    npc.conversation(user)
            else:
                print("There's no one to talk to in this room.")

        elif command == Option.PICK_UP.value:
            items = user.current_room.get_items()
            if len(items):
                print("The following items are available: ")
                print("0. I don't want to pick anything up")
                for item in items:
                    print(f"1. {item.location}")
                chosen_item = int(input("Which item would you like to pick up: "))
                if chosen_item != 0:
                    user.pick_up(items[chosen_item - 1].name)
                else:
                    continue
            else:
                print("There are no items available")

        elif command == Option.INVENTORY.value:
            user.show_inventory()

        elif command == Option.PRINT_MAP.value:
            user.display_map()

        elif command == Option.ACCUSE.value:
            accused = input("Who do you want to accuse? (This decision is final)\n"
                            "1. Marge\n"
                            "2. Francis\n"
                            "3. David\n"
                            "4. Mark\n"
                            "5. Choose later\n"
                            "Choice: ")
            if accused == "1" or accused == "3":
                print("unfortunately you did not solve the mystery.\n To find out who did it you can play again.")
                break
            elif accused == "2":
                print("You partially solved the mystery.\n Play again to solve the rest and find out what the real story is.")
                break
            elif accused == "4":
                print("You solved the mystery!\nMark made francis force Marge to poison Helen so Mark could own the heirloom all on his own.")
                break
            elif accused == "5":
                continue
            else:
                print("Type a number from 1 - 5 please.")
                continue
        elif command == Option.QUIT.value:
            quit_choice = input("Are you sure you want to quit? (This decision is final)\n"
                                "y/n: ")
            if quit_choice == "y" or quit_choice == "Y":
                print("Thanks for playing!")
                break
            elif quit_choice == "n" or quit_choice == "N":
                continue
            else:
                print("Please only enter y or n. (y = yes & n = no)")
        else:
            print("Invalid command.")


def the_missing_heirloom():
    # Run the TMH_classes logic
    name = "Detective D!BZY"
    print('This is a text based detective TMH_classes.\n'
          'You play as the famous detective D!BZY.\n'
          'Tonight is very special.\n'
          'You have been invited to one of the party\'s of the well known baron & baroness Decuard.\n'
          'These party\'s are known for their lavish dinners and amazing live orchestra\'s in the ballroom.\n'
          'Because you know them for a while you can call them by their first names.\n'
          'Mark and Helen have asked for your help in the past.\n'
          'Without you realizing it going into the party, they will need your help again tonight...\n'
          'The Decuard family heirloom has gone missing and it is your job to get to the bottom of this mess.\n')
    player = setup_game(name)
    play_game(player)
if __name__ == "__main__":
    the_missing_heirloom()