from joueur import*
from time import sleep

def printTexts(listeText):
    for e in listeText: 
        print('{:^100}'.format(e))
        sleep(0.5)
