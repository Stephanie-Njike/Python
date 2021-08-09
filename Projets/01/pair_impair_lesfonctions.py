##13.01.21

# Exercice:
"""
 pair_impair.py : écrire 2 fonctions :
— pair (nbre), qui renvoie True, si le nombre est Pair
— impair (nbre), qui renvoie True, si le nombre est Impair
Le nombre sera demandé à l’utilisateur. Le résultat attendu est : "La fonction Pair retourne True
pour la valeur 2"

"""


def mon_nombre_pair(mon_nombre):
    if mon_nombre % 2 == 0 :
      return True
    else :
      return False

def mon_nombre_impair(mon_nombre):
    if mon_nombre % 2 != 0 :
        return True
    else :
        return False

mon_nombre = input('Veuiller entrer un nombre: ')
mon_nombre = int(mon_nombre)

valeur_de_retour = mon_nombre_pair(mon_nombre)
valeur_de_retour2 = mon_nombre_impair(mon_nombre)

print('la fonction pair retourne', valeur_de_retour, 'pour la valeur', mon_nombre)
print('la fonction impair retourne', valeur_de_retour2, 'pour la valeur', mon_nombre)

