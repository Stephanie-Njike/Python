#### 18.02.2021

"""
12.5 Définissez une classe Cercle(). Les objets construits à partir de cette
classe seront des cercles de tailles variées. En plus de la méthode constructeur
(qui utilisera donc un paramètre rayon), vous définirez une méthode surface(),
qui devra renvoyer la surface du cercle.
Définissez ensuite une classe Cylindre() dérivée de la précédente.
Le constructeur de cette nouvelle classe comportera les deux paramètres rayon
et hauteur. Vous y ajouterez une méthode volume() qui devra renvoyer le volume
du cylindre (rappel : vo-lume d’un cylindre = surface de section × hauteur).
Exemple d’utilisation de cette classe:
>>> cyl = Cylindre(5, 7)
>>> print(cyl.surface())
78.54
>>> print(cyl.volume())
549.78
"""
from math import pi
"""
Définissez une classe Cercle(). Les objets construits à partir de cette
classe seront des cercles de tailles variées. En plus de la méthode constructeur
(qui utilisera donc un paramètre rayon),
"""
class Cercle:
    def __init__(self,rayon):
        self.rayon = rayon

#, vous définirez une méthode surface(), qui devra renvoyer la surface du cercle.

    def surface(self):
        return pi*self.rayon**2

"""Définissez ensuite une classe Cylindre() dérivée de la précédente."""

class Cylindre(Cercle):
# Le constructeur de cette nouvelle classe comportera les deux paramètres rayon
#et hauteur.
    def __init__(self,rayon,hauteur):
        Cercle.__init__(self,rayon)
        self.hauteur = hauteur

# Vous y ajouterez une méthode volume() qui devra renvoyer le volume
#du cylindre (rappel : vo-lume d’un cylindre = surface de section × hauteur).

    def volume(self):
        s = Cercle.surface(self)### meme quand je l efface cette ligne , elle retourne lareponse
        return self.hauteur * s
    ## comment dois je ecrire pi*self.rayon**2 si je veux ecrire la ligne du haut?

#cyl = Cylindre(5, 7)
#print(cyl.surface())
#print(cyl.volume())

"""
12.6 Complétez l’exercice précédent en lui ajoutant encore une classe Cone(),
qui devra dériver cette fois de la classe Cylindre(), et dont le constructeur
comportera lui aussi les deux paramètres  rayon  et  hauteur. Cette nouvelle
classe possédera sa propre méthode volume(), laquelle devra renvoyer le volume
du  cône (rappel : volume d’un cône= volume du cylindre correspondant divisé
par 3).
Exemple d’utilisation de cette classe:
>>> co = Cone(5,7)
>>> print(co.volume())
183.26
"""

"""
from math import pi
class Cercle:
    def __init__(self,rayon):
        self.rayon = rayon
    def surface(self):
        return pi*self.rayon**2
class Cylindre(Cercle):
    def __init__(self,rayon,hauteur):
        Cercle.__init__(self,rayon)
        self.hauteur = hauteur
    def volume(self):
        s = Cercle.surface(self)
        return self.hauteur * s
"""
"""
Complétez l’exercice précédent en lui ajoutant encore une classe Cone(),
qui devra dériver cette fois de la classe Cylindre(),
"""

class Cone(Cylindre):

#, et dont le constructeur comportera lui aussi les deux paramètres  rayon
#et  hauteur.
     def __init__(self,rayon,hauteur):
         Cylindre.__init__(self,rayon,hauteur)

#Cette nouvelle classe possédera sa propre méthode volume(), laquelle devra
#renvoyer le volume
#du  cône (rappel : volume d’un cône= volume du cylindre correspondant divisé 
     def volume(self):
         v = Cylindre.volume(self)
         return self.hauteur * v /3
    
co = Cone(5,7)
print(co.volume())
"""
12.7 Définissez une classe JeuDeCartes() permettant d’instancier des objets dont
le comportement soit similaire à celui d’un vrai jeu de cartes.
La classe devra comporter au moins les quatre méthodes suivantes:
* méthode constructeur : création et remplissage d’une liste de 52 éléments, qui
sont eux-mêmes des tuples de 2 entiers. Cette liste de tuples contiendra les
caractéristiques de chacune des 52 cartes. Pour chacune d’elles, il faut en
effet mémoriser séparément un entier indiquant la valeur (2, 3, 4, 5, 6, 7,
8, 9, 10, 11, 12, 13, 14, les 4 dernières valeurs étant celles des valet, dame,
roi et as), et un autre entier indiquant la couleur de la carte
(c’est-à-dire 3,2,1,0 pour Cœur, Carreau, Trèfle et Pique). Dans une telle liste
, l’élément (11,2) désigne donc le valet de Trèfle, et la liste terminée doit
être du type:[(2, 0), (3,0), (3,0), (4,0), ..... (12,3), (13,3), (14,3)]
* méthode  nom_carte(): cette méthode doit renvoyer, sous la forme d’une chaîne,
l’identité d’une carte quelconque dont on lui a fourni le tuple descripteur en
argument.
Par exemple, l’instruction:
print(jeu.nom_carte((14, 3))) doit provoquerl’affichage de: As de pique
* méthode battre() : comme chacun sait, battre les cartes consiste à les
mélanger.Cette méthode sert donc à mélanger les éléments de la liste contenant
les cartes,quel qu’en soit le nombre.
* méthode tirer() : lorsque cette méthode est invoquée, une carte est retirée du
jeu. Le tuple contenant sa valeur et sa couleur est renvoyé au programme appelant.
On retire toujours la première carte de la liste. Si cette méthode est invoquée
alors qu’il ne reste plus aucune carte dans la liste, il faut alors renvoyer
l’objet spécial None auprogramme appelant.
Exemple d’utilisation de la classe JeuDeCartes():
jeu = JeuDeCartes()                # instanciation d'un objet
jeu.battre()                       # mélange des cartes
for n in range(53):                # tirage des 52 cartes:
    c = jeu.tirer()
    if c == None:                  # il ne reste plus aucune carte
        print('Terminé !')         # dans la liste
    else:
    print(jeu.nom_carte(c))        # valeur et couleur de la carte

"""

"""
import random
class JeuDecartes2:
      couleursReeles = ['Cœur', 'Carreau', 'Trèfle', 'Pique']
      couleurs =[0,1,2,3]
      valeurs =[2,3,4,5,6,7,8,9,10,11,12,13,14]
      valeursReelesAPartirDe11 = ['AS', 'Valet', 'Dame' , 'Roi']
      def __init__(self):
          self.liste =[]
          for x in JeuDecartes2.valeurs:
            for y in JeuDecartes2.couleurs:
                self.liste.append((x,y))

      def nom_carte(self, tupl):
          couleurInt = tupl[1]
          couleurReele = JeuDecartes2.couleursReeles[couleurInt]
          print('la couleur reelle est : ',couleurReele)
          valeurInt= tupl[0]
          valeurReele =""
          if valeurInt <= 10:
             valeurReele = "{0}".format(valeurInt)
          else:
              index = valeurInt -11
              valeurReele = JeuDecartes2.valeursReelesAPartirDe11[index]
              print('la valeur reelle est ',valeurReele)

          resul = "{0} de {1}".format(valeurReele, couleurReele)
          return resul

jdc = JeuDecartes2()

nom_carte = jdc.nom_carte((18,3))
print(nom_carte)
"""
          
import random
class MonJeuDeCartes:
    valeursDesCartes =[(2, ''), (3, ''), (4, ''), (5, ''), (6, ''), (7, ''), (8, ''), (9, ''), (10, ''), (11, 'Valet'), (12, 'Dame'), (13, 'Roi'), (14, 'As')]
    couleursDesCartes = [(3, 'Coeur'), (2, 'Carreau'), (1, 'Trefle'), (0, 'Pique')]
    def __init__(self):
        self.liste = []
        for (x, m) in MonJeuDeCartes.valeursDesCartes:
            for (y, v) in MonJeuDeCartes.couleursDesCartes:
                self.liste.append((x,y))
        print(self.liste)
        
    def nom_carte(self, tuple):
        if (tuple[0] > 1)and (tuple[0] < 15) and (tuple[1] >=0) and (tuple[1] < 4): 
            tupleValeur = None
            tupleCouleur = None
            for (val, equiv) in MonJeuDeCartes.valeursDesCartes:
                if val == tuple[0]:
                    tupleValeur = (val, equiv)
                
            for (coulInt, coul) in MonJeuDeCartes.couleursDesCartes:
                if coulInt == tuple[1]:
                    tupleCouleur = (coulInt, coul)
            if tupleValeur[0] > 10:
                return '{0} de {1}'.format(tupleValeur[1], tupleCouleur[1])
            else:
                return '{0} de {1}'.format(tupleValeur[0], tupleCouleur[1])
        else:
            return 'Veuillez entrer un tuple valide'
        
    def battre(self):
        print('Melanger la liste des cartes')
        random.shuffle(self.liste)
        return self.liste

    def tirer(self):
        carteTirer = None
        if len(self.liste) > 0:
            carteTirer = self.liste[0]
            self.liste.remove(carteTirer)
        return carteTirer
        
monjeu = MonJeuDeCartes()
print(monjeu.nom_carte((14, 2  )))
print(monjeu.battre())
print(monjeu.tirer())
print(monjeu.liste)
    

"""         
class JeuDeCartes:
    def __init__(self):
        self.couleur = ['Cœur', 'Carreau', 'Trèfle', 'Pique']
        self.valeur = ['2','3','4','5','6','7','8','9','10','AS', 'Valet', 'Dame' , 'Roi']
        self.liste = []
        for x in self.valeur:
            for y in self.couleur:
                self.liste.append((x,y))

    def nom_carte(self,identiteCarte):
        for element in self.liste :
            self.identiteCarte = element[0] + ' ' + 'de' + ' ' + element[1]
        return self.identiteCarte

    def battre(self):
        random.shuffle(self.liste)
        return self.liste 

    def tirer(self):
        tailleListe = len (self.liste)
        if tailleListe == 0:
            print('Terminé !')
        else:
            self.carteTiree = self.liste[0]
            del(self.liste[0])
        return self.carteTiree
                #self.echantillon  = random.sample(self.liste,1)
       # return self.echantillon
        
     
           
        
#jeudecarte1 =  JeuDeCartes()       
#print(jeudecarte1.liste)
#jeudecarte1.nom_carte(('As','Trèfle'))
#print(jeudecarte1.identiteCarte)
#jeudecarte1.battre()
#print(jeudecarte1.liste)
#jeudecarte1.tirer()
#print(jeudecarte1.carteTiree)
#print(jeudecarte1.echantillon)



"""   
        
    




