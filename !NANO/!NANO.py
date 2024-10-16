import galgje
import nummerRaadSpel
import steenPapierSchaar
from gameFiles.TMH import the_missing_heirloom

print('\n'
'                    NSNSXNNNSXNNNSXSXSXN\n'
'                  NS                   XSNNS\n'
'               XNN                           XSNNX\n'
'             SNS                                 SN\n'
'              N                                  XNX\n'
'               N                          NNNNNNNX\n'
'               XN                          NN\n'
'                SN                          XNX\n'
'                 NX                           SN                                                NNNNNNNNNNNNNNNNNSSNSSSSSSSSSSSSSSSSSSXXXX      _____________________________\n'
'                 XN                    XNX      NS                                              NNNX                                  XXXX      |            Hoi!           |\n'
'                  NS                     SN      SNNNNNNS      NNS     SNNS   XNNNNSSNSNS       NNN                                    SSX      |        Ik ben D!BZY.      |\n'
'                   N              XNX      NS      NNNNNNNS    NNNNX   NNNS   XNNNNNNNNNN       NNN                                    SXX      |     Wil je een spelletje  |\n'
'                    NS       S      SN      NN      XNNNNNN    NNNNNN  NNNS   XNNNN             NNN    XNNNNNNNNNSSNSSSSSSSSSSSSSSX    SXX     <        met mij spelen?     |\n'
'                     SN      XNX      NS  XNNSNN      NNNNN    NNNNNNNNNNNS   XNNNNSSSSX        NNN    XNNNNNNNNNNSNSSSSSSSSSSSSSSX    XXX      |___________________________|\n'
'                       NN      NN    SNSSSS    NNX     XNNN    NNNSSNNNNNNS   XNNNNNNNNN        NNN    XNNSS       SNNS      SSSSSX    SXX\n'
'                        XNS     NNNNNSN        NNNS   XNNNN    NNNS  SNNNNS   XNNNN             NNN    XNNN    SS   SN   SS   SSSSX    XXX\n'
'                            XSS                NNNNNNNNNNNN    NNNS    NNNS   XNNNNXXXXXX       NNN    XNNNS  SSSS XSSX SSSS SSSSSX    SSX\n'
'                                               SNNNNNNNNNNS    NNNS    NNNS   XNNNNNNNNNN       NNN    XNNSNNNNNNSSNSSSSSSSSSSSSSSX    SXX\n'
'                                                  XXXXX                                         NNN    XNNNNNNSNNNNSSNSSSSSSSSSSSSX    XXX\n'
'                                                                                                NNN    XNX                       SX    XXX\n'
'                                               NNNNNNNNNNNS    NNNNNNNS     XNNNNNNNNNN         NNN    XNS                      SSX    SSX\n'
'                                               SSSNNNNNSSSX   NNNNSNNNN     XNNNSSXSNNNS        NNN    XNNX    SNNNSSNSSSSX    SSSX    XXX\n'
'                                                   NNNN      SNNNS  SNNN    XNNN    NNNN        NNN    XNNNS      XSSSSX      SSSSX    SSX\n'
'                                                   NNNN      NNNN   XNNNS   XNNNS  XNNNS        NNN    XNNNNNS              SSSSSSX    XXX\n'
'                                                   NNNN     SNNNNNNNNNNNN   XNNNNNNNNNNX        NNN    XNNSNNNNNNNSSXXSSSSSSSSSSSSX    SSX\n'
'                                                   NNNN     SNNNNSSSSNNNN   XNNNSX              NNN    XNNNNSNNNNNSSSSSSSSSSSSSSSSX    SXX\n'
'                                                   NNNN     SNNNX    NNNN   XNNN                NNN                                    SXX\n'
'                                                   NNNN     SNNNX    NNNN   XNNN                NNN                                    SXX\n'
'                                                                                                NNNX                                  XXXX\n'
'                                                                                                NNNNNNNSNNSNNNNNNNSNSSSSSSSSSSSSSSSSSSSXXX\n')

#----------------------------------------------------------------------------------------------------------------------------------------------------

def main_menu():

    print('\nWelkom bij One Tap! Wat wil je spelen?\n')
    print("1 = nummer raad spel\n"
          "2 = galgje\n"
          "3 = steen papier schaar\n"
          "4 = Detective D!BZY: TheMissingHeirloom\n"
          "5 = credits\n"
          "6 = programma afsluiten\n")


while True:
    main_menu()

    try:
        menuKeuze = int(input("Voer een cijfer tussen 1 en 6 in: \n"))
        if menuKeuze not in list(range(1, 7)):
            print('Ongeldige invoer. Voer een cijfer tussen 1 & 6 in.\n')
            continue
    except ValueError:
        print("Ongeldige invoer. Voer een cijfer tussen 1 & 6 in.\n")
        continue

    if menuKeuze == 1:
        print("                                                                  _                  _\n"
"                                                                 | |                | |\n"
"  _ __  _   _ _ __ ___  _ __ ___   ___ _ __   _ __ __ _  __ _  __| |  ___ _ __   ___| |\n"
" | '_ \\| | | | '_ ` _ \\| '_ ` _ \\ / _ \\ '__| | '__/ _` |/ _` |/ _` | / __| '_ \\ / _ \\ |\n"
" | | | | |_| | | | | | | | | | | |  __/ |    | | | (_| | (_| | (_| | \\__ \\ |_) |  __/ |\n"
" |_| |_|\\__,_|_| |_| |_|_| |_| |_|\\___|_|    |_|  \\__,_|\\__,_|\\__,_| |___/ .__/ \\___|_|\n"
"                                                                         | |           \n"
"                                                                         |_|           \n")
        nummerRaadSpel.play_nrs()
    elif menuKeuze == 2:
        print(""
            "              _        _      \n"
"             | |      (_)     \n"
"   __ _  __ _| | __ _  _  ___ \n"
"  / _` |/ _` | |/ _` || |/ _ \\\n"
" | (_| | (_| | | (_| || |  __/\n"
"  \\__, |\\__,_|_|\\__, || |\\___|\n"
"   __/ |         __/ |/ |     \n"
"  |___/         |___/__/     \n")
        galgje.play_galgje()
    elif menuKeuze == 3:
        print("      _                                      _                      _                      \n"
"     | |                                    (_)                    | |                     \n"
"  ___| |_ ___  ___ _ __    _ __   __ _ _ __  _  ___ _ __   ___  ___| |__   __ _  __ _ _ __ \n"
" / __| __/ _ \\/ _ \\ '_ \\  | '_ \\ / _` | '_ \\| |/ _ \\ '__| / __|/ __| '_ \\ / _` |/ _` | '__|\n"
" \\__ \\ ||  __/  __/ | | | | |_) | (_| | |_) | |  __/ |    \\__ \\ (__| | | | (_| | (_| | |   \n"
" |___/\\__\\___|\\___|_| |_| | .__/ \\__,_| .__/|_|\\___|_|    |___/\\___|_| |_|\\__,_|\\__,_|_|   \n"
"                          | |         | |                                                  \n"
"                          |_|         |_|                                                  \n")
        steenPapierSchaar.play_sps()
    elif menuKeuze == 4:
        print(""
"  _____       _            _   _             _____  _ ____ ________     __   _______ _                      _         _               _          _      _                       \n"
" |  __ \\     | |          | | (_)           |  __ \\| |  _ \\___  /\\ \\   / /  |__   __| |                    (_)       (_)             | |        (_)    | |                      \n"
" | |  | | ___| |_ ___  ___| |_ ___   _____  | |  | | | |_) | / /  \\ \\_/ (_)    | |  | |__   ___   _ __ ___  _ ___ ___ _ _ __   __ _  | |__   ___ _ _ __| | ___   ___  _ __ ___  \n"
" | |  | |/ _ \\ __/ _ \\/ __| __| \\ \\ / / _ \\ | |  | | |  _ < / /    \\   /       | |  | '_ \\ / _ \\ | '_ ` _ \\| / __/ __| | '_ \\ / _` | | '_ \\ / _ \\ | '__| |/ _ \\ / _ \\| '_ ` _ \\ \n"
" | |__| |  __/ ||  __/ (__| |_| |\\ V /  __/ | |__| |_| |_) / /__    | |  _     | |  | | | |  __/ | | | | | | \\__ \\__ \\ | | | | (_| | | | | |  __/ | |  | | (_) | (_) | | | | | |\n"
" |_____/ \\___|\\__\\___|\\___|\\__|_| \\_/ \\___| |_____/(_)____/_____|   |_| (_)    |_|  |_| |_|\\___| |_| |_| |_|_|___/___/_|_| |_|\\__, | |_| |_|\\___|_|_|  |_|\\___/ \\___/|_| |_| |_|\n"
"                                                                                                                               __/ |                                            \n"
"                                                                                                                              |___/                                             \n")
        the_missing_heirloom()

    elif menuKeuze == 5:
        print("\nMax Parra Torres heeft dit Nano XL appstore project gemaakt.\n"
              "Niet alleen de app store maar ook de games die erin verwerkt zitten."
              "Knap hè? ;)\n"
              "En laten we natuurlijk D!BZY niet vergeten!\n"
              "Die heeft meegeholpen met... uhhh... gezelligheid?\n")
    elif menuKeuze == 6:
        print("Programma wordt afgesloten. \n"
              "D!BZY: Tot de volgende keer!")
        break
