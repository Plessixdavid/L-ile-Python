from joueur import *
import random
random.randint(0, 21)
from time import *
import os

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
            if x == joueur["x"] and y == joueur['y']:
                row+= "⬛"
            elif element == 7:
                row+="⬛"
            elif element == 5:
                row+="🟥"  
            elif element == 0:
                row+="🟫"
            elif element == 3:
                row+="🟨"
            elif element == 4 :
                row+="📜"
            elif element == 2:
                row+="⬜"
            
            else:
                row+="0"
        print(row)

    
    disquete1 = (f"En haut de la falaise, en bordure de forêt et pas très loin de la plage,",
                "tu découvres la statue d’un Sphinx avec une grosse clé en bronze posée sur les pattes.\n\n",
                "Lorsque tu t’en approches, les yeux de la statue s’illuminent et une voix se fait entendre :",
                "« Bonjour explorateur! Pour ouvrir la porte de la montagne,",
                "atteindre le cœur de l’île et rejoindre tes compagnons.\n\n",
                "tu devras tout d’abord prouver ta valeur individuelle en gagnant les 3 clés",
                "que tu obtiendras en relevant les défis appropriés.\n\n",
                "Ceci est le premier d’entre eux. »",
                "Il est bien entendu impossible de prendre la clé tant que le défi n’est pas gagné.\n\n",
                "La voix poursuit :",
                "« 3 fois de suite, tu devras deviner le nombre que j’ai en tête.",
                "Tu as 20 essais maximum pour les trouver tous, es-tu prêt ? »")


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

    
    disquete1_2 = ("Felicitation explorateur, tu a gagné mon défis et je te confie la clef de bronze",
                    "N'oublie pas de la ranger dans ton sac.", 
                    "Maintenant, dirige toi vers le prochain défis mais gare à toi car l'île regeorge de danger.\n\n"
                    "Le sphinx disparu dans un epaix nuage aux senteurs inabituel de ... d'herbes de provence.  ")
    
    for e in disquete1_2: 
        print('{:^100}'.format(e))
        sleep(0.5)
    disquete1_3 = input("La cléf tombe sur le sol, voulez-vous la ramasser?\n\n"
                            "1 : oui. 2 : non.\n")
    print(disquete1_3)
    if disquete1_3 == 1:
        joueur["cléf bronze"] = "ok"
        print(f"vous avez pris la cléf de bronze .\n\n")
    else:
        joueur["cléf bronze"] = "ok"
        print("Vous êtes con ou quoi...Vous prenez la cléf quand même.\n\n")
    print()
    print()
     

if __name__ == "__main__":
    quete1()