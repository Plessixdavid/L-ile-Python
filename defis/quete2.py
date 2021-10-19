from random import*

from time import *
import os
import json
from options.joueur import player

def quete2():
    disquete2 = (
                "Au nord de la plage, tu trouves un petit temple taillé\n",
                "dans la paroi rocheuse. Au-dessus de l’arche d’entrée,\n",
                " est écrit un message dans une langue apparemment inconnue mais\n",
                " utilisant l’alphabet habituel.\n\n",

                "Sur les colonnes de l’arche, sont d’ailleurs gravées en relief\n",
                "toutes les lettres de l’alphabet. Curieux, tu appuies au hasard\n",
                "sur l’une des lettres et tu t’aperçois que les lettres formant le\n",
                "message changent. Malgré cela, le message en lui-même reste \n",
                "incompréhensible.\n\n",
                "En effectuant plusieurs tests, tu te rends compte qu’a une lettre\n",
                "définie correspond une composition spécifique du message. Ne voyant\n",
                "pas trop quoi faire d’autre pour le moment, tu décides d’entrer dans\n",
                "le temple.\n\n",
                "À l’intérieur, tout le sol est recouvert de sable. Au milieu de la petite\n",
                "pièce, se trouve un autel avec une niche fermée par une grille apparemment\n",
                "sans serrure.\n\n",
                "À l’intérieur de la niche tu vois une grosse clé en argent (inatteignable\n",
                "tant que la grille est en place).\n" ,
                "À côté de la niche, un écriteau en bois indique :\n\n", 
                "« Récite le crédo du Python, puis trace ton nom secret ».")

    os.system('cls') 
    for e in disquete2:
        print('{:^100}'.format(e))
        sleep(0.5)



    alpha_b = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]

    for x in range(len(alpha_b)):
        alpha_b.append(alpha_b[x])

    message= input("entrez votre message:\n")
    clef= randint(0,26)
    os.system('cls')
    def chiffrage_lettre(lettre, alpha_b, clef):
        for i in range(len(alpha_b)):
            if lettre == " ":
                return " "
            elif alpha_b[i] == lettre:
                return str(alpha_b[i+clef])
        return "?"


    message_chiffré = str()

    for lettre in message:
        message_chiffré += chiffrage_lettre(lettre, alpha_b, clef)
        

    print(message_chiffré)

    messagedeux= input("entrez votre message:\n")
    bclef= int(input("entrez une clef de décalage svp:\n"))

    alpha_c = ["z","y","x","w","v","u","t","s","r","q","p","o","n","m","l","k","j","i","h","g","f","e","d","c","b","a"]

    for x in range(len(alpha_c)):
        alpha_c.append(alpha_c[x])



    def dechiffrage_lettre(lettre, alpha_c, bclef):
        for i in range(len(alpha_c)):
            if lettre == " ":
                return " "
            elif alpha_c[i] == lettre:
                return str(alpha_c[i+bclef])
        return "?"


    message_chiffrédeux = str()

    for lettre in messagedeux:
        message_chiffrédeux += dechiffrage_lettre(lettre, alpha_c, bclef)
        if message_chiffrédeux != player["names"]:
            break
        else:
            print(f"bien joué {message_chiffrédeux}")

    disquete2_1= (f"Bien joué, tu as réussi l'epreuve,\n",
                 "tu entend un lourd mecanisme grincer et la grille se soulève sous tes yeux.\n" ,
                 "tu recois la cléf d'argent.\n\n",
                 "Courage encore quelques effort et tu retrouveras tes amis.")
    
    for e in disquete2_1:
        print('{:^100}'.format(e))
        sleep(0.5)
    
    

    player["cléf argent"] = "ok"
    with open('joueur.json', 'w', encoding='utf-8') as f:
        json.dump(player, f, ensure_ascii=False, indent=4)
        

if __name__ == "__main__":
    quete2()