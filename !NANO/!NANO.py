import galgje
import nummerRaadSpel
import steenPapierSchaar

print("1 = nummer raad spel\n"
      "2 = galgje\n"
      "3 = steen papier schaar\n"
      "4 = **nog maken**\n"
      "5 = **detective game**\n"
      "6 = credits\n"
      "7 = programma afsluiten")

while True:

    menuKeuze = input("Maak een keuze: ")

    try:
        moeilijkheidsgraad = int(moeilijkheidsgraad)
        if moeilijkheidsgraad not in range(0, 8):
            print("Ongeldige keuze. Kies een nummer tussen 1 & 7")
            continue
    except ValueError:
        print("Ongeldige invoer. Voer een cijfer in.")
        continue


while True:

    if menuKeuze == 1:
        nummerRaadSpel
    elif menuKeuze == 2:
        galgje
    elif menuKeuze == 3:
        steenPapierSchaar
    elif menuKeuze == 4:
        print("dev error :(")
    elif menuKeuze == 5:
        print("dev error :(")
    elif menuKeuze == 6:
        print("Max Parra Torres heeft dit nano appstore project gemaakt.\n"
              "Niet alleen de app store maar ook de games die erin verwerkt zitten.\n"
              "knap hè? ;)")
    else:
        break