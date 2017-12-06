#!/usr/bin/python2.7
#-*- coding: utf-8 -*-

##Ce programme simule le lancé de trois dés à 6 faces. Chaque joueur choisit un dé en début de partie. On compare les scores et une pour chaque dé inférieur on marque un point, pour chaque dé supérieur on perd un point.

import random
## Choix des paramètres nombre de parties et nombre de round dans une partie.
print ('Combien de parties ?')
nb_games = input()

print ('Combien de rounds ?')
nb_tirages = input()

#GAMES
 #Nombre de victoire
av=0
bv=0
cv=0
j = 0
while j < int(nb_games):
    
    #Les dés ont des valeurs spécifiques
    DA = [2, 2, 4, 4, 9, 9]
    DB = [1, 1, 6, 6, 8, 8]
    DC = [3, 3, 5, 6, 7, 7]

    #Résultats
    a=0
    b=0
    c=0



    #Tirages
    i = 0
    while i < int(nb_tirages):

        TA = DA[random.randint(0, 5)]
        TB = DB[random.randint(0, 5)]
        TC = DC[random.randint(0, 5)]

    #    print ('Dé A : ' + str(TA))

    #    print ('Dé B : ' + str(TB))

    #    print ('Dé C : ' + str(TC))

        if TA > TB:
            a = a + 1
        if TA > TC:
            a = a + 1
        if TA < TB:
            a = a - 1
        if TA < TC:
            a = a - 1
        if TB > TA:
            b = b + 1
        if TB > TC:
            b = b + 1
        if TB < TA:
            b = b - 1
        if TB < TC:
            b = b - 1
        if TC > TA:
            c = c + 1
        if TC > TB:
            c = c + 1
        if TC < TA:
            c = c - 1
        if TC < TB:
            c = c - 1
##         print ('Résultat provisoire A : ' + str(a))
##         print ('Résultat provisoire B : ' + str(b))
##         print ('Résultat provisoire C : ' + str(c))

        i = i + 1

##    print ('–––––––––––––––––Résultats finaux––––––––––––––––––––')
##    print (a)
##    print (b)
##    print (c)


    if a>c and a>b:
        av = av + 1
    if b>a and b>c:
        bv = bv + 1
    if c>a and c>b:
        cv = cv + 1
    j = j + 1

print (str(av) + '|' + str(bv) + '|' + str(cv))
