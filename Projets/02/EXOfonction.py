import os
"""
Exercice 1:
1) Qu'affiche le programme suivant ?"""

def starts(n):
    print(n*"*")
starts(3)
starts(10)

"""
le resultat est le suivant:
***
**********
"""

#2) En utilisant cette fonction dans une boucle, produire l'affichage suivant:


def starts():
    return "*"
etoile = starts()

for i in range(6):
    ligne = i+1
    nbre_etoile = etoile * ligne 
    print(nbre_etoile)

"""
Exercice 2:
Que fait et affiche le programme suivant ?"""

def MaFonction(a,b):
    y=a+b
    return y
    
a=2;b=5
c=MaFonction(a,b)
print("c = ", c)

z=MaFonction(3,2+5)
print("z = ", z)
        
# Combien la fonction nommée MaFonction a-t'elle d'arguments en entrée ? en sortie ?
"""
c =  7
z =  10
La fonction MaFonction a un 1 argument à l'entrée et un à la sortie. Cependant ladite
fonction est appelée à chaque fois pour un nouveau calcul/nouvelle intégration d'une
valeur:la réatulisabilité"""

# Écrire une fonction, nommée MyNewFct, avec trois arguments qui retourne la moyenne des trois valeurs.
def MyNewFct():
    somme = x + y + z
    return somme

x=10; y=20; z=30
somme = MyNewFct()
print(somme)

moyenne = int(somme/3)
print(moyenne)

"""
3) Écrire une fonction, nommée Mention, qui a un argument en entrée: une note entre
0 et 20, et en sortie renvoie la mention correspondante: P, AB, B, TB.
Compléter cette fonction pour qu'elle affiche un message d'erreur si la note entrée
est négative ou supérieure à 20."""
from random import*

ma_variable = randint(0,20)

def Mention():
    appreciation = 'P','AB','B','TP'
    return ma_variable
appreciation = Mention()
print(appreciation)
while appreciation is range(10,11):
    print('P') 
    if appreciation is range(12,14):
        print('AB')        
        if ma_variable is range(14,16):
            print('B')
            if ma_variable is range(14,16):
                print('B')
                if appreciation is range(14,16):
                    print('B')
                    if appreciation is range(17,20):
                        print('TB')
else:
    print('erreur')
                
            

"""
Exercice 3:
Qu'affiche le programme suivant ?"""
def f(x):
    return 100*x-4*x**2+2

print(f(2))
    
"""
Écrire un programme qui affiche les valeurs f(x) pour tous les nombres entiers x
entre 0 et 20 (utiliser une boucle for ...)"""

def f(x):
    
    for i in range (0,20):
        ligne = i + 1
        
  
        return 100*ligne-4*ligne**2+2
nombre = 100*ligne-4*ligne**2+2

print(f(nombre))
# ou

def f(n):
      
    return 100*x-4*x**2+2
                
print(f(1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20))










    


os.system ("pause")
