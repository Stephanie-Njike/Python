myList = []

# Ajouter un element dans la myList
myList.append('bonjour')

print(myList)

myList.append(45)

print(myList)

# Modifier le contenu de la liste

myList[1] = 'Madame'

print(myList)

# Inverser les valeurs d'une liste

myList.append('le')

myList.append('Ministre')

print(myList)

myList.reverse()

print(myList)

# Compter les éléments d'une myList ou retourner le nombre d'éléments d'une liste

print(len(myList))

# Supprimer un élément de myList

print(myList)

del myList[2]

print(myList)

# Trouver la position d'un élément de la myList

print(myList)

position = myList.index('le')

print(position)

# Compter le nombre d'occurences d'un élément

myList.append('le')

myList.append('le')

print(myList)

occurence = myList.count('le')

print(occurence)

# une autre fonction pour supprimer un élément dans la myList

print(myList)

myList.remove('Ministre')

print(myList)

myList.remove('le')

print(myList)








