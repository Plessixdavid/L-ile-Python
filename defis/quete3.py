from random import *
from time import *
import json 
from options.joueur import player


def quete3():
    map_mattrix = [
        [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0], 
        [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,7,7,7,7,7,7,7,0,0,0,0,0,0,0,0,7,7,7,7,7,0,7,7,7,0,7,7,7,7,7,0,0],
        [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,7,4,4,4,4,4,4,4,7,7,0,0,0,0,0,0,7,0,0,0,0,0,0,7,0,0,0,0,0,0,7,0,0], 
        [0,0,0,0,0,0,0,0,0,0,0,0,0,0,7,7,4,4,4,0,0,4,4,0,7,0,0,0,0,0,0,7,0,0,0,0,0,0,7,0,0,0,0,0,7,0,0,0],
        [0,0,0,0,0,0,0,0,0,0,0,0,0,7,4,4,4,4,0,0,0,0,0,0,0,7,0,0,0,0,0,7,7,7,7,7,0,0,7,0,0,0,0,7,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0,0,0,0,7,4,4,4,0,0,0,7,0,0,7,0,7,0,0,0,0,0,7,0,0,0,0,0,0,7,0,0,0,7,0,0,0,0,0], 
        [0,0,0,0,0,0,0,0,0,0,0,0,0,7,4,7,4,0,0,0,7,0,0,7,0,7,0,0,0,0,0,7,0,0,0,0,0,0,7,0,0,7,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0,0,0,0,7,4,7,4,0,7,0,0,0,0,0,0,0,7,0,0,0,0,7,0,0,0,0,0,7,7,7,0,7,7,7,7,7,0,0],
        [0,0,0,0,0,0,0,0,0,0,0,0,0,0,7,4,4,7,0,0,0,0,0,0,0,0,0,7,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0], 
        [0,0,0,0,0,0,0,0,7,7,7,0,0,0,0,7,4,7,0,0,0,0,7,7,0,0,0,7,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,7,4,4,4,7,0,0,0,0,7,0,7,7,7,7,0,0,7,7,7,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,7,4,4,4,4,4,7,0,0,0,7,7,0,0,0,0,0,0,0,7,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0], 
        [0,0,0,0,0,0,7,4,4,4,4,4,7,0,0,7,4,4,7,7,7,7,7,7,7,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,7,4,4,4,7,7,7,7,7,4,4,4,4,4,7,4,4,7,0,0,0,0,0,0,0,7,7,7,7,0,0,7,0,7,0,7,7,7,7,7,0,0],
        [0,0,0,0,0,0,0,7,4,4,4,4,4,4,4,4,4,4,7,4,4,7,4,4,7,0,0,0,0,0,0,7,0,0,0,7,0,7,0,7,0,0,0,0,0,7,0,0], 
        [0,0,0,0,0,0,0,0,7,7,7,7,7,4,4,4,4,4,4,7,4,4,7,4,4,7,0,0,0,0,0,7,0,0,0,7,0,7,0,7,0,0,0,0,7,0,0,0],
        [0,0,0,0,0,0,0,0,0,0,0,0,0,7,7,7,7,7,4,7,4,4,4,7,4,4,7,0,0,0,0,7,7,7,7,0,0,7,0,7,0,0,0,7,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0,0,0,7,4,4,4,4,4,7,4,4,4,4,7,4,4,7,0,0,0,0,7,0,0,0,7,0,7,0,7,0,0,7,0,0,0,0,0], 
        [0,0,0,0,0,0,0,0,0,0,0,0,7,4,4,4,4,4,7,4,4,4,7,4,4,7,0,0,0,0,0,7,0,0,0,7,0,7,0,7,0,7,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0,0,0,7,7,7,7,7,7,7,7,7,7,7,7,7,0,0,0,0,0,0,7,7,7,7,0,0,7,7,7,0,7,7,7,7,7,0,0],
        [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],

    ]

    for y in range(len(map_mattrix)):
        row = ""
        for x in range(len(map_mattrix[y])):
            element = map_mattrix[y][x]
            if x == player["x"] and y == player['y']:
                row+= "⬛"
            elif element == 7:
                row+="⬛"
            elif element == 5:
                row+="🟥"  
            elif element == 4:
                row+="🟫"
            elif element == 3:
                row+="🟨"
            elif element == 0:
                row+="📜"
            elif element == 0:
                row+="🟦"
            elif element == 2:
                row+="⬜"
            
            else:
                row+="0"
        print(row)


    sleep(3)
    disquete3 = ("En explorant la jungle, tu remarques une bande de singes braillards",
    "évoluant dans les arbres. En écoutant avec un peu plus d’attention,",
    "tu te rends comptes que les singes semblent articuler des nombres et que deux sons",
    "reviennent régulièrement : Fizz et Buzz...\n",
    "À un moment, les cris s’arrêtent et tu te retrouves subitement entouré par les singes.",
    "L’un d’eux, probablement le chef vu sa démarche assurée, descend de l’arbre",
    "et s’approche de toi. Il te toise un instant puis, du doigt, te désigne un endroit",
    "en hauteur. En levant la tête, tu aperçois une grosse clé en or, pendue à une solide",
    "liane, tu commences à chercher un moyen de grimper dans les arbres, mais cela",
    "déclenche une vive réaction de la part des singes. Il semble qu’ils ne soient",
    "pas disposés à te donner la clé comme ça !\n",
    "Tu te ravises alors, et le chef se rapproche de toi et commence à te parler...\n",
    "« Toi jouer ! Si gagner alors clé à toi ! »\n",
    "Jouer ? Mais à quoi ?\n",
    "Semblant lire dans tes pensées, le chef dit alors « Nous montrer. »",
    "Puis il dit « 1 ».",
    "Un autre singe dans les arbres dit alors « 2 », puis un troisième « Fizz »",
    "et ainsi de suite : « 4 », « Buzz », « Fizz », « 7 », « 8 », « Fizz », « Buzz »,",
    "« 11 », « 12 »...\n",
    "À ce moment, tous les autres singes se mettent à rire et celui",
    "qui vient d’annoncer 12 pousse un cri de déception et se retourne sur sa branche",
    "en boudant, puis le jeu recommence avec les singes restants : « 1 », « 2 »,",
    "« Fizz »...\n",
    "Au bout de quelques tours tu comprends le principe du jeu et tu tentes ta chance\n",
    "pour obtenir la clé.")

    for e in disquete3: 
        print('{:^100}'.format(e))
        sleep(0.5)

    joueurs = {
        "singe1" : randint(50,70),
        "singe2" : randint(50,70),
        "singe3" : randint(50,70),
        "singe4" : randint(50,70),
        "singe5" : randint(50,70),
        "singe6" : randint(50,70),
        "singe7" : randint(50,70),
        "singe8" : randint(50,70),
        "singe9" : randint(50,70),
        "chef" : randint(70,90),
        f"{player['names']}" : randint(70,100)
    }
    playerwin = (f"un grand silence envahi la jungle, même les oiseaux stop leurs chants.",
                f"{player['names']} regarde autour de lui, inquiet. Le chef monte sur l arbre,",
                "la défaite lui pèse sur les épaules. Arrivé à la moitié du chemin, le chef ",
                "se retourne et dit:",
                f"Que ferais tu si je ne te donnais pas la clef {player['names']}?\n",
                f"Prenant sont courage à deux mains {player['names']} lui répondi:",
                "Nous pourrions rejouer et je gagnerais encore!\n",
                "Le singe baissa les épaules et décrocha la clef tout en souflant:",
                "Prend et ne reviens jamais.\n",
                f"{player['names']} ramassa la cléf et s éloigna soulagé d avoir gagné la clef d'or"
                )
    playerisfalse= False
    print(joueurs)
    fizzbuzz = 0
    while fizzbuzz <=3000 and len(joueurs)>= 1 and not playerisfalse:
        for k,v in joueurs.items():
            if len(joueurs) == 1:
                for e in playerwin:
                    print('{:^100}'.format(e))
                    player["cléf or"] = "ok"
                    sleep(0.5)
                    with open('joueur.json', 'w', encoding='utf-8') as f:
                        json.dump(player, f, ensure_ascii=False, indent=4)
                
                fizzbuzz = 64646
                break
            if k == player['names']:
                print(f'{player["names"]} prend son temps et lance.')
            else:
                print(f"le {k} lance fièrement:")
            fizzbuzz+=1
            rnd_nb = randint(0,100)

            if rnd_nb <= v:
                if fizzbuzz % 3 == 0 and fizzbuzz % 5 == 0:
                    print("il fait fizzbuzz")
                    continue
                elif fizzbuzz % 3 == 0:
                    print("fizz")
                    continue
                elif fizzbuzz % 5 == 0:
                    print("buzz")
                    continue
                print(fizzbuzz)
            else:
                if player['names'] in joueurs and len(joueurs) <= 1:
                    print(player['names'] + " a gagné !")
                    break
                if k== player['names']:
                    playerisfalse = True
                    print("il rate et sort du jeu")
                    break

                joueurs = { k : v for k,v in joueurs.items() if v}
                print("loupe et sort du jeu.")
                del joueurs[k]
                fizzbuzz = 0
        

if __name__ == "__main__":
    quete3()