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
fichier = open('mondevoirsurlesfichiers.txt', 'a')
reponseJuste = 2
reponseFausse = 0
pointsGagnes = []
recommandation = 'o'
while recommandation != 'n':
    maCleListe = random.sample(evaluationDELEleve.keys(), 1)
    maCle = maCleListe[0]
    print(maCle)
    fichier.write('\n'+ maCle)  
    reponse = input('entrer la reponse : ')
    print(reponse)
    fichier.write('\n'+ reponse) 
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

fichier.close()
