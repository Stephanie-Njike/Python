### 13.01.21

# Exercice 1:

"""
Ecrire une fonction qui prend 2 listes en parametres,
et retourne le resultat des 2 listes fusionnees

"""

"""
def mes_2_listes(liste1, liste2):
    return liste1 + liste2 
print(mes_2_listes([0,1,3,2,6,9], [2,0,1,4,5,2]))
"""
# Exercice 2:

"""
Ecrire une fonction qui prend une liste en parametre,et retourne la forme
inverse
"""

def retourne(maliste):
    maliste.reverse()
    return maliste
print(retourne([1,2,3,4,5,6]))


# Exercice 3:

"""
Ecrire une fonction qui prend 2 parametres : un element et une liste et retourne la position de l element de la liste
"""

def position(a, liste3):
    # liste3.append(a)
    return liste3.index(a)
print(position(3, [1,2,3]))


# Exercice 4 :


#ECrire une fonction qui retourne la somme des entiers qu on lui passe en parametre

def somme(liste):
    somme_dejas_calculee = 0
    for i in liste:
        somme_dejas_calculee = somme_dejas_calculee + i
    return somme_dejas_calculee
liste = [1,8,5,4,3]    
print(somme(liste))

def somme_entiers_optionnels(*mes_entiers):
	somme = 0
	for i in range(0, len(mes_entiers)):
		somme = somme + mes_entiers[i]
	return somme
ma_somme = somme_entiers_optionnels(1, 5, 5)
print(ma_somme)



