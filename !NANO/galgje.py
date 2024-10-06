import random

teRadenWoord = random.randrange(1, 4)

woord1 = "appel"
woord2 = "bomen"
woord3 = "auto"

if teRadenWoord == 1:
    teRadenWoord = woord1
elif teRadenWoord == 2:
    teRadenWoord = woord2
else:
    teRadenWoord = woord3

geradenWoord = []
levens = 10

def letterWeergave(teRadenWoord, geradenWoord):
    """
    geeft de letters weer die al geraden zijn en laat degene die nog niet geraden zijn verborgen
    """
    streepjes = []
    for letter in teRadenWoord:
        if letter in geradenWoord:
            streepjes.append(letter)
        else:
            streepjes.append("_")
    print(f"Nog te raden: {' '.join(streepjes)}")


def pogingen(geradenWoord, teRadenWoord, levens):
    """
    berekent het aantal pogingen dat de gebruiker nog kan doen
    """
    if geradenWoord not in teRadenWoord:
        levens -= 1
    print(f"Je hebt nog {levens} levens.")
    return levens


def galg(levens):
    if levens == 10:
        print("|\n"
              "|\n"
              "|\n"
              "|\n"
              "|")
    elif levens == 9:
        print("__________\n"
              "|\n"
              "|\n"
              "|\n"
              "|\n"
              "|")
    elif levens == 8:
        print("__________\n"
              "|     |\n"
              "|\n"
              "|\n"
              "|\n"
              "|")
    elif levens == 7:
        print("__________\n"
              "|     |\n"
              "|     O\n"
              "|\n"
              "|\n"
              "|")
    elif levens == 6:
        print("__________\n"
              "|     |\n"
              "|     O\n"
              "|     |\n"
              "|\n"
              "|")
    elif levens == 5:
        print("__________\n"
              "|     |\n"
              "|     O\n"
              "|   / |\n"
              "|\n"
              "|")
    elif levens == 4:
        print("__________\n"
              "|     |\n"
              "|     O\n"
              "|   / | \ \n"
              "|\n"
              "|")
    elif levens == 3:
        print("__________\n"
              "|     |\n"
              "|     O\n"
              "|   / | \ \n"
              "|     |\n"
              "|")
    elif levens == 2:
        print("__________\n"
              "|     |\n"
              "|     O\n"
              "|   / | \ \n"
              "|     |\n"
              "|    /")
    elif levens == 1:
        print("Je hebt nog maar 1 leven!\n"
              "__________\n"
              "|     |\n"
              "|     O\n"
              "|   / | \ \n"
              "|     |\n"
              "|    / \ ")
    else:
        print("Je hebt het woord niet geraden.\n"
              "  _____\n"
              " /     \ \n"
              "/   R.  \ \n"
              "|   I.  |\n"
              "|   P.  |\n"
              "|_______|")


#______________________________________________________________


print('*dev code* het te raden woord is:', teRadenWoord)
print("Welkom bij galgje.\n"
          "Raad het woord, letter voor letter.\n"
          "Zijn je levens op? Dan heb je verloren.")

while levens > 0:
    letterWeergave(teRadenWoord, geradenWoord)

    while True:
        try:
            geradenLetter = input("Welke letter wil je proberen? - ").lower()
            if len(geradenLetter) != 1: #controleert of de invoer 1 letter is
                raise ValueError("Voer alstublieft precies één letter in.")
            if not ('a' <= geradenLetter <= 'z'):  #controleert of de invoer een letter is met behulp van ASCII
                raise ValueError("Voer alstublieft een letter in, geen cijfers of speciale tekens.")
            break
        except ValueError as error:
            print(error) #laat de error aan de gebruiker zien

    if geradenLetter not in geradenWoord:
        if geradenLetter in teRadenWoord:
            geradenWoord.append(geradenLetter)
        else:
            levens = pogingen(geradenLetter, teRadenWoord, levens)


    galg(levens)

    alleGeraden = True
    for letter in teRadenWoord:
        if letter not in geradenWoord:
            alleGeraden = False
            break

    if alleGeraden:
        print("Gefeliciteerd! Je hebt het woord geraden!\n")
        break

else:
    print(f"Helaas, het woord was: {teRadenWoord}")
