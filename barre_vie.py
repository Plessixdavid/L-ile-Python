from random import *
from joueur import * 




nbr_singe = 9
singe_chance = randint(0,100) < 60
chef_chance = randint(0,100) <70
moi = randint(0,100)

joueurs = []

for loop in range(1,nbr_singe+1):
    joueurs.append(f"singe{loop}")

joueurs.append("chef")
joueurs.append(f'{joueur["nom"]}')

fizzbuzz = 0
while fizzbuzz <=101:
    for e in joueurs:
        print(joueurs)
        if e == "david":
            print(f"{e} prend son temps et lance.")
        if e == "chef":
            print(f"{e} prend son temps et lance.")
        if joueurs == []:
            break
        else:
            print(f"{e} prend son temps et lance.")
        print(joueurs)
        fizzbuzz+=1
        if randint(0,100) < 70:  
            if fizzbuzz % 3 == 0 and fizzbuzz % 5 == 0:
                print("fizzbuzz")
                continue
            elif fizzbuzz % 3 == 0:
                print("fizz")
                continue
            elif fizzbuzz % 5 == 0:
                print("buzz")
                continue
            print(fizzbuzz)
        else:
            joueurs.pop()
            print("boom")

