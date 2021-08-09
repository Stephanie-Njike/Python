# Exo d'application sur les dictionnaires :

# Ecrire un programme qui evalue un eleve ou un candidat
 # -- Indications :
 # .le programme va creer un dictionnaire avec les questions et les reponses .
 # .Quand on lance le programme, il affiche une question qu il choisit aleatoirement dans le dictionnaire.
 # .Et l utilasateur va entrer la reponse et apres va dire a l utilisateur si sa reponse est vrai ou fausse.
 # .Enfin le programme demande a l utilisateur: Voulez vous continuer avec les questions ? taper 'o'pour oui et 'n' pour non.

"""evaluationDELEleve = {}
evaluationDELEleve['Comment tu t appelles?'] = 'Stephanie'
evaluationDELEleve['Quelle age avez vous?'] = '18 ans'
evaluationDELEleve['Quelle est votre nationalite?'] = 'Camerounaise'
print('l evaluation de l eleve est :' ,evaluationDELEleve)
import random
for i in range (3):
    maCleListe = random.sample(evaluationDELEleve.keys(),1)
    maCle = maCleListe[0]
    print(maCle)
    reponse = input('entrer la reponse : ')
    print(reponse)

    if reponse == evaluationDELEleve[maCle]:
        print('O')
    else:
        print('N')

    instruction = 'Voulez vous continuer de repondre aux questions?'
    print(instruction)
    recommandation = input('tapez o pour oui ou n pour non : ')
    print( recommandation)
    if recommandation == 'o':
        continue
    else:
       break
"""
# Methode while

import random
evaluationDELEleve = {}
evaluationDELEleve['Comment vous vous appellez?'] = 'Stephanie'
evaluationDELEleve['Quelle age avez vous?'] = '18 ans'
evaluationDELEleve['Qu est ce qui vous rend plus heureux a l ecole?'] = 'Les retrouvailles'
evaluationDELEleve['Qu est ce qui vous rend mal a l aise a l ecole?'] = 'Les disputes'
evaluationDELEleve['Quelle sont vos objectifs a atteindre a la fin d annee?'] = 'Reussir a mon examen'
evaluationDELEleve['comment te sens tu quand tu commets une faute ou une erreur?'] = 'tres gene'
evaluationDELEleve['Quelle est votre meilleur amie?'] = 'Patricia'
evaluationDELEleve['Qui vous aide le plus a atteindre tes objectifs?'] = 'Papa et Maman'
evaluationDELEleve['Que dois je faire pour vous aider?'] = 'En m aidant a m ameliorer '
evaluationDELEleve['Avez vous dejas connu un echec?'] = 'oui'

print('l evaluation de l eleve est :' ,evaluationDELEleve)

i = 0
reponseJuste = 2
reponseFausse = 0
pointsGagnes = []
# Correction: Ajouter les deux lignes ci-dessous   
recommandation = 'o'
while recommandation != 'n':
# Correction  retirer i < 10   
# while i < 10:
    # Correction: enlever i = i + 1
    #  i = i + 1
    maCleListe = random.sample(evaluationDELEleve.keys(), 1)
    maCle = maCleListe[0]
    print(maCle)  
    reponse = input('entrer la reponse : ')
    print(reponse) 
    if reponse == evaluationDELEleve[maCle]:
        print('Bonne reponse vous avez gagne', reponseJuste,'points')
        pointsGagnes.append(reponseJuste)
        print(pointsGagnes)
    else:
        print('Mauvaise reponse, dommage vous obtenez', reponseFausse,'point')
        pointsGagnes.append(reponseFausse)
        print(pointsGagnes)
        
    sommeTotale = sum(pointsGagnes)
    print('Vous avez obtenu une somme totale de ', sommeTotale,'points')
    instruction = 'Voulez vous continuer de repondre aux questions?'
    print(instruction)
    recommandation = input('tapez o pour oui ou n pour non : ')
    print(recommandation)
    
    """
    Vous n'avez plus besoin de ce block
    if recommandation == 'o':
        continue
    else:
        break
    """

"""
# Madame voici la version amelioree de votre programme

import random
evaluationDELEleve = {}
evaluationDELEleve['Comment vous vous appellez?'] = 'Stephanie'
evaluationDELEleve['Quelle age avez vous?'] = '18 ans'
evaluationDELEleve['Qu est ce qui vous rend plus heureux a l ecole?'] = 'Les retrouvailles'
evaluationDELEleve['Qu est ce qui vous rend mal a l aise a l ecole?'] = 'Les disputes'
evaluationDELEleve['Quelle sont vos objectifs a atteindre a la fin d annee?'] = 'Reussir a mon examen'
evaluationDELEleve['comment te sens tu quand tu commets une faute ou une erreur?'] = 'tres gene'
evaluationDELEleve['Quelle est votre meilleur amie?'] = 'Patricia'
evaluationDELEleve['Qui vous aide le plus a atteindre tes objectifs?'] = 'Papa et Maman'
evaluationDELEleve['Que dois je faire pour vous aider?'] = 'En m aidant a m ameliorer '
evaluationDELEleve['Avez vous dejas connu un echec?'] = 'oui'

print('l evaluation de l eleve est :' ,evaluationDELEleve)

i = 0
reponseJuste = 2
reponseFausse = 0
pointsGagnes = []
recommandation = 'o'
while recommandation != 'n':
    maCleListe = random.sample(evaluationDELEleve.keys(), 1)
    maCle = maCleListe[0]
    print(maCle)  
    reponse = input('entrer la reponse : ')
    print(reponse) 
    if reponse == evaluationDELEleve[maCle]:
        print('Bonne reponse vous avez gagne', reponseJuste,'points')
        pointsGagnes.append(reponseJuste)
        print(pointsGagnes)
    else:
        print('Mauvaise reponse, dommage vous obtenez', reponseFausse,'point')
        pointsGagnes.append(reponseFausse)
        print(pointsGagnes)
        
    sommeTotale = sum(pointsGagnes)
    print('Vous avez obtenu une somme totale de ', sommeTotale,'points')
    instruction = 'Voulez vous continuer de repondre aux questions?'
    print(instruction)
    recommandation = input('tapez o pour oui ou n pour non : ')
    print(recommandation)

"""
