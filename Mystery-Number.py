#Bibliothèques
from random import randrange

#Variables
inf=int(input("nombre minimum de l'intervalle:"))
sup=int(input("nombre maximum de l'intervalle:"))
util=0
a=0
hsrd=randrange(inf, sup)
utili=eval(input('Choisis une difficulté entre 2 et 4: '))

#Boucle de jeu
while hsrd!=util:
    util=eval(input('Choisis un nombre !'))
    if util>hsrd:
        print('Plus petit !')
    elif util<hsrd:
        print('Plus grand !')
    a=a+1
    dif=utili
    if a==dif:
        print("Perdu")
        break
    if util==hsrd:
        print('Bravo !')