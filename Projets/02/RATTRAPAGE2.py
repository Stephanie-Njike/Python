import os


""" Exercices
2.1 Décrivez le plus clairement et le plus complètement possible ce qui se passe à chacune
des trois lignes de l’exemple ci-dessous :
>>> largeur = 20
>>> hauteur = 5 * 9.3
>>> largeur * hauteur
930"""

"""  REPONSE
- La varaible 'largeur' reçoit la valeur 20

- La variable 'hauteur' reçoit la valeurs 5 * 9.3

- En multipliant les deux variables ci-dessus, on obtient la valeur 930"""



"""  2.2 Assignez les valeurs respectives 3, 5, 7 à trois variables a, b, c.
Effectuez l’opération a - b//c. Interprétez le résultat obtenu.


    SOLUTION """

a = 3
b = 5
c = 7
d = a - b // c 
print(d)

   # INTERPRETATION
"""
-Lopérateur // permet de récupérer la partie entière de la division. Cependant,
je note que les valeurs ont été inversées pendant la division. Je m'attendais à
ce que la réponse soit 0 conformément à l'opération -2/7; -2 étant le résultat
de 3 - 5. LA DIVISION TOUT COMME LA MULTIPLICATION PRIME SUR LA SOUSTRATION ET L'ADDITION
"""


"""
Exercice
2.3 Testez les lignes d’instructions suivantes. Décrivez dans votre cahier ce qui se passe :
>>> r , pi = 12, 3.14159
>>> s = pi * r**2
>>> print(s)
>>> print(type(r), type(pi), type(s))
Quelle est, à votre avis, l’utilité de la fonction type() ? """

r , pi = 12, 3.14159
s = pi * r**2
print(s)
print(type(r), type(pi), type(s))

""" DESCRIPTION:

- Lorsque deux valeurs côte à côte sont précédées de deux variables séparées par la virgule,
le langage Python a la possibilité d'affecter chacune des valeurs à une variable, ce en
respectant la position initiale de chacune: affectation multiple ou affectation à plusieurs
variables simultanément.

- le symbole "*" est celui de la multiplication

- Une variable peut en recevoir une autre avec sa/ses valeur(s)

- L'opérateur ** (puissance) permet de multiplier la valeur qui la précède par lui-même, en
tenant compte de la la valeur qui la suit qui, elle-même désigne le nombre de puissance

- la fonction type() permet d'afficher le type de variable (int, float, str, ...) qui se
trouve dans la parenthèse
"""


""" Exercice

a, b, c, d = 3, 4, 5, 7

Actuellement, a contient la valeur 3, et c la valeur 5 ; nous voudrions que ce soit
l’inverse. Comment faire ?

4.1 Écrivez les lignes d’instructions nécessaires pour obtenir ce résultat.


    SOLUTION:"""
a, b, c, d = 3, 4, 5, 7
a,c = c,a
print(a,c)

maison, manger, dormir, voyager = 'yaoundé','douala','bafoussam','bafang'
maison,voyager = voyager, maison
print(maison,voyager)

""" COMMENTAIRE:

En plus d'affecter les valeurs à plusieurs variables simultanément, Python auffre aussi cette
possibilé de changer la/les valeur(s) d'une variable: LA RE-AFFECTATION
"""

"""
Exercices
4.2 Écrivez un programme qui affiche les 20 premiers termes de la table de multiplication
par 7.
     SOLUTION """

a = 0
while a < 20:
    a = a + 1
    multiplication = a * 7
    print(multiplication)


"""
4.3 Écrivez un programme qui affiche une table de conversion de sommes d’argent exprimées
en euros, en dollars canadiens. La progression des sommes de la table sera « géométrique »,
comme dans l’exemple ci-dessous :
1 euro(s) = 1.65 dollar(s)
2 euro(s) = 3.30 dollar(s)
4 euro(s) = 6.60 dollar(s)
8 euro(s) = 13.20 dollar(s)
etc. (S’arrêter à 16384 euros.)


    SOLULION: """

"""i = 1
while i <= 16384:
    # sommeEuros = input('Entrer la somme a convertir en dollars ')
    print('Vous voulez convertir ', i, 'Euros en dollars')
    print(i,'Euros = ', 1.65*i, 'Dollars')
    i = i * 2

i = 1
while i < 16384:
    i = i * 2
    print(i, 'Euros = ', 1.65*i, 'Dollars')"""


"""
euro = 1
dollar = euro + 0.65
while euro < 16384
somme_euros = input('entrer la somme à convertir en dollars: ')
print(1.65*int(somme_euros))


while True:
    sommeEuros = input('Entrer la somme a convertir en dollars ')
    print('Vous voulez convertir ', sommeEuros, 'Euros en dollars')
    print(sommeEuros,'Euros = ', 1.65*int(sommeEuros), 'Dollars')
"""
    
""" 4.4 Écrivez un programme qui affiche une suite de 12 nombres dont chaque terme soit
égal au triple du terme précédent."""


a, b = 1, 1
while a < 177147:
    print(b)
    a,b = b, b*3
    
# OU
a = 1
for i in range(1, 13):
    print(a)
    a = a*3



#Exercices page 35,36


"""
4.5 Écrivez un programme qui calcule le volume d’un parallélépipède rectangle dont sont
fournis au départ la largeur, la hauteur et la profondeur."""

largeur = 20
hauteur = 5 * 9.3
longueur = 35
volume = longueur * largeur * hauteur
print(volume)


"""
4.6 Écrivez un programme qui convertit un nombre entier de secondes fourni au départ en
un nombre d’années, de mois, de jours, de minutes et de secondes (utilisez l’opérateur
modulo : %)."""

# le modulo (%) est un opérateur qui permet de récupérer le reste de la division

nombre_de_seconde = 150000
nombre_de_minute = nombre_de_seconde % 60           # 60 est le nbre de seconde par minute
nombre_heure = nombre_de_seconde % 3600             # 3600 est le nombre de seconde par heure
nombre_de_jour = nombre_de_seconde % 86400          # 86400 = au nombre de seconde par jour
nombre_de_mois = nombre_de_seconde % 2592000        # 2592000 est le nbre de seconde/mois(30 jrs)
nombre_année = nombre_de_seconde % 31536000         # 31536000 est le nbre de seconde/an (365 jrs)

print(nombre_de_minute, nombre_heure, nombre_de_jour, nombre_de_mois,nombre_année)


"""
4.7 Écrivez un programme qui affiche les 20 premiers termes de la table de multiplication
par 7, en signalant au passage (à l’aide d’une astérisque) ceux qui sont des multiples de
3.
Exemple : 7 14 21 * 28 35 42 * 49 ..."""

a = 1
while a < 20:
    a = a + 1
    table = a * 7
    print(a," * "," 7 "," = ",table)
    if table % 3 == 0:
        print(a," * "," 7 "," = ",table,"*")

       
"""
4.8 Écrivez un programme qui calcule les 50 premiers termes de la table de multiplication
par 13, mais n’affiche que ceux qui sont des multiples de 7.
"""

a = 1
while a < 50:
    a = a + 1
    table = a * 13
    if table % 7 == 0:
        print(a," * ","13", " = ",table)

            
"""
4.9 Écrivez un programme qui affiche la suite de symboles suivante :
*
**
***
****
*****  
******
*******"""

a = "*"
ligne = "*" * 7
print(a)
print(a*2)
print(a*3)
print(a*4)
print(a*5)
print(a*6)
print(a*7)

for i in range(0, 7):
    print(a*i)




os.system("pause")
