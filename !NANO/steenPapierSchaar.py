import random

def uitkomst(player_aanval, computer_aanval):
    """
    Bepaalt de uitkomst van het gevecht.
    1 == verlies, 2 == winst, gelijkspel == 0
    """
    if player_aanval == computer_aanval:
        return 0
    elif player_aanval == 1 and computer_aanval == 2:
        print("Papier verslaat steen.")
        return 1
    elif player_aanval == 1 and computer_aanval == 3:
        print("Steen verslaat schaar.")
        return 2
    elif player_aanval == 2 and computer_aanval == 1:
        print("Papier verslaat steen.")
        return 2
    elif player_aanval == 2 and computer_aanval == 3:
        print("Schaar verslaat papier.")
        return 1
    elif player_aanval == 3 and computer_aanval == 1:
        print("Steen verslaat schaar.")
        return 1
    else:
        print("Schaar verslaat papier.")
        return 2


def pogingen(computer_levens, player_levens, result):
    """
    Geeft het aantal levens weer en stopt het programma als een van de spelers 0 levens heeft.
    """
    if result == 1:
        player_levens -= 1
        print("\nOei... de computer won.")
        print(f"Je hebt nog {player_levens} levens. De computer heeft nog {computer_levens} levens.\n")
    elif result == 2:
        computer_levens -= 1
        print("\nGoed bezig! Je hebt deze ronde gewonnen.")
        print(f"Je hebt nog {player_levens} levens. De computer heeft nog {computer_levens} levens.\n")
    else:
        print("\nGelijkspel!\n")

    return computer_levens, player_levens

# ---------------------------------------------------------------------------------------------------------------------

player_levens = 3
computer_levens = 3

print("Welkom bij steen-papier-schaar!")

while player_levens > 0:

    if computer_levens < 1:
        print('Je hebt gewonnen!')
        break

    computer_aanval = random.randrange(1, 4)
    #print(f"*DEV CODE* computer speelt: {computer_aanval}")

    print("Welke aanval wil je uitvoeren?\n"
          "1: Steen\n"
          "2: Papier\n"
          "3: Schaar\n")
    player_aanval = input("Maak een keuze: ")

    try:
        player_aanval = int(player_aanval)
        if player_aanval not in [1, 2, 3]:
            print("Ongeldige keuze. Kies 1, 2 of 3.")
            continue
    except ValueError:
        print("Ongeldige invoer. Voer een cijfer in.")
        continue

    #zorgen ervoor dan computer_levens en player_levens de goede waarde krijgen gedurende het spel
    result = uitkomst(player_aanval, computer_aanval)
    computer_levens, player_levens = pogingen(computer_levens, player_levens, result)

    if player_levens < 1:
        print('Helaas, je hebt verloren.')
