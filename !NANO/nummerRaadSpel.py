def play_nrs():
    """
    speelt nummer raad spel
    """

    import random

    teRadenNum = int(random.randrange(1, 10))
    #print("DEV CODE. NUMMER IS: ", teRadenNum)

    levens = 3

    #--------------------------------------------------------------------------------------

    while levens > 0:

        geradenNum = input(f"D!BZY denkt aan een getal tussen 1 & 10. Jij moet het proberen te raden! Je hebt {levens} levens. - ")

        try:
            geradenNum = int(geradenNum)
            if geradenNum not in range(1, 11):
                print("D!BZY: Raad een nummer tussen de 1 & 10!")
                continue
        except ValueError:
            print("D!BZY: Voer een geldig getal in.")
            continue

        levens -= 1

        if geradenNum == teRadenNum:
            print('D!BZY: Gefeliciteerd! Je hebt het nummer geraden! |^Ｏ^|')
            break
        elif geradenNum > teRadenNum:
            print(f"D!BZY: Het nummer is lager dan {geradenNum}! Probeer het opnieuw.\n")
        else:
            print(f"D!BZY: Het nummer is hoger dan {geradenNum}! Probeer het opnieuw.\n")

        if levens == 0:
            print('D!BZY: Fout! Je hebt geen levens meer! |┛ಠ_ಠ|┛彡┻━┻'
                  f'Het juiste nummer was: {teRadenNum}')
            break
