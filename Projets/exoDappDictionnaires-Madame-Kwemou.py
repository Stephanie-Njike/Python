# Exo d'application sur les dictionnaires :

# Ecrire un programme qui evalue un eleve ou un candidat
 # -- Indications :
 # .le programme va creer un dictionnaire avec les questions et les reponses .
 # .Quand on lance le programme, il affiche une question qu il choisit aleatoirement dans le dictionnaire.
 # .Et l utilasateur va entrer la reponse et apres va dire a l utilisteur si sa reponse est vrai ou fausse.
 # .Enfin le programme demande a l utilisateur: Voulez vous continuer avec les questions ? taper 'o'pour oui et 'n' pour non.

# faire toutes les importations ici
# import random
evaluationDELEleve = {}
evaluationDELEleve['Comment tu t appelles?'] = 'Stephanie'
evaluationDELEleve['Quelle age avez vous?'] = '18 ans'
evaluationDELEleve['Quelle est votre nationalite?'] = 'Camerounaise'
print('l evaluation de l eleve est :' ,evaluationDELEleve)

import random
for i in range (3):
    maCleListe = random.sample(evaluationDELEleve.keys(), 1)
    maCle = maCleListe[0]
    print(maCle)
    reponse = input('entrer la reponse : ')
    print(reponse)

    if reponse == evaluationDELEleve[maCle]:
        # print('Bonne reponse')
        print('O')
    else:
        # print('Mauvaise reponse')
        print('N')

    instruction = 'Voulez vous continuer de repondre aux questions?'
    print(instruction)
    recommandation = input('tapez o pour oui ou n pour non : ')
    print( recommandation)
    if recommandation == 'o':
        continue
    else:
       break


