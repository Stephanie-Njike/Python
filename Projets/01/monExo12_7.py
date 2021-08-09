#### 18.03.2021

import random
class JeuDecartes:
    "definition de la classe et instanciation de l attribut classe"
    couleursReeles = ['Cœur', 'Carreau', 'Trèfle', 'Pique']
    couleurs =[3,2,1,0]
    valeurs =[2,3,4,5,6,7,8,9,10,11,12,13,14]
    valeursReelesAPartirDe11 = ['Valet', 'Dame' , 'Roi' , 'AS']
    def __init__(self):
        " definition de la methode constructeur et creation de la liste des tuples"
        self.liste =[]
        for x in JeuDecartes.valeurs:
            for y in JeuDecartes.couleurs:
                self.liste.append((x,y))

    def nom_carte(self, tupl):
        "definition de la methode qui renvoie sous forme d une chaine l identite d une carte"
        couleurInt = tupl[1]
        couleurReele = JeuDecartes.couleursReeles[couleurInt]
        print('la couleur reelle est : ',couleurReele)
        valeurInt= tupl[0]
        valeurReele =""
        if valeurInt <= 10:
            valeurReele = "{0}".format(valeurInt)
        else:
            index = valeurInt -11
            valeurReele = JeuDecartes.valeursReelesAPartirDe11[index]
            print('la valeur reelle est ',valeurReele)

        resul = "{0} de {1}".format(valeurReele, couleurReele)
        return resul

    def battre(self):
        "definition de la methode qui melangera les cartes"
        random.shuffle(self.liste)
        return self.liste 

    def tirer(self):
        "une carte est retirée du jeu. Le tuple contenant sa"
        "valeur et sa couleur est renvoyé au programme appelant."
        "On retire toujours la première carte de la liste."
        tailleListe = len (self.liste)
        if tailleListe == 0:
               print('Terminé !')
        
        if tailleListe > 0:
            self.carteTiree = self.liste[0]
            del(self.liste[0])
        return self.carteTiree
        
            

jdc = JeuDecartes()
print(jdc.liste)

nom_carte = jdc.nom_carte((11,3))
print(nom_carte)
print(jdc.battre())
print(jdc.tirer())

         
