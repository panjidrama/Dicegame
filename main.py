#Dicegame1
import random
#Dés
DA = [2, 2, 4, 4, 9, 9]
DB = [1, 1, 6, 6, 8, 8]
DC = [3, 3, 5, 6, 7, 7]

#Résultats
a=0
b=0
c=0

#Tirages
i = 0
while i < 100:

    TA = DA[random.randint(0, 5)]
    TB = DB[random.randint(0, 5)]
    TC = DC[random.randint(0, 5)]

#on peut choisir d'afficher chaque tirage en décommentant les lignes ci-dessous.
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

#    print ('Résultat provisoire A : ' + str(a))
#    print ('Résultat provisoire B : ' + str(b))
#    print ('Résultat provisoire C : ' + str(c))

    i =     i + 1

print ('–––––––––––––––––Résultats finaux––––––––––––––––––––')
print (a)
print (b)
print (c)
