def play_galgje():
    """
    speelt galgje
    """
    import random
    import time

    def woord(moeilijkheidsgraad):
        """
        geeft een willekeurig woord naar aanleiding van de gekozen moeilijkheidsgraad
        """
        randomNummer = random.randrange(0, 5)

        if moeilijkheidsgraad == 1:
            with open("gameFiles\galgje\galgjeMakkelijk", "r") as woorden:
                woordenlijst = woorden.readlines()
                teRadenWoord = woordenlijst[randomNummer].strip()
        elif moeilijkheidsgraad == 2:
            with open("gameFiles\galgje\galgjeMoeilijk", "r") as woorden:
                woordenlijst = woorden.readlines()
                teRadenWoord = woordenlijst[randomNummer].strip()
        elif moeilijkheidsgraad == 3:
            with open("gameFiles\galgje\galgjeOnmogelijk", "r") as woorden:
                woordenlijst = woorden.readlines()
                teRadenWoord = woordenlijst[randomNummer].strip()

        return teRadenWoord


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
                  "|     O  <[ Help! ] \n"
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


    #--------------------------------------------------------------------------------------


    geradenWoord = []
    levens = 10

    print("D!BZY: Welkom bij galgje.\n"
              "Raad het woord, letter voor letter.\n"
              "Zijn je levens op? Dan heb je verloren.\n")

    username = input("Onder welke naam wil je spelen?: ")

    while True:

        moeilijkheidsgraad = input("D!BZY: Welke moeilijkheidsgraad wil je spelen?\n"
                                   "1 = makkelijk\n"
                                   "2 = moeilijk\n"
                                   "3 = onmogelijk (test je woordenschat)\n" #dit zijn 5 van de meest gegoogelde nederlandse woorden
                                   "Maak een keuze: ")

        try:
            moeilijkheidsgraad = int(moeilijkheidsgraad)
            if moeilijkheidsgraad not in [1, 2, 3]:
                print("D!BZY: Ongeldige keuze. Kies uit 1, 2 of 3")
                continue
        except ValueError:
            print("D!BZY: Ongeldige invoer. Voer een cijfer in.")
            continue

        break

    teRadenWoord = woord(moeilijkheidsgraad)

    #-------------------------------------------------------#
    #print('*dev code* het te raden woord is:', teRadenWoord)
    #-------------------------------------------------------#

    while levens > 0:

        letterWeergave(teRadenWoord, geradenWoord)

        while True:

            try:
                geradenLetter = input("D!BZY: Welke letter wil je proberen? - ").lower()
                if len(geradenLetter) != 1: #controleert of de invoer 1 letter is
                    raise ValueError("D!BZY: Voer alsjeblieft precies één letter in.")
                if not ('a' <= geradenLetter <= 'z'):  #controleert of de invoer een letter is met behulp van ASCII
                    raise ValueError("D!BZY: Voer alsjeblieft een letter in, geen cijfers of speciale tekens.")
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

        uitkomst = "niet geraden"

        if alleGeraden:
            print(f"D!BZY: Gefeliciteerd! Je hebt het woord '{teRadenWoord}' geraden!\n")
            uitkomst = "geraden"
            break


    else:
        print(f"D!BZY: Helaas, het woord was: {teRadenWoord}"
              f"Geef het niet op! D!BZY gelooft in je! |っᵔ◡ᵔ|っ")

    #houdt een logboek bij
    numPoging = 10 - levens + len(teRadenWoord)
    with open("gameFiles\galgje\galgjeLogboek", "a") as log:
        log.write(f"{username} heeft het woord {teRadenWoord} op {time.strftime('%d/%b/%Y, %H:%M')} {uitkomst}. {username} heeft er {numPoging} keer over gedaan.\n"
                  "-------------------------------------------------------------------------------------------\n")
