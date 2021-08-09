import os
"""
             EXERCICE 1
     
1) Définition de liste en python:
une liste est un type de variable dans lequel on insert des éléments qui peuvent
être tout autre type de variables et même encore une liste

Correction: Une liste est une structure de donnees dans laquelle on ranger plusieurs 
donnees ou valeurs de differents types

2) Ecrire un programme informatique qui crée une liste vide et affiche
son contenu;
"""
liste = []
print(liste) #ou
liste = list()
print(liste)

"""          EXERCICE 2

Ecrire un programme python qui ajoute les valeurs : 3, ‘a’, ‘b’, 5 et 1 dans
une liste. Puis, le programme affiche le contenu de la liste """

liste = []
liste.append(3)
liste.append('a')
liste.append('b')
liste.append(5)
liste.append(1)

print(liste)
# comment insérer plusieurs valeurs à la fois sans passer par plusieurs 'append'?

"""
          Exercice 3:

Soit le programme Python ci-dessous: """

liste = ['bonjour', 'Madame', 'le', 'Ministre']
print(liste)
liste.reverse()
print(liste)

"""1) A quoi sert la fonction reverse() appliquée à une liste?
reverse() permet de d'inverser les éléments contenus dans la liste


2) Quel est le résultat du programme ci-dessus ?
le résultat présentera les éléménts du dernier au premier

Correction: Le resultat est le suivant:
['bonjour', 'Madame', 'le', 'Ministre']
['Ministre', 'le', 'Madame', 'bonjour']

          Exercice 4 :

Soit la variable"""
liste = []

#liste[0] = (‘a’)
#liste[1] = 1
liste = []
#liste.append(elt)
liste.append('c')
liste.append(1)
print(liste)

"""
Trouvez les instructions erronées et expliquez pourquoi elles sont erronées.

- liste[0] = 'a': est la syntaxe pour modifier l'élément à la position 0 par 'a'.or la
liste est vide. Donc ici il est question d'ajouter des éléments à la liste
- liste[1] = la raison est la même que la première
- liste.append(elt): ici le type de variable de l'élément n'est pas spécifié
python ne le connait pas et ne peut présenter un résultat

"""

"""         Exercice 5

Ecrire un programme python qui prend la liste suivante : [0, 1, 2, 3, 4, 1, 4, 3, 0, 1]

1) Affiche la taille de cette liste;
la taille de la liste est un nombre ou chiffre qui défini le nombre d'élément de liste
pour celà , on utilise la fonction len()"""

liste = [0, 1, 2, 3, 4, 1, 4, 3, 0, 1]
print("la taille de la liste est: ",len(liste))


#2) Affiche le nombre d’occurences de chaque élément de la liste; 

liste = [0, 1, 2, 3, 4, 1, 4, 3, 0, 1]
compte = {}.fromkeys(set(liste),0)
for valeur in liste:
    compte[valeur] += 1
print(compte)
   #ou
liste = [0, 1, 2, 3, 4, 1, 4, 3, 0, 1]
occurence = dict([(i, liste.count(i))for i in set(liste)])
print(occurence)



#3) Trouver la position de l’élément 3 dans la liste
''' la fonction ma_variable.index permet de retourner la position d'un élément de la liste'''
liste = [0, 1, 2, 3, 4, 1, 4, 3, 0, 1]
position = liste.index(3)
print(position) # comment retourner les positions d'un élément qui revient plusieurs fois???

liste = [0, 1, 2, 3, 4, 1, 4, 3, 0, 1]


#4)Trier la liste par ordre croissant (utiliser la fonction sort() ou sorted())

liste = [0, 1, 2, 3, 4, 1, 4, 3, 0, 1]
print(sorted(liste))


#5)Quelle est la différence entre la fonction sort() et la fonction sorted() ?
""" - sorted() est une fonction builtin. Elle fait le tri mais ne modifie pas la liste
d'origine
    - sort() fait le même tri mais modifie la liste d'origine
   Correction: De plus, sort() trie uniquement les listes alors que sorted() trie tout objet iterable
"""
"""      Exercice 6

Ecrire un programme python qui affiche tous les éléments de la liste suivante :
[‘a’, ‘Hello’, 1, 2, 3, 4, ‘T’, 10, 20, ‘Oui’, ‘Moi’, ‘Toi’, ‘Bonjour Monsieur’]"""

liste = []
liste.extend(['a', 'Hello', 1, 2, 3, 4, 'T', 10, 20, 'Oui','Moi', 'Toi', 'Bonjour Monsieur'])
print(liste)  #ou


liste = []
print(liste)
liste +=['a','Hello', 1, 2, 3, 4, 'T', 10, 20, 'Oui','Moi', 'Toi', 'Bonjour Monsieur']
print(liste)

"""
Correction: 

for i in liste:
	print(i)
"""




"""
    Exercice 7

Ecrire un programme qui prend un nombre entier n au clavier et affiche une liste des
puissances comme suit : [n, n2, n4, n8, n16, …]. La taille de la liste à afficher est
de 5. """

'''n = int(input('entrer la valeur de n :'))
listeDePuissance = []
listeDePuissance.append(n)
for i in range(5):
    valeurAAjouter = listeDePuissance[i]**2
    listeDePuissance.append(valeurAAjouter)
print(listeDePuissance)'''

'''   Exercice 8

1) Donnez le résultat d’exécution du code suivant:'''

liste1 = [1, 2, 3, 4]
print('affichage de la liste1')
print(liste1)
liste2 = [4, 5, 1, 0]
print('affichage de la liste2')
print(liste2)
liste1.extend(liste2)
print('affiche de nouveau le liste1')
print(liste1)

''' 2. Donnez le résultat de l’exécution du program suivant:'''

liste1 = [1, 2, 3, 4]
print('affichage de la liste 1')
print(liste1)
liste2 = [4, 5, 1, 0]
print('affichage de la liste 2')
print(liste2)
print("affiche de nouveau de l'addition des deux listes")
print(liste1 + liste2)

'''  3. Que fait le programme ci-dessous ? Donnez le résultat de son exécution'''

liste1 = [1, 2, 3, 4]
print('affichage de la liste 1')
print(liste1*5)
'''ma_variable*5 permet de repéter les variables séquentiellement 5 fois '''

'''  Exercice 9

Donnez la sortie écran du script python ci-dessous'''
liste1 = [1, 2, 3, 4]
print(liste1*5)
print(liste1[0]*5)
print('affichage des deux premiers éléments de la liste ')
print(liste[:2])
print('affichage du dernier élément de la liste')
print(liste[-1])
print('affichage du troisième élément de la liste en partant de la fin')
print(liste[-3])
print('affichage des 3 derniers éléments d\'une la liste: ')
print(liste[-3:])

"""
Correction:

Bien vouloir faire les exercices 8 et 9
"""



os.system("pause")
