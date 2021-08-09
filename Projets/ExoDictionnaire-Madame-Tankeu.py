import os

"""  Exercice 1 - Intéraction utilisateur et chaînes de caractères
Écrire un programme qui permet à l'utilisateur de saisir un prénom (ex: "Jean") et d'écrire
"Bonjour Jean !" """
'''a = input("veuillez entrer votre prenom : ")
print('bonjour',a, '!')'''

#  résultat: veuillez entrer votre prenom : 'Jean'



"""  Exercice 2 - Intéraction utilisateur et chaînes de caractères
Écrire un programme qui demande à l'utilisateur son année de naissance et qui
affiche son âge. L'année courante sera mise dans une variable """

from datetime import datetime
date = datetime.now()
print(date)
annee_courante = 2020
an = int(input('votre année de naissance: '))
age=int(annee_courante - an)
print(age)
# COMMENT RETOURNER L'ANNEE EN COURS (SANS LE MOIS NI LE JOUR) AVEC datetime?    




"""Exercice 3 - Manipulation des listes
Soit la liste:

?
1
>>> L = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]"""

L = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# A. Ajouter la valeur 1 à chaque elt

L1 = [i+1 for i in L]
print(L1)

# B. Ajouter la valeur 11 à la fin de la liste
L.append(11)
print(L)

# C. Ajouter les valeurs 12 et 13 à la fin de la liste.
L.append(12)
L.append(13)
print(L)

# D. Afficher le premier élément, les deux premiers éléments, le dernier élément,
#les deux derniers éléments
print(L[0])
print(L[:2])
print(L[-1])
print(L[-2:])

# E. Construire la liste "paires" qui contient les nombres paires de L et la liste
# "impaire" qui contient les nombres "impaires" de L.
#-> boucle for et liste compréhension

liste_paire = [i for i in L if i%2==0]
print(liste_paire)

liste_impaire = [i for i in L if i%2==1]
print(liste_impaire)

# F. Ajouter la valeur 3.5 entre 3 et 4
L.insert(4,3.5)
print(L)

# G. Supprimer la valeur 3.5
del L[4]
print(L)

# H. Inverser l'ordre des éléments de L
L.reverse()
print(L)

# I. Demander à l'utilisateur de fournir un nombre au hasard et dire si
#ce nombre est présent dans L
'''
a = int (input('entrer un nombre: '))
if a in L:
    print('true')
else:
    print('false')'''
    



'''Exercice 4 - Manipulation des dictionnaires
Soit le dictionnaire :''' # il y a une mauvaise reponse ici



d = {'nom': 'Dupuis', 'prenom': 'Jacque', 'age': 30}

# A. Corriger l'erreur dans le prénom, la bonne valeur est 'Jacques'
d['prenom'] = 'Jacques'
print(d)

# B. Afficher la liste des clés du dictionnaire
for clé in d.keys():
    print(clé)

print(d.keys())

# C. Afficher la liste des valeurs du dictionnaire.
for valeurs in d.values():
    print(valeurs)
    
print(d.values())

# D. Afficher la liste des paires clé/valeur du dictionnaire.
for clé, valeurs in d.items():
    print(clé, '=>', valeurs)

print(d.items())

liste_des_paires_clés_valeurs = d.items()
print(liste_des_paires_clés_valeurs)

# E. Ecrire la phrase "Jacques Dupuis a 30 ans"

# Mauvaise reponse

print("Jacques Dupuis a 30 ans")




""" Exercice 5 - Structures conditionnelles et module string
Demander à l'utilisateur de fournir un caractère au hasard et dire s'il s'agit :

D'une lettre minuscule,
D'une lettre majuscule,
D'un chiffre,
D'autre chose.
"""
a = (input('Veuillez entrer un caractère : '))
if a is a.lower():
    print('lerttre miniscule')
if a is a.upper():
    print('lettre majuscule')
if a is type(int()):
    print('chiffre')
else:
    print('autre chose')
# JE NE SAIT COMMENT ARRIVER AU BON RESULTAT

# Regardez ici
# Correction
"""
caract = input('Entrer un caractere : ')
print(caract)
if caract.isupper():
    print( 'C est une majuscule')
elif caract.islower():
    print( 'C est une minuscule')
elif int(caract)  or float(caract):
    print( 'C est un chiffre')
else:
    print( 'C est autre chose')
"""



# Nous allons corriger cet exercice ensemble (exercice 6)
"""
Exercice 6 - Le jeux du + ou du -
L'ordinateur choisit un nombre au hasard entre 1 et 100 et l'utilisateur doit deviner ce nombre mystère en respectant la règle suivante :

L'utilisateur propose un nombre.
L'ordinateur lui dit s'il est trop petit ou trop grand.
Et ainsi de suite tant que l'utilisateur n'a pas trouvé le nombre mystère.
"""
a = 50
n = int(input('Dévinez le nombre mystère ? '))

    
if n < a:
    print(n, 'est trop petit')
if n > a:
    print(n, 'est trop grand')    
if n == a:
    print('Félicitations! le nombre mystère est bien', a, '!!!')
# COMMENT FAIRE REPETER LA QUESTION EN CAS DE MAUVAISE REPONSE?
# POUR LE RESTE JE SAIS PAS COMMENT PROCEDER         
          


os.system ("pause")

