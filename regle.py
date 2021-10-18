from prez import *
from time import sleep

cls = lambda: print('\n'*100)
cls()

reg = [
"Le jeu doit permettre de :\n\n",
"• Demander le nom du joueur.\n",
"• Représenter en mode texte (console) la carte (résolution minimum 50x30,\n",
"la carte sera statique, c’est-à-dire qu'elle tient entièrement sur l'écran\n",
"sans défilement) qui t'as a été remise avec tous les éléments indiqués (eau,\n",
"plaine, arbres, rochers, les 4 endroits mystérieux, etc.).\n\n",
"• Représenter ton avatar sur cette carte.\n",
"• Déplacer l'avatar sur la carte selon 4 directions en respectant les obstacles.\n",
"• Gérer le contenu de son sac à dos (avec une capacité d'objets maximum).\n",
"• Gérer une liste d'objets à trouver sur la carte (avec possibilité de les placer\n",
"aléatoirement en début de partie), de pouvoir les ramasser (et les mettre dans le\n",
"sac à dos) ou les redéposer au sol.\n",
"• Gérer l'utilité de ces objets, certains seront utiles pour certaines actions\n",
"spécifiques, d'autres juste pour prendre de la place dans le sac à dos (ou peut-être\n",
"à utiliser pour les étapes/projets suivants).\n",
"• Gérer 3 niveaux vitaux (soif, faim et fatigue) de l'avatar sur une échelle de 0 à 100.\n",
"Si l'un des compteurs arrive à zéro, c'est cuit, la partie est perdue !\n\n",
"Les spécifications détaillées suivent.\n\n",
"À noter pour tout ce qui n’est pas explicitement détaillé (par exemple : comment\n",
"représenter visuellement un arbre, comment nourrir mon personnage, à quelle\n",
"fréquence/quelle quantité doit apparaitre la nourriture, etc.)\n",
"tu dois donner libre cours à ton imagination tout en restant crédible dans le scénario.\n"]

for e in reg:
    # print('{:^100}'.format(e))
    print(e.center(100))
    sleep(1)