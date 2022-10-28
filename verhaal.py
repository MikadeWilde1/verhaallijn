from time import sleep
def printsleep(sleeptime, txt):
    sleep(sleeptime)
    print(txt)




def intro():
    printsleep(0.5, "Je wordt wakker in een abnormale wereld, waar niets is wat je denkt dat het is. ")
    printsleep(0.5, "Je weet niet waar je bent beland of hoe je er bent gekomen. Wat je wel weet is dat je hier zo snel mogelijk weg wilt zijn. ")
    printsleep(0.5, "Maar dat is nog niet zo makkelijk als je denkt dat het is ")
    printsleep(0.5, "Je kijkt om je heen.  ")
    printsleep(0.5, "Je ziet een ladder die zo hoog rijkt als je kunt zien. ")
    printsleep(0.5, "Je ziet een grot, een donkere grot zonder enige manier om iets te zien ")
    printsleep(0.5, "Je ziet een rivier, met een klein roeibootje ter grootte van één persoon. Zonder peddels  ")
    printsleep(3,"" )
    print("welke richting wil je op?  ")
    print()
    print("A: de ladder")
    print("B: de grot")
    print("C: de rivier")
    print()
    keuze1 = input("kies, A, B of C  ")
    if keuze1 == 'A':
        print("je klimt omhoog, je klimt, en je klimt, en je klimt. Je denkt dat er geen einde aan gaat komen, en dat klopt. Je klimt tot dat je je armen niet meer omhoog kan Strekken om de volgende treden vast te grijpen. je valt tot je dood. ")
    elif keuze1 == 'B':
        printsleep(2,"je sluipt naar binnen, bang voor wat er misschien schuilt in de grot.")
        print("Je beweegt jezelf verder door de grot, met je handen tegen de wand hopend niet tegen een een muur aan te botsen.")
        print("Na een korte tien minuten van lopen kom je in een  dilemma terecht.")
        printsleep(2,"Het pad splits zich in tweeën, links helemaal donker, maar aan de rechter kant schijnt er in de verte een lichtje.  ")
        print("welke richting wil je op?")
        printsleep(1,"A: links")
        print("B: rechts")
        print()
        keuze2 = input("kies A of B  ")
        if keuze2 == 'A':
            print()
            printsleep(1,"doodlopend , je sterft aan verhongering")
        elif keuze2 == 'B':
            print()
            printsleep(1,"het licht blijkt een reusachtige vuurvlieg te zijn en jij bent zijn volgende maal")

    elif keuze1 == 'C':
        print()
        printsleep(2,"je stapt in het roerbootje, in volle hoop tot verlossing. ")
        print("Het gaat goed tot je aankomt bij een afgrond, omdat je geen peddels hebt kun je  ")
        print("Niet Weg varen, er is niks aan te doen, je valt naar beneden. Gelukkig land je in een meer en overleef je. ")
        printsleep(1, "Vervolgens loop je door de dichte bossen met blauwe bomen en paarse planten ")
        print("Je duwt een plant opzij en voelt een steek, uit angst sprint je door en beland je in een open stuk bos")
        print("Je kijkt naar je wond en vind uit dat het ontstoken is. Er zijn twee opties. Je smeert een van de omringende planten over de wond in hoop dat het heelt")
        print("Je smeert een van de omringende planten over de wond in hoop dat het heelt Of je doet er niks aan en hoopt te overleven ")
        printsleep(3, "welke keuze maak je?")
        printsleep(2, "A: je smeert de plant over de wond ")
        print("B: je doet er niks aan")
        keuze3 = input("kies A of B  ")
        if keuze3 == 'B':
            print("je overleeft de onsteking niet.")
        elif keuze3 == 'A':
            print("wil je een ronde of een vierkante plant over de wond heen smeren?  ")
            print("A: ronde plant")
            print("B: vierkante plant")
            keuze4 = input("kies A of B  ")
            if keuze4 == 'A': 
                print("de plant blijkt niet te werken, je sterft aan de ontsteking")
            elif keuze4 == 'B':
                print("de plant blijkt te werken en je de ontsteking heelt.")      
                print("Je loopt verder door het bos, het wordt laat en je hebt eten nodig om te overleven ")
                print("wil je jagen op landdieren of op waterdieren?")
                print()
                print("A: jagen op waterdieren") 
                print("B: jagen op landdieren")
                keuze5 = input("kies A of B  ")
                if keuze5 == 'A':
                    print("Het water blijkt giftig te zijn, je sterft")
                elif keuze5 == 'B':
                    print("Je vangt hazen, en hebt genoeg voedsel voor de komende dagen ")
                    print("na een tijdje wordt het donker en je moet een keuze maken...")
                    print("A: maak een vuurtje")
                    print("B: maak geen vuurtje")
                    keuze6 = input ("kies of je een vuurtje wilt maken of niet.  ")

                    if keuze6 == 'B':
                        print("je sterft aan een aanval van dieren")
                    elif keuze6 == 'A':
                        print("het vuurtje houdt dieren op afstand en je overleeft de avond")
                        printsleep(1, "Het wordt laat en donker, je hebt een slaapplek nodig ")
                        print("wil je een tent op de grond of een hut hoog in de bomen maken?")
                        print("A: tent op de grond")
                        print("B: hut in de bomen")
                        keuze7 = input("kies A of B  ")
                        if keuze7 == 'A': 
                            print("je wordt aangevallen in de nacht, je overleeft het niet") 
                        elif keuze7 == 'B':
                            print("de dieren kunnen je niet bereiken en je overleeft de nacht")

                            printsleep(2,"De volgende ochtend bereik je het einde van het bos, je komt aan bij een groot weiland, met een reusachtig, maar helemaal lege snelweg.")
                            printsleep(3,"Met maar één stilstaand busje aan de zijkant van de weg, je loopt ernaartoe.") 
                            print("kies of je met de man mee wilt of niet.")
                            printsleep(2, "A: je gaat mee")
                            print("B: je blijft op jezelf ")
                            keuze8 = input ("kies A of B. ")
                            if keuze8 == 'A':
                                print("je botst zo hard dat het je wakker maakt, het blijkt allemaal een droom geweest te zijn. je hebt gewonnen! ")
                            elif keuze8 == 'B':
                                print("wil je langs de snelweg lopen of het weiland in?")
                                printsleep(2, "A: het weiland in")
                                print("B: langs de snelweg lopen")
                                keuze9 = input("kies A of B  ") 
                                if keuze9 == 'B':
                                    print("Na 3 dagen lopen word je aan ge reden door het busje waar je eerder langs liep. ")
                                elif keuze9 == 'A':
                                    print("Je vindt een metalen plaat op de grond, met een sleutelgat in het midden ")
                                    print("A: zoek voor een sleutel in het weiland")
                                    print("B: pleeg zelfmoord")
                                    keuze10 = input ("kies A of B  ")
                                    if keuze10 == 'B':
                                        print("het blijkt allemaal een droom te zijn, je hebt gewonnen!")
                                    elif keuze10 == 'A':
                                        print("Je vindt de sleutel en opent de ingang")
                                        printsleep(2, "Je loopt naar binnen en komt aan bij een grootte kamer, met een portaal in het midden ")
                                        printsleep(2, "Er is een rode en groene knop ")
                                        printsleep(2, "A: druk de rode knop in")
                                        print("B: druk de groene knop in")
                                        keuze11 = input ("kies A of B  ")
                                        if keuze11 == 'A':
                                            print("Je wordt in het portaal gezogen en wordt wakker, het blijkt allemaal een droom te zijn")
                                            printsleep(2, "Maar je hebt de verkeerde knop ingedrukt en bent alles van de echte wereld vergeten")
                                            printsleep(2, "Je weet niet meer wie je bent of wat er gebeurd is.")
                                        elif keuze11 == 'B':
                                            print("Je wordt in het portaal gezogen en wordt wakker, het blijkt allemaal een droom te zijn. ")
                                            printsleep(2, "A: stap me je rechterbeen uit bed")
                                            print("stap me je linkerbeen uit bed")
                                            keuze12 = input("kies A of B  ")
                                            if keuze12 == 'A':
                                                print("je stapt met je goeie been uit bed en leeft nog een lang en gelukkig leven!")
                                            elif keuze12 == 'B':
                                                print("je stapt met je verkeerde been uit bed en wordt diezelfde middag nog aangereden onderweg naar school, je was zo dichtbij... probeer het nog eens!")







startgame = input ("wil je een spel spelen? ")

if startgame == 'nee' :
    print("jammer :(")
elif startgame == 'ja':
    intro()

