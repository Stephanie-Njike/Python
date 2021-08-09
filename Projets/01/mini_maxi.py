### 13.01.21

# exercice :

"""
mini_maxi.py : écrire 2 fonctions :
— mini (a,b) qui renvoie le minimum entre a et b
— maxi (a,b) qui renvoie le maximum entre a et b
Les 2 nombres a et b seront demandés à l’utilisateur
"""

def mini(a,b):
    if a < b :
        return a
    else:
        return b
        
def maxi(a,b):
    if a > b:
        return a
    else:
        return b
    
a = input('Veuiller entrer le premier nombre: ')
a = int(a)
b = input('Veuiller entrer le deuxieme nombre: ')
b = int(b)
    
print('la fonction maxi retourne la grande valeur qui est',maxi(a,b))
print('la fonction mini retourne la plus petite valeur qui est',mini(a,b) )
