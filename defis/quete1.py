import random
random.randint(0, 21)
from time import *
import os
import json
from options.joueur import player

def quete1():
    map_mattrix = [
        [2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2],
        [2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2], 
        [2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2],
        [2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,5,7,5,7,7,7,7,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2],
        [2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,7,1,5,1,5,1,1,1,7,7,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2], 
        [2,2,2,2,2,2,2,2,2,2,2,2,2,2,7,7,1,1,1,2,2,1,1,2,7,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2],
        [2,2,2,2,2,2,2,2,2,2,2,2,2,5,5,5,5,1,2,2,2,2,2,2,2,7,2,2,2,2,2,2,2,2,2,2,2,3,3,3,2,2,2,2,2,2,2,2],
        [2,2,2,2,2,2,2,2,2,2,2,2,2,7,1,1,1,2,2,2,2,2,2,2,2,7,2,2,2,2,2,2,2,2,2,2,3,3,2,3,3,2,2,2,2,2,2,2], 
        [2,2,2,2,2,2,2,2,2,2,2,2,2,5,5,5,1,2,2,2,7,2,2,7,2,7,2,2,2,2,2,2,2,2,2,3,3,2,2,2,3,3,2,2,2,2,2,2],
        [2,2,2,2,2,2,2,2,2,2,2,2,2,7,1,1,1,2,2,2,2,2,7,2,2,2,7,2,2,2,2,2,2,2,3,3,2,2,2,2,2,3,3,2,2,2,2,2],
        [2,2,2,2,2,2,2,2,2,2,2,2,5,5,5,5,1,2,2,2,2,2,2,7,2,2,2,7,2,2,2,2,2,2,2,2,2,2,2,2,2,3,3,2,2,2,2,2], 
        [2,2,2,2,2,2,2,2,2,2,2,7,1,1,1,1,1,2,2,2,7,2,2,2,2,2,2,7,2,2,2,2,2,2,2,2,2,2,2,2,2,3,3,2,2,2,2,2],
        [2,2,2,2,2,2,2,2,2,2,7,7,7,7,7,7,7,2,2,2,2,7,7,7,2,2,7,2,2,2,2,2,2,2,2,2,2,2,2,2,3,3,2,2,2,2,2,2],
        [2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,7,7,2,2,2,2,2,2,2,7,2,2,2,2,2,2,2,2,2,2,2,2,2,3,3,2,2,2,2,2,2,2], 
        [2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,7,4,4,7,7,7,7,7,7,7,2,2,2,2,2,2,2,2,2,2,2,2,2,3,3,2,2,2,2,2,2,2,2],
        [2,2,2,2,2,2,2,2,2,2,2,2,2,2,7,4,4,4,4,4,7,4,4,7,2,2,2,2,2,2,2,2,2,2,2,2,2,3,3,2,2,2,2,2,2,2,2,2],
        [2,2,2,2,2,2,2,2,2,2,2,2,2,7,4,4,4,4,7,4,4,7,4,4,7,2,2,2,2,2,2,2,2,2,2,2,2,3,3,2,2,2,2,2,2,2,2,2], 
        [2,2,2,2,2,2,2,2,2,2,2,2,7,4,4,4,4,4,4,7,4,4,7,4,4,7,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2],
        [2,2,2,2,2,2,2,2,2,2,2,2,2,7,7,7,7,7,4,7,4,4,4,7,4,4,7,2,2,2,2,2,2,2,2,2,2,3,3,2,2,2,2,2,2,2,2,2],
        [2,2,2,2,2,2,2,2,2,2,2,2,7,4,4,4,4,4,7,4,4,4,4,7,4,4,7,2,2,2,2,2,2,2,2,2,2,3,3,2,2,2,2,2,2,2,2,2], 
        [2,2,2,2,2,2,2,2,2,2,2,2,7,4,4,4,4,4,7,4,4,4,7,4,4,7,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2],
        [2,2,2,2,2,2,2,2,2,2,2,2,7,7,7,7,7,7,7,7,7,7,7,7,7,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2],
        [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],

    ]

    for y in range(len(map_mattrix)):
        row = ""
        for x in range(len(map_mattrix[y])):
            element = map_mattrix[y][x]
            if element == 7:
                row+="???"
            elif element == 5:
                row+="????"  
            elif element == 0:
                row+="????"
            elif element == 3:
                row+="????"
            elif element == 4 :
                row+="????"
            elif element == 2:
                row+="???"
            
            else:
                row+="0"
        print(row)

    
    disquete1 = (f"En haut de la falaise, en bordure de for??t et pas tr??s loin de la plage,",
                "tu d??couvres la statue d???un Sphinx avec une grosse cl?? en bronze pos??e sur les pattes.\n\n",
                "Lorsque tu t???en approches, les yeux de la statue s???illuminent et une voix se fait entendre :",
                "?? Bonjour explorateur! Pour ouvrir la porte de la montagne,",
                "atteindre le c??ur de l?????le et rejoindre tes compagnons.\n\n",
                "tu devras tout d???abord prouver ta valeur individuelle en gagnant les 3 cl??s",
                "que tu obtiendras en relevant les d??fis appropri??s.\n\n",
                "Ceci est le premier d???entre eux. ??",
                "Il est bien entendu impossible de prendre la cl?? tant que le d??fi n???est pas gagn??.\n\n",
                "La voix poursuit :",
                "?? 3 fois de suite, tu devras deviner le nombre que j???ai en t??te.",
                "Tu as 20 essais maximum pour les trouver tous, es-tu pr??t ? ??")


    for e in disquete1: 
        print('{:^100}'.format(e))
        sleep(0.5)

    os.system('cls')
    reset = False

    for loop in range(1,4):
        nbralea = random.randint(0,100)
        repquete= -1
        essais = 1
        if reset == True:
            break
        while repquete != nbralea:
            repquete = int(input("entre un nombre.\n"))
            essais += 1
            if essais >= 20:
                reset = True
                print(f"fin de parti, recommence.")
                break
            if repquete < nbralea:
                print(" ton nombre est trop petit.")
                
            elif repquete > nbralea:
                print("ton nombre est trop grand.")
            else:
                print("bravo")
        print(f"fin de la partie {loop}")

    
    disquete1_2 = ("Felicitation explorateur, tu a gagn?? mon d??fis et je te confie la clef de bronze",
                    "N'oublie pas de la ranger dans ton sac.", 
                    "Maintenant, dirige toi vers le prochain d??fis mais gare ?? toi car l'??le regeorge de danger.\n\n"
                    "Le sphinx disparu dans un epaix nuage aux senteurs inabituel de ... d'herbes de provence.  ")
    
    for e in disquete1_2: 
        print('{:^100}'.format(e))
        sleep(0.5)
    disquete1_3 = input("La cl??f tombe sur le sol, voulez-vous la ramasser?\n\n"
                            "1 : oui. 2 : non.\n")
    print(disquete1_3)
    if disquete1_3 == 1:
        player["cl??f bronze"] = "ok"
        print(f"vous avez pris la cl??f de bronze .\n\n")
    else:
        player["cl??f bronze"] = "ok"
        print("Vous ??tes con ou quoi...Vous prenez la cl??f quand m??me.\n\n")
    print()
    print()
     

with open('joueur.json', 'w') as f:
	json.dump(player, f)

if __name__ == "__main__":
    quete1()