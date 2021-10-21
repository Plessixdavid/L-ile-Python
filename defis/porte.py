from divers.anima_porte import *
from time import *
import os
import sys
import json
from liste_def import printTexts
from options.joueur import *

with open('joueur.json', 'r', encoding='utf-8') as f:
    joueur = json.load(f)

def door():
    frame5()

    disdoor = ("Tout au nord de la zone, à côté d’une magnifique cascade descendant de la montagne,",
            "tu remarques une grotte.\n",
            "Intrigué, tu y pénètres mais l’intérieur est très sombre.",
            "Heureusement, une torche et un silex pour l’allumer se trouvent sur une pierre près de l’entrée.",
            "Tu allumes donc la torche et tu t’enfonces dans la grotte. Au bout de quelques minutes,",
            "tu trouves une grosse porte en bois qui bloque le passage.\n"
            "Au milieu de cette porte, trois grosses serrures qui semblent refléter les couleurs de 3 métaux",
            "précieux : bronze, argent et or.")


    printTexts(disdoor)

    for k in joueur.keys():
        if "cléf or" in joueur:
            print(f"{joueur['names']}  mets la clef or dans sa sérrure.")
            sleep(1)
        if "cléf argent" in joueur:
            print(f"{joueur['names']}  mets la clef argent dans sa sérrure.")
            sleep(1)
        if "cléf bronze" in joueur:
            print(f"{joueur['names']}  mets la clef bronze dans sa sérrure.")
            sleep(1)
            frame1()
            frame2()
            frame3()
            break
        else:
            print(f"{joueur['names']} il te manque au moins une clef... revient quand tu l'auras.")
            frame4()
            break

    
