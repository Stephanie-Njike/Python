
"""
def list_in_param(*params):
    return params[0]+params[1]+params[2]


value = list_in_param(1, 2, 3, 4, 5, 8)
print(value)

value2 = list_in_param('1', '2', '3', '4')
print(value2)

def list_in_param2(a, *params):
    return params[0]+params[1]+params[2]+a

value = list_in_param2(1, 2, 3, 4, 5, 8)
print(value)


def dico_in_param(**params):
    return params

print(dico_in_param(nom="Stephanie", prenom="olive"))


def maliste(listeParam):
    listeParam.append('moi')
    return listeParam

liste = [1, 2, 3]
print(maliste(liste))
"""

"""
def triangle(n):
    nombre_espace_gauche = n
    nombre_etoiles_milieu = 1
    nombre_espace_droit = n
    for i in range(n):
        for j in range (nombre_espace_gauche):
            print(' ', end = '')
        for k in range (nombre_etoiles_milieu):
            print('*', end = '')
        for l in range (nombre_espace_droit):
            print(' ', end = '')
        # print(' => ',i)
        print('')
        nombre_espace_gauche = nombre_espace_gauche - 1
        nombre_etoiles_milieu = nombre_etoiles_milieu + 2
        nombre_espace_droit = nombre_espace_droit - 1
    return " "
print(triangle(n = int(input("saisir la hauteur du triangle : "))))
"""

"""
def triangleNewMethod(n):
    espace = n
    nombreEtoile = 1
    for i in range(n):
        print(' '*espace, '*'*nombreEtoile, ' '*espace)
        espace = espace - 1
        nombreEtoile = nombreEtoile + 2
triangleNewMethod(n = int(input("saisir la hauteur du triangle : ")))
"""

"""
def maximum(nb1,nb2,nb3):
    max1 = nb1
    if nb1 > nb2 and nb1 > nb3:
        max1 = nb1
    if nb3 > nb1 and nb3 > nb2:
        max1 = nb3
    else:
        max1 = nb2
    return max1
print(maximum(nb1 = int(input("saisir le premier nombre : ")),
nb2 = int(input("saisir le deuxieme nombre : ")),
nb3 = int(input("saisir le troisieme nombre : "))))
"""
"""
def triangleAvecChiffres(n):
    espace = n
    nombreEtoile = 2
    valeurAAfficher = 1
    for i in range(n):
        if valeurAAfficher < n:
            print(' '*espace, str(valeurAAfficher)*nombreEtoile, ' '*espace)
            espace = espace - 1
            nombreEtoile = nombreEtoile + 2
            valeurAAfficher = valeurAAfficher + 1
triangleAvecChiffres(n = int(input("saisir la hauteur du triangle : ")))
"""
"""
def triangleNewMethod(n):
    espace = n
    nombreEtoile = 2
    for i in range(1, n):
        print(' '*espace, str(i)*nombreEtoile, ' '*espace)
        espace = espace - 1
        nombreEtoile = nombreEtoile + 2
triangleNewMethod(n = int(input("saisir la hauteur du triangle : ")))
"""
"""
def chiffre_porte_bonheur (nb):
    nouveau = nb
    while nouveau >= 10:
        resultat = str(nouveau)
        somme = 0
        for i in range(len(resultat)):
            chiffre = int(resultat[i])
            print(chiffre,"**2 = ",chiffre**2)
            somme = somme + chiffre**2
        nouveau = somme
    if nouveau == 1:
        print("le chiffre ", nb, " est un chiffre porte bonheur")
    else:
        print ("le chiffre ", nb, " n'est pas un chiffre porte bonheur")
print(chiffre_porte_bonheur (nb = int(input("saisir le nombre : "))))
"""
"""
def compte_mot(phrase):
    liste_mot = phrase.split(':')
    print(liste_mot)
    nombre_mot = len(liste_mot)
    return nombre_mot

print(compte_mot('Bonjour:toi:et:moi:aussi'))
"""

"""
def NbCMin(passe):
    liste = [i.islower() for i in passe]
    print(liste)
    return sum(liste)
"""

"""
def NbCMin(passe):
    som = 0
    for i in passe:
        if i.islower():
           som = som + 1
    return som
print(NbCMin('paREDsse'))
"""
"""
def longMaj(passe):
    longMajMax = 0
    longTmp = 0
    for i in passe:
        if i.isupper():
            longTmp = longTmp + 1
        else:
            longTmp = 0
        if longTmp > longMajMax:
            longMajMax = longTmp
    return longMajMax
            
print(longMaj('ERRRiiuooiiAAfgghrrhhhDDDDR'))
"""

def premier_nb(borninf,bornsup):

    for nbr1 in range(borninf,bornsup):
        nbrpre = 1
        for div1 in range(2,nbr1):
           if nbr1 % div1 == 0:  
              nbrpre = 0
        if nbrpre == 1:
            print("Le nombre - ",nbr1, " - est premier" )
        
    return nbr1

premier_nb(1,100)
        
