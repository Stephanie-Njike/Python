"""
class Personne:

    def __init__(self, nom, prenom, age):
        self.nom = nom
        self.prenom = prenom
        self.age = age

    def marche(self):
        print('Je marche')

    def donne_moi_le_nom(self):
        print(self.nom)
        
        
pers1 = Personne('Alex', 'Alex', 10)
pers2 =  Personne('Maxime', 'Parfait', 20)

print(pers1.nom)
print(pers2.nom)

pers1.marche()
pers1.donne_moi_le_nom()
"""
"""
class Rectangle:
    def __init__(self,longueur,largeur):
        self.longueur = longueur
        self.largeur = largeur

    def perimetre(self):
        print((self.longueur + self.largeur)*2)
    def _get_longueur(self):
        print ("Récupération de la longueur")
        return self.longueur

    def _set_longueur(self, long):
        print ("Changement de la longueur")
        self.longueur  =  long

    def _get_largeur(self):
        print ("Récupération de la largeur")
        return self.largeur

    def _set_largeur(self, larg):
        print ("Changement de la largeur")
        self.largeur  =  larg

    _longueur=property(_get_longueur, _set_longueur)
    _largeur=property(_get_largeur, _set_largeur)

    @property
    def _longueur(self):
         print ("Récupération de la longueur")
         return self.longueur
        
    @_longueur.setter
    def _longueur(self, long):
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

figure = Rectangle(10,15)
figure.perimetre()

figure._longueur = 20
print(figure._longueur)
"""

"""
class Point:
    def __init__(self, abs, ord):
        self.abs = abs
        self.ord = ord
    def __str__(self):
        return (self.abs, self.ord)
    
    def __st__(self, p):
        return (p.abs, p.ord)

    def calcul_distance(self, p):
        return ((p.abs - self.abs)**2 + (p.ord - self.ord)**2)*0.5

p1 = Point(3, 2)
p2 = Point(5, 0)

print(p1.calcul_distance(p2))

# print(p1.__str__())
# print(p1.__st__(p2))
"""
"""
class mere:
    # corps de la classe mère
 
class enfant(mere):
    # corps de la classe enfant
"""

class Personne:     
       
    # Constructeur         
    def __init__(self, nom, cin):    
        self.nom = nom 
        self.cin = cin 
 
    def afficher(self): 
        print("Nom : ",self.nom) 
        print("CIN : ",self.cin) 
 
class Employe( Personne ): 
 
    def __init__(self, nom, cin, salaire): 
        self.salaire = salaire 

        # appeler __init__ de la classe mère (Personne) 
        super().__init__(nom, cin)

    def afficher(self):
        Personne.afficher(self)
        print("salaire : ", self.salaire)
        
""" 
# création d'une variable d'instance
p=Personne("ISMAIL", "EE456788")
 
# appeler une fonction de la classe Personne en utilisant son instance
p.afficher()
"""
emp=Employe("Ismail", "EE4567", 7000)
emp.afficher()














    
