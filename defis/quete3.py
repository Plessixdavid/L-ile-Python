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
                row+= "???"
            elif element == 7:
                row+="???"
            elif element == 5:
                row+="????"  
            elif element == 4:
                row+="????"
            elif element == 3:
                row+="????"
            elif element == 0:
                row+="????"
            elif element == 0:
                row+="????"
            elif element == 2:
                row+="???"
            
            else:
                row+="0"
        print(row)


    sleep(3)
    disquete3 = ("En explorant la jungle, tu remarques une bande de singes braillards",
    "??voluant dans les arbres. En ??coutant avec un peu plus d???attention,",
    "tu te rends comptes que les singes semblent articuler des nombres et que deux sons",
    "reviennent r??guli??rement : Fizz et Buzz...\n",
    "?? un moment, les cris s???arr??tent et tu te retrouves subitement entour?? par les singes.",
    "L???un d???eux, probablement le chef vu sa d??marche assur??e, descend de l???arbre",
    "et s???approche de toi. Il te toise un instant puis, du doigt, te d??signe un endroit",
    "en hauteur. En levant la t??te, tu aper??ois une grosse cl?? en or, pendue ?? une solide",
    "liane, tu commences ?? chercher un moyen de grimper dans les arbres, mais cela",
    "d??clenche une vive r??action de la part des singes. Il semble qu???ils ne soient",
    "pas dispos??s ?? te donner la cl?? comme ??a !\n",
    "Tu te ravises alors, et le chef se rapproche de toi et commence ?? te parler...\n",
    "?? Toi jouer ! Si gagner alors cl?? ?? toi ! ??\n",
    "Jouer ? Mais ?? quoi ?\n",
    "Semblant lire dans tes pens??es, le chef dit alors ?? Nous montrer. ??",
    "Puis il dit ?? 1 ??.",
    "Un autre singe dans les arbres dit alors ?? 2 ??, puis un troisi??me ?? Fizz ??",
    "et ainsi de suite : ?? 4 ??, ?? Buzz ??, ?? Fizz ??, ?? 7 ??, ?? 8 ??, ?? Fizz ??, ?? Buzz ??,",
    "?? 11 ??, ?? 12 ??...\n",
    "?? ce moment, tous les autres singes se mettent ?? rire et celui",
    "qui vient d???annoncer 12 pousse un cri de d??ception et se retourne sur sa branche",
    "en boudant, puis le jeu recommence avec les singes restants : ?? 1 ??, ?? 2 ??,",
    "?? Fizz ??...\n",
    "Au bout de quelques tours tu comprends le principe du jeu et tu tentes ta chance\n",
    "pour obtenir la cl??.")

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
    playerwin = (f"un grand silence envahi la jungle, m??me les oiseaux stop leurs chants.",
                f"{player['names']} regarde autour de lui, inquiet. Le chef monte sur l arbre,",
                "la d??faite lui p??se sur les ??paules. Arriv?? ?? la moiti?? du chemin, le chef ",
                "se retourne et dit:",
                f"Que ferais tu si je ne te donnais pas la clef {player['names']}?\n",
                f"Prenant sont courage ?? deux mains {player['names']} lui r??pondi:",
                "Nous pourrions rejouer et je gagnerais encore!\n",
                "Le singe baissa les ??paules et d??crocha la clef tout en souflant:",
                "Prend et ne reviens jamais.\n",
                f"{player['names']} ramassa la cl??f et s ??loigna soulag?? d avoir gagn?? la clef d'or"
                )
    playerisfalse= False
    print(joueurs)
    fizzbuzz = 0
    while fizzbuzz <=3000 and len(joueurs)>= 1 and not playerisfalse:
        for k,v in joueurs.items():
            if len(joueurs) == 1:
                for e in playerwin:
                    print('{:^100}'.format(e))
                    player["cl??f or"] = "ok"
                    sleep(0.5)
                    with open('joueur.json', 'w', encoding='utf-8') as f:
                        json.dump(player, f, ensure_ascii=False, indent=4)
                
                fizzbuzz = 64646
                break
            if k == player['names']:
                print(f'{player["names"]} prend son temps et lance.')
            else:
                print(f"le {k} lance fi??rement:")
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
                    print(player['names'] + " a gagn?? !")
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