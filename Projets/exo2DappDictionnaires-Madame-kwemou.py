 # Exercice 1 - Intéraction utilisateur et chaînes de caractères

 #Écrire un programme qui permet à l'utilisateur de saisir un prénom (ex: "Jean") et d'écrire "Bonjour Jean !".

salutation = 'Bonjour'
prenom = None
x = input ('Entrez un prenom : ')
print(x)
prenom = x
y = '!'

z = salutation  +' '+ x +' ' + y
print(z)

# Exercice 2 - Intéraction utilisateur et chaînes de caractères

#Écrire un programme qui demande à l'utilisateur son année de naissance et qui affiche son âge. L'année courante sera mise dans une variable.


anneeCourante = 2020
anneeDeNaissance = None
aN = int(input ( 'Entrer votre annee de naissance : '))
print(aN)
anneeDeNaissance = aN
monAge = anneeCourante - anneeDeNaissance
print(monAge)


# Exercice 3 - Manipulation des listes


#Soit la liste:

l = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

#A partir de L:

# 1 Ajouter la valeur 1 à chacun de ses éléments.
l2 = [i + 1 for i in l]
print(l2)

# 2 Ajouter la valeur 11 à la fin de la liste.
l.append(11)
print(l)

# 3 Ajouter les valeurs 12 et 13 à la fin de la liste.
l.append(12)
l.append(13)
print(l)

# 4 Afficher le premier élément, les deux premiers éléments, le dernier élément, les deux derniers éléments.
print(l[0])
 #ou
print(l[-10])

print(l[:2])

print(l[9])
 #ou
print(l[-1])

print(l[-2:])
 # 5  Construire la liste "paires" qui contient les nombres paires de L et la liste "impaire" qui contient les nombres "impaires" de L.
    -> boucle for et liste compréhension

lNbrePairs = []
lNbreImpairs = []
for i in l:
    if i % 2 == 0:
        lNbrePairs.append(i)
    else:
        lNbreImpairs.append(i)
print(lNbrePairs)
print(lNbreImpairs)
 
# 6 Ajouter la valeur 3.5 entre 3 et 4.
#l[4:4] = [3.5]
#print(l)
 #ou
l.insert(4,3.5)
print(l)

# 7 Supprimer la valeur 3.5.
l.remove(3.5)
print(l)

# 8 Inverser l'ordre des éléments de L.
l.reverse()
print(l)


# 9 Demander à l'utilisateur de fournir un nombre au hasard et dire si ce nombre est présent dans L

nombre = input('entrer un nombre au hasard : ')
valeur = int(nombre)
if valeur in l:
    print('True')
else:
    print('False')


#  Exercice 4 - Manipulation des dictionnaires

#Soit le dictionnaire :

d = {'nom': 'Dupuis', 'prenom': 'Jacque', 'age': 30}


# 1 Corriger l'erreur dans le prénom, la bonne valeur est 'Jacques'.

d['prenom'] = 'Jacques'
print(d)

# 2 Afficher la liste des clés du dictionnaire
list_of_keys = d.keys()
print(list_of_keys)
# 3 Afficher la liste des valeurs du dictionnaire.
list_of_values = d.values()  ### vous m aviez conseille de ne plus utiliser les termes prores au language. je ne sais si cette nommination pourra gener
print(list_of_values)
# 4 #Afficher la liste des paires clé/valeur du dictionnaire.
liste_of__keys_and_values = d.items()
print(liste_of__keys_and_values)
# 5 Ecrire la phrase "Jacques Dupuis a 30 ans"
a = 'a'
b = 'ans'
c = str(d['age'])
phrase = d['prenom'] + ' ' + d['nom'] + ' ' + a + ' ' + c + ' ' + b
print(phrase)


#  Exercice 5 - Structures conditionnelles et module string

#Demander à l'utilisateur de fournir un caractère au hasard et dire s'il s'agit :

#    D'une lettre minuscule,
#    D'une lettre majuscule,
#    D'un chiffre,
#    D'autre chose.

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

# Exercice 6 - Le jeux du + ou du -

"""L'ordinateur choisit un nombre au hasard entre 1 et 100 et l'utilisateur doit deviner ce nombre mystère en respectant la règle suivante :

    L'utilisateur propose un nombre.
    L'ordinateur lui dit s'il est trop petit ou trop grand.
    Et ainsi de suite tant que l'utilisateur n'a pas trouvé le nombre mystère.

Exemple
Devinez le nombre mystère ? 60
60 est trop petit !
Quel est le nombre ? 75
75 est trop grand !
Quel est le nombre ? 70
Félicitations, le nombre mystère est bien 70 !!!

Amélioration du programme :

v2) Ajouter une gestion d'erreur si l'utilisateur ne rentre pas un nombre entre 1 et 100 ou s'il rentre autre chose qu'un nombre.

v3) Indiquer à l'utilisateur en combien de coups il a trouvé le nombre mystère.
 """






