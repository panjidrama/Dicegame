"""" Ce programme simule le tirage de trois dés à 6 faces aux valeurs non canoniques. Pour chaque dé à une valeur inférieure, le joueur gagne 1 point. Pour chaque dé à valeur supérieure, il perd un point. 

""""
#Dicegame1
print ('Games ?')
nb_games = input()
print ('Rounds/game ?')
nb_round = input()

    a_victorys = 0
    b_victorys = 0
    c_victorys = 0

j = 0
    while j > nb-games:




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
while i < nb_rounds:

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

""""print ('–––––––––––––––––Résultats finaux––––––––––––––––––––')
print (a)
print (b)
print (c)""""

    if a < b and a < c:
        a_victorys = a + 1
    if b>c and b>a:
        b_victorys = b + 1
    if c>b and c>a:
        c_victorys = c + 1
        
        j = j + 1
print ('_________________________')        
print (a_victorys)
print (b_victorys)
print (c_victorys)
