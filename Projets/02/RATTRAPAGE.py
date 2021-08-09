import os


''' Exercices
2.1 Décrivez le plus clairement et le plus complètement possible ce qui se passe à chacune
des trois lignes de l’exemple ci-dessous :
>>> largeur = 20
>>> hauteur = 5 * 9.3
>>> largeur * hauteur
930'''

'''  REPONSE
- La varaible 'largeur' reçoit la valeur 20
- La variable 'hauteur' reçoit la valeurs 5 * 9.3
- En multipliant les deux variables ci-dessus, on obtient la valeur 930'''



'''  2.2 Assignez les valeurs respectives 3, 5, 7 à trois variables a, b, c.
Effectuez l’opération a - b//c. Interprétez le résultat obtenu.

    SOLUTION '''

a = 3
b = 5
c = 7
d = a - b // c 
print(d)

   """ INTERPRETATION
'''
-Lopérateur  permet de récupérer la partie entière de la division. Cependant,
je note que les valeurs ont été inversées pendant la division. Je m'attendais à
ce que la réponse soit 0 conformément à l'opération -2 7; -2 étant le résultat
de 3 - 5
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






























os.system("pause")
