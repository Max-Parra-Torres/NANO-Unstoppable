import random #zorgt ervoor dat de random module werkt

teRadenNum = int(random.randrange(1, 10)) #deze line zorgt voor een random getal tussen 1&10
print("DEV CODE. NUMMER IS: ", teRadenNum)

levens = 3


for leven in range(levens, 0, -1): #deze line zorgt ervoor dat de levens terugtellen tot ze op 0 zijn
    geradenNum = int(input(f"Raad het getal tussen 1 & 10! Je hebt {leven} levens. - "))

    if geradenNum == teRadenNum:
        print('Gefeliciteerd! Je hebt het nummer geraden! (^Ｏ^)')
        exit() #als het geraden nummer hetzelfde is als het te raden nummer krijg je een berichtje en sluit de console zich af
    elif geradenNum > 10:
        print('Het nummer is niet groter dan 10!')
    elif geradenNum < 1:
        print('Het nummer is niet kleiner dan 1!')
    elif leven > 1 and geradenNum > teRadenNum: #als je een fout antwoord geeft krijg je dit bericht tot de laatste poging
        print(f"Het nummer is lager dan {geradenNum}! Probeer het opnieuw.\n")
    elif leven > 1 and geradenNum < teRadenNum:
        print(f"Het nummer is hoger dan {geradenNum}! Probeer het opnieuw.\n")
    else:
        print('Fout! Je hebt geen levens meer! (┛ಠ_ಠ)┛彡┻━┻ ') #als je de laatste poging ook verkeerd hebt krijg je deze tekst te zien
        print(f"Het juiste nummer was: {teRadenNum}")
