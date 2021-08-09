####  18.01.2021

#### file:///C:/Users/emericc/AppData/Local/Temp/Cours-Python-Exercices-A.pdf


### Exercice numérique No 1:


# fichier : exo_num_1.py by J.Tschanz
# fonction : quelques opérations sur les nombres.

nbr_1 = 3            # entier normal
nbr_2 = 999999999    # entier long                   #####????? avec L a la fin elle marque une erreur , comment le rendre en entier long ? 
nbr_3 = 1.24         # virgule flottante                     # en enlevant le L la variable est assignee a un integer
nbr_4 = 0xff         # nombre hexa.
nbr_5 =  25 + 4.0j   # complexe
nbr_6 = 4
print(type(nbr_2))


# simple calculs !!
print ("Un entier sur un flottant : %s " % (nbr_1/nbr_3))
print ("Un hexa + un complexe : %s " % (nbr_4+nbr_5))
print ("Un long - (un entier * un hexa.) : %s " % (nbr_2 - nbr_1*nbr_4))
print ("Une puissance : %s " % (nbr_3**nbr_1))                               # puissance
print ("Un entier sur un entier !? : %s" % (nbr_6/nbr_1))                    # attention entier divisé par un entier
print ("Un modulo avec un réel : %s " % (nbr_6%nbr_3))                       # modulo avec un reel






### Exercice numérique No 2.


# fichier : exo_num_2.py by J.Tschanz
# fonction : quelques opérations booléennes.

x = y = 1                                                                    # simple calculs !!
print ("Décalage à gauche : %s " % (y<<2) )                                  # décalage à gauche : 0100 (4)
print ("OU bits-à-bits : %s " % (x | 2))                                     #  0011 (3)
print ("ET bits-à-bits : %s " % (x & 3))                                     # 0001 (1)
print ("XOR bits-à-bits : %s" % (x^y))                                       # 0000 (0)




### Exercice sur les chaînes No 1:


# fichier : exo_chaine_1.py by J.Tschanz
# fonction : quelques opérations sur les chaînes.
# déclarations
s1 = 'Hello World'
s2 = " I'm here !!"
s3 = """Python is a good
programming
language !!"""                                                              # sur plusieurs lignes !!

# opérations
print ("Concaténation : ")
print (s2+s1)
print ("Répétition : ")
print (s1*4)
print ("Longueur d'une chaîne : ")
print (s3,len(s3))                 ####???? comment compte t on la longueur ds ce cas? ici 40?
print ("Insertion : ")
print ("I told you : %s" % s1)


### Exercice sur les chaînes No 2:

# fichier : exo_chaine_2.py by J.Tschanz
# fonction : quelques indiçages sur les chaînes.

# déclarations
s1 = "0123456789"

# indiçages
print ("quelques indiçages :")
print ("")
print ("De la position 0 à 4 non comprise : ")
print (s1[0:4])
print ("Idem : ")
print (s1[:4])
print ("De la positon 4 à la fin : ")
print (s1[4:])                                                                #  (4eme comprise)
print ("La troisième position : ")
print (s1[3])
print ("La troisième depuis la fin :")
print (s1[-3])
print ("Du début à l'avant dernière position : ")
print (s1[:-1])


### Exercice sur les chaînes No 3.

# fichier : exo_chaine_3.py by J.Tschanz
# fonction : quelques changements de formatage.

# déclarations
s1 = "My name is Python !"

# modification par "copie"
print (s1)
print ("")
print ("Modification par copie :")
print ("")
s1 =  ('Your' + s1[2:])
print (s1)

s2 =  ('December')
print ("My birthdate is : %s %s %s" % (28,s2,77))#####???? lire en bas


### Exercice sur les listes No 1.

# fichier : exo_file_1.py by J.Tschanz
# fonction : montre les fonctions principales sur les listes

# définition des listes
liste_une = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
liste_deux = ['a', 'b', 'c', 'd', 'e', 'f']
liste_trois = []

# affichage simple
print (liste_une)

# concaténation
print ("Une concaténation : ")
print (liste_une + liste_deux)
print ("Une répetition : ")
# répetiton
print (liste_une*2)
print ("---------------------")

# affichage avec un indice
print ("Extraction par indiçage : ")
print (liste_une[0])

# avec une tranche (entre 2 et 4)
print ("Extraction par tranche :")
print (liste_une[2:4])

# tranche de 4 à la fin
print (liste_une[4:])

# tranche du début à la 4
print (liste_une[:4])
print ("---------------------")
print ("Ajout dans une liste : ")
liste_trois.append(liste_une)
liste_trois.append(liste_une)
print (liste_trois)
print ("Remplacement : ")
liste_trois[1] = liste_deux
print (liste_trois)
print ("Extraction avec plusieurs indices : ")
print (liste_trois[0][4])
print (liste_trois[1][2])
print ("Supression : ")
liste_trois[0] = []
del liste_trois[1]
print (liste_trois)               


### Exercice sur les listes No 2:

# fichier : exo_file_2.py by J.Tschanz
# fonction : montre les fonctions principales sur les listes

# définition des listes
liste_une = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
liste_deux = ['f', 'e', 'd', 'c', 'b', 'a']

# afficher la longueur de chaque liste
print ("La longueur de chaque listes : ")
print (len(liste_une), len(liste_deux))

print ("---------------")

# invertion de la liste
print ("La fonction reverse() : ")
liste_une.reverse()
print (liste_une)

print ("---------------")

# remise dans l'ordre de la liste_deux
print ("La fonction sort() : ")
liste_deux.sort()
print (liste_deux)

print ("---------------")

# recherche de l'indice depuis la valeur
print ("La fonction index() : ")
print (liste_deux.index('b'))

print ("---------------")

# création d'une list depuis une chaîne de caractères
print ("La fonction list() : ")
chaine = "Hello World !"
print (list(chaine))


### Exercice sur les dictionnaires No 1:

# file : exo_dico_1.py by J.Tschanz
# présentation des fonctions possibles avec les dictionnaires

dico_1 = {'one' : {'un' : 1}, 'two' : {'deux' : 2}}
dico_2 = {'japan' : 'japon', 'switzerland' : 'suisse'}
dico_3 = {}

# affichage simple
print ("Nos deux dictionnaires :")
print (dico_1)
print (dico_2)
print ("---------")

# affichage par indice de clé
print ("Une recherche par clef : ")
print (dico_2['japan'])
print (dico_1['one'])
print (dico_1['one']['un'])
print ("---------")

# liste des clés d'un dico.
print ("La liste des clefs du dictionnaire 2 ")
print (dico_2.keys())
print ("---------")

# liste des valeurs du dico.
print ("La liste des valeurs du dictionnaire 2")
print (dico_2.values())
print ("---------")

# la longueur du dico.
print ("La longueur du dictionnaire 1 ")
print (len(dico_1))
print ("---------")

# ajout d'une valeur ou modification
print ("Ajout et modification dans le dictionnaire 2 ")
dico_2['japan'] = ['nihon']
dico_2['germany'] = ['allemagne']
print (dico_2)
print ("---------")

# suppression d'une valeur
print("Suppression dans le dictionnaire 2 ")
del dico_2['japan']
print(dico_2)
print("---------")

# méthode de recherche d'appartenance
print("Méthode de recherche d'appartenance ")

print(dico_1)
print(dico_2)

if dico_1.get('one') == {'un': 1}:
    print ("dico_1 --> 'one' ! ")
else:
    print ("dico_1--> ?? ")
    
if dico_2.get('germany') == 1:
    print ("dico_1--> ?? ")                     
    
if dico_2.get('germany') == ['allemagne']:
    print ("dico_2 --> 'germany' ! ")
else:
    print ("dico_2--> ?? ")

if dico_1.get('japan') == 1:
    print ("dico_1 --> 'japan' ! ")
else:
    print ("dico_1--> ?? ")

"""
if dico_1.has_key('one') :
    print ("dico_1 --> 'one' ! ")
else:
    print ("dico_1--> ?? ")
    
    
if dico_2.has_key('germany') :
    print ("dico_1--> ?? ")
    
if dico_2.has_key('germany') :
    print ("dico_2 --> 'germany' ! ")           ##########??????
else:
    print ("dico_2--> ?? ")

if dico_1.has_key('japan') :
    print ("dico_1 --> 'japan' ! ")
else:
    print ("dico_1--> ?? ")

"""

if dico_1['one'] == {'un': 1}: 
    print ("dico_1 --> 'one' ! ")
else:
    print ("dico_1--> ?? ")
    
    
if dico_2['germany'] == 1:
    print ("dico_1--> ?? ")
    
if dico_2['germany'] == ['allemagne'] :
    print ("dico_2 --> ['germany'] ! ")           ##########?????? peut on utiliser le code qui permet l affichage 
else:                                             #par indice  de cle? ou ce que l on utilise parfois pour changer 
    print ("dico_2--> ?? ")                       #la valeur d une cle afin d ecrire le code de la methode d appartenance 

if dico_1['japan'] == 1 :
    print ("dico_1 --> 'japan' ! ")
else:
    print ("dico_1--> ?? ")




### Exercice sur les tuples No 1:

# fichier : exo_tuple_1.py by J.Tschanz
# fonction : montre l'erreur lors de l'affectation d'un valeur.

# définition du tuple
tuple_1 = (0, 1, 2, 3, 4, 5, 6, 7, 8, 8,)

# lecture du tuple (idem à la liste)
print ("Lectures d'un tuple avec et sans indices : ")
print (tuple_1)
print (tuple_1[4])
print (tuple_1[:5])
print (tuple_1[-2])

print ("------------")
print ("Remplacement total du tuple : ")
tuple_1 = (0, 1, 2, 3, 4, 5, 6, 7, 8, 9)
print ("----------")
print (tuple_1)

# essai de changement de 6 par 6.0 (par assignement) !!

print ("Un essai de changement partielle : ")
#tuple_1[6] = 6.0 ## TypeError: 'tuple' object does not support item assignment



### Exercice sur les tuples No 2:

# fichier : exo_tuple_2.py by J.Tschanz
# fonction : montre les fonctions principales sur les tuples

# définition des listes
tuple_1 = (0, 1, 2, 3, 4, 5, 6, 7, 8, 9)
tuple_2 = ('a', 'b', 'c', 'd', 'e', 'f')
tuple_3 = ()

# affichage simple
print (tuple_1)
print ("Concaténation de tuples : ")
print (tuple_1 + tuple_2)
print ("Répétition : ")
print (tuple_2 * 2)
print ("---------------------")
print ("Séléctions par indice : ")
# affichage avec un indice
print (tuple_1[0])

# avec une tranche (entre 2 et 4)
print (tuple_1[2:4])
# tranche de 4 à la fin
print (tuple_1[4:])
# tranche du début à la 4
print (tuple_1[:4])
print ("---------------------")

# insertion de tuples dans un tuple
tuple_3 = (tuple_1, tuple_2)
print (tuple_3)

# affichage avec plusieurs indices
print (tuple_3[0][4])
print (tuple_3[1][2])

#supression
tuple_3 = ()
print (tuple_3)

# afficher la longueur de chaque tuples
print (len(tuple_1), len(tuple_2), len(tuple_3))







