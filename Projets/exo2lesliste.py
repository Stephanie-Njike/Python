# Exo 1 :
#    - Donner une definition de liste en python
""" Une liste est une structure de donnees ou une variable contenant plusieurs elements.
    Ces elements pouvant aussi etre de types differents
"""

#    - Ecrire un programme informatique qui cree une liste vide et affiche son contenu.

"""
liste = []
print(type(liste)) 

Correction : print(liste)
"""

# Exo 2 :
# - Ecrire un programme python qui ajoute les valeurs : 3, 'a', 'b', 5 et 1
# puis le programe affiche le contenu de la liste

"""liste = []
liste.append(3)
liste.append('a')
liste.append('b')
liste.append(5)
liste.append(1)
print(liste)
"""

# Exo 3 :
# -la fonction reverse() nous permet de renverser les positions de chaque element de la liste.

#Ainsi le premier element sera en derniere position et le dernier, en premiere position

# -le programme cidessous aura le resultat suivant:

"""
Correction: Affichage
 -- ['Bonjour', 'Madame','le', 'Ministre']
 -- ['Ministre', 'le','Madame', 'Bonjour']
"""

# liste = ['Ministre', 'le','Madame', 'Bonjour']

"""liste = ['Bonjour', 'Madame', 'le', 'Ministre']
print(liste)
liste.reverse()
print(liste)
"""

# Exo 4 :
"""
les 2 premieres instructions seront eronees parce que :
 la liste declaree est d abord une liste vide, donc ne contient dejas aucun element.
 Et on ne peut pas changer la valeur d une position si dejas sa variable est vide
 la 3ieme instruction a une faute puisqu on ne sait ici quel type a elt . Pour
 qu elle soit bien ecrit, l on devrait mettre la double cote autour de l element 'elt'.
 De meme  l on devrait d abord ajouter les elements a la liste avant d affecter de nouvelle
 valeurs a certaines positions.
"""
"""liste = []
liste.append('elt')
liste.append('c')
liste.append('1')
liste[0] = 'a'
liste[1] = '1'
print(liste)
"""

# Exo 5 :
# ecrire un programme python qui prend la liste suivante [0, 1, 2, 3, 4, 1, 4, 3, 0, 1]
# Affiche la taille de cette liste
"""
liste = [0, 1, 2, 3, 4, 1, 4, 3, 0, 1]
print(len(liste))
"""
# Affiche le nombre d occurences de chaque element de la liste
"""
print(liste.count(0))
print(liste.count(1))
print(liste.count(2))
print(liste.count(3))
print(liste.count(4))
"""
#Trouver la position(index) de l element 3 dans la liste
#print(liste.index(3))
# trouver la difference entre les fonctions sort() et sorted() :
"""la fonction sort() trie directement les elements de la liste tandis que la fonction
 sorted() retourne d abord la liste principale avant de l ordonner ses element soit
 par order alphabetique, ou du plus petit au plus grand
"""

"""
Correction: 
liste.sort()
sorted(liste)
print(liste)
la fonction sort() trie uniquement les listes alors que 
la fonction sorted() trie n'importe quel objet iterable (liste, chaine de caractere, ...)
"""

# Exo 6 : Ecrire un programme python qui affiche tout les elements de la liste suivante
#['a', 'Hello',1,2,3,4,'T',10,20,'Oui', 'Moi', 'Toi', 'Bonjour Monsieur']
"""
liste = ['a', 'Hello',1,2,3,4,'T',10,20,'Oui', 'Moi', 'Toi', 'Bonjour Monsieur']
for i in liste:
    print(i)
"""

# Exo 7 : Ecrire un programme qui prend un nombre entier n au clavier et affiche
#une liste des puissance [n,n**2, n**4, ...].La taille de la liste est 5

"""
n = None
x = input('entrer n :')
n =int(x)

listeDesPuissances = []
listeDesPuissances.append(n)

for i in range(5):
    b = listeDesPuissances[i]**2
    listeDesPuissances.append(b)
print(listeDesPuissances)
"""

# Exo 8 : Donner le resultat d execution du code suivant( voir exo)

"""
1)
Affichage de la liste 1
[1, 2, 3, 4]
Affichage de la liste 2
[4,5,1,0]
Affiche de nouveau la liste 1
[1, 2, 3, 4,4,5,1,0]


 2)
 Affichage de la liste 1
[1, 2, 3, 4]
Affichage de la liste 2
[4,5,1,0]
Affichage de l adition de deux listes
[1, 2, 3, 4,4,5,1,0]

3)
Affichage de la liste 1
[1, 2, 3, 4,1, 2, 3, 4,1, 2, 3, 4,1, 2, 3, 4,1, 2, 3, 4]

"""

# Exo 9 : Donner la sortie ecran script python ci dessous (voir exo)
"""
[1, 2, 3, 4, 1, 2, 3, 4, 1, 2, 3, 4, 1, 2, 3, 4, 1, 2, 3, 4]
[1, 1, 1, 1, 1,]
Affichage des 2 premiers elements de la liste
[1, 2]
Affichage du dernier element de la liste
[4]
Affichage du 3ieme element de la liste en partant de la fin
[2]
Affichage des 3 derniers elements d une liste
[2, 3, 4]
"""



