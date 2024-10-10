import random

teRadenNum = int(random.randrange(1, 10))
print("DEV CODE. NUMMER IS: ", teRadenNum)

levens = 3

#--------------------------------------------------------------------------------------

while levens > 0:

    geradenNum = input(f"Raad het getal tussen 1 & 10! Je hebt {levens} levens. - ")

    try:
        geradenNum = int(geradenNum)
        if geradenNum not in range(1, 11):
            print("Raad een nummer tussen de 1 & 10!")
            continue
    except ValueError:
        print("Voer een geldig getal in.")
        continue

    levens -= 1

    if geradenNum == teRadenNum:
        print('Gefeliciteerd! Je hebt het nummer geraden! (^Ｏ^)')
        break
    elif geradenNum > teRadenNum:
        print(f"Het nummer is lager dan {geradenNum}! Probeer het opnieuw.\n")
    else:
        print(f"Het nummer is hoger dan {geradenNum}! Probeer het opnieuw.\n")

    if levens == 0:
        print('Fout! Je hebt geen levens meer! (┛ಠ_ಠ)┛彡┻━┻')
        print(f"Het juiste nummer was: {teRadenNum}")
        break
