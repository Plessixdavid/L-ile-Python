from options.liste_def import printTexts
from defis.quete1 import quete1
from defis.quete2 import quete2
from defis.quete3 import quete3
from defis.porte import door
from divers.carte import carte
from divers.map1 import mappy1
from options.joueur import player

from inv import *
from time import *
import os
import json



mappy1()

def colquette():
    print(player["x"], player["y"])
    if player["y"] == 5 and player["x"] == 25:
        quete1()
    if player["y"] == 2 and player["x"] == 12:
        door()
    elif player["y"] == 16 and player["x"] == 17:
        quete2()
    elif player["y"] == 14 and player["x"] == 5:
        quete3()


if player['names'] == "":
    entrejeu = ("Ce matin, tu n'as pas été réveillé par les mouvements du navire.",
                "Ton dernier souvenir est de t’être endormi sur la  confortable couchette de ta cabine\n", 
                "à bord de l’Argo.", 
                "Mais par le bruit des vagues, la chaleur du soleil et le champ  des oiseaux",
                "Il semble que tu ne sois plus sur le bateau.", 
                "Tu es allongé sur une plage !",  
                "Tu te redresses doucement, et, un peu aveuglé par le soleil,",
                "Tu regardes autour de toi.",
                "D'un côté la mer… de l'autre  un paysage sauvage, en partie steppe, en partie jungle.", 
                "Assez loin, au-delà des arbres, tu penses apercevoir des  montagnes.\n",)


    printTexts(entrejeu)

    name = input("tu ne te souviens pas de ton nom bizarrement, alors choisis en un.\n"
            "comment te nomme tu?\n")

    player.update({"names": name})
    print(player)
    with open('joueur.json', 'w', encoding='utf-8') as f:
        json.dump(player, f, ensure_ascii=False, indent=4)


    os.system('cls')
    sacdcouv = ("Tu fais un rapide bilan de ta situation :",
                "outre les vêtements que tu as sur toi, tu trouves un sac à dos avec :\n",
                "• une bouteille vide en verre.\n",
                "• un petit couteau multifonctions de bonne facture.\n",
                "1 : prendre le sac.\n",
                "2 : ne pas prendre le sac ?\n\n")
    printTexts(sacdcouv)


    poid1 = int(input(f"Que voulez vous faire {name}?\n"))
    if poid1 == 1:
        print(f"vous avez pris le sac.\n\n")
        print(f" dans le sac, il y a {sac}")
        print()
    else:
        print("Vous n'avez pas pris le sac et un coup de vent l'emporte loin vers le large...\n\n")

    os.system('cls')
    decouvpc = ("Un peu plus loin, posée sur une pierre, se trouve une mallette contenant :\n",  
                "• ton ordinateur portable (oui, il y a du réseau sur cette île)\n",
                "• un système de recharge photovoltaïque.\n",
                "1 : prendre le pc et le systeme de recharge.\n",
                "2 : ne pas prendre le pc et le systeme de rechage.\n\n") 
    printTexts(decouvpc)

    poid=0

    poid1=int(input(f"Que voulez vous faire {name}?\n"))
    if poid1 == 1:
            player["Pc"] = "ok"
            player["recharge"] = "ok"
            print(f"vous avez pris le pc ainsi que le systeme de recharge et votre charge est à {poid} sur 10 point.\n\n")
    else:
            print("Vous n'avez pas pris le pc ainsi que le systeme de recharge, une noix de coco tombe dessus et detruit le tout...\n\n")
    os.system('cls')
    decouvcarte = (
        "Enfin, glissée à l'intérieur du couvercle de la mallette\n",
        "se trouve une carte grossière plastifiée.\n",
        "1 : voir la carte.\n",
        "2 : ranger la carte dans le sac \n\n")

    printTexts(decouvcarte)


    repcarte= int(input(f"Que voulez vous faire {name}?\n"))
    if repcarte == 1:
        player["mappy"] = "ok"
        print(f"vous avez pris la carte .\n\n")
    else:
        print("Vous n'avez pas pris la carte...\n\n")

    os.system('cls')

    
while True:
    carte()
    print(player)
    dis1 = int(input("Vous décidez de prendre la route et le chemin sera long.\n"
            "Alors , vous décidez que la plage serait le sud et les montage.. le nord.\n"
            "L'ouest sera à votre gauche et l'Est sera à votre droite."
            "Que voulez-vous faire?\n"
            "             8 : aller vers le nord.\n"
            "4 : aller vers l'Ouest. 6 : aller vers l'Est.\n"
            "             2 : aller vers le sud.\n" ))
    if player["fatigue"] == 0:
        dis2 = int(input("vous êtes fatigué, il serait temps de vous reposer... \n"
                    "1h de repos vous rend 25 point d'endurance et vous en avez 0.\n"
                    "1 : repos 1h. 2 : repos 2h.\n"
                    "3 : repos 3h. 4 : repos 4h.\n" ))
        if dis2 == 1:
            player["fatigue"] +=25
        if dis2 == 2:
            player["fatigue"] +=50
        if dis2 == 3:
            player["fatigue"] +=75
        if dis2 == 4:
            player["fatigue"] +=100
    if player["soif"] <=20:
        dis3 = int(input(f"vous avez soif, il serait temps de boire... \n"
                    "boire 1 fois vous rend 15 point d'hydratation et vous en avez {soif}.\n"
                    "1 : boire 1 fois. 2 : boire 2 fois.\n"
                    "3 : boire 3 fois. 4 : boire 4 fois.\n" ))
        if dis3 == 1:
            player["soif"] +=15
        if dis3 == 2:
            player["soif"] +=30
        if dis3 == 3:
            player["soif"] +=45
        if dis3 == 4:
            player["soif"] +=60
    if dis1 == 0:
        with open('joueur.json', 'w') as f:
            json.dump(player, f)
            print(f"vous avez Saugardeé votre position. \n\n")
            exit()
    if dis1 == 4:
        player["x"] -=1
        player["fatigue"] -=10
        print(f"vous avez fait 100m vers l'Ouest. \n\n")
        colquette()
    if dis1 == 6:
        player["x"] +=1
        player["fatigue"] -=10
        print(f"vous avez fait 100m vers l'Est. \n\n")
        colquette()
    if dis1 == 8:
        player["y"] -= 1
        player["fatigue"] -=10
        print("vous avez fait 100m vers le nord.\n\n")
        colquette()
    if dis1 == 2:
        player["y"] +=1
        player["fatigue"] -=10
        print(f"vous avez fait 100m vers le sud. \n\n")
        colquette()
    

    
    