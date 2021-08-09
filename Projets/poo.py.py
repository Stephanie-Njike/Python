from tkinter import *


fen1 = Tk()
tex1 = Label(fen1, text='Bonjour tout le monde !', fg='red')
tex1.pack()
bou1 = Button(fen1, text='Quitter', command = fen1.destroy)
bou1.pack()
fen1.mainloop()



"""
sommeEuros = input('Entrer la somme a convertir en dollars')
print(1.65*int(sommeEuros))
"""
"""
a, b = 1, 1
while a < 1771:
    print(b)
    a, b = b, b*3
"""

"""
prec = 1
for i in range(1, 13):
    print(prec)
    prec = prec*3
"""

"""
i = 1
while i <= 16384:
    # sommeEuros = input('Entrer la somme a convertir en dollars ')
    print('Vous voulez convertir ', i, 'Euros en dollars')
    print(i,'Euros = ', 1.65*i, 'Dollars')
    i = i*2
"""
"""
class Rectangle:

    def __init__(self, long, larg):
        self.longueur = long
        self.largeur = larg

    def perimetre(self):
        return (self.longueur + self.largeur)*2

class Carree:

    def __init__(self, cote):
        self.cote = cote

    def perimetre(self):
        return (self.cote * 4)

class Cercle:

    def __init__(self, rayon):
        self.rayon = rayon

    def perimetre(self):
        return (self.rayon * self.rayon * 3.14)


rectangle = Rectangle(10, 5)
print('Le perimetre du rectangle est :')
print(rectangle.perimetre())
rectangle.longueur = 3
rectangle.largeur = 2
print('Le perimetre du rectangle est :')
print(rectangle.perimetre())
largeur = rectangle.largeur
print(largeur)



carree = Carree(10)
print('Le perimetre du carree est :')
print(carree.perimetre())

cercle = Cercle(5)
print('Le perimetre du cercle est :')
print(cercle.perimetre())
"""

"""
class Rectangle:

    def __init__(self, long, larg):
        self.longueur = long
        self.largeur = larg
        
    def _get_longueur(self):
        print ("Récupération de la longueur")
        return self.longueur

    def _set_longueur(self, long):
        print ("Changement de la longueur")
        self.longueur  =  long

    @property
    def _largeur(self):
         print ("Récupération de la largeur")
         return self.largeur
        
    @_largeur.setter
    def _largeur(self, larg):
        print ("Changement de la largeur")
        self.largeur  =  larg

    # _largeur=property(_get_largeur, _set_largeur)
    _longueur=property(_get_longueur, _set_longueur)


rectangle = Rectangle(10, 5)
rectangle._longueur = 10
long = rectangle._longueur
print(rectangle.longueur)

rectangle._largeur = 5
larg = rectangle._largeur
print(rectangle.largeur)

print(dir(rectangle))
print(rectangle.__dict__)

"""

"""
class Personne:
    nom = 'Alex'
    prenom = 'Moi'
    def __init__(self, nom, prenom):
        self.nom = nom
        self.prenom = prenom

    def nomComplet(self):
        return self.nom + ' ' +self.prenom

    def personneMarche(self):
        print('La personne marche!')


class Eleve(Personne):
    def __init__(self, matricule):
        self.matricule = matricule

    def personneMarche(self):
        Personne.personneMarche(self)
        print('L\'eleve marche!')

personne = Personne('MVAH', 'Fabrice')
print(personne.nomComplet())

eleve = Eleve('1008')
print(eleve.matricule)
print(eleve.nom)
print(eleve.nomComplet())
print(eleve.personneMarche())

"""












    
