import os
from random import*

question = {}
question[0]='quelle est la capitale du Cameroun?'
question[1]='un'
question[2]='deux'
question[3]='trois'
question[4]='quatre'
question[5]='cinq'
question[6]='six'
question[7]='sept'
question[8]='huit'
question[9]='neuf'
question[10]='dix'

reponse = {}
reponse[0]='Yaoundé'
reponse[1]='1'
reponse[2]='2'
reponse[3]='3'
reponse[4]='4'
reponse[5]='5'
reponse[6]='6'
reponse[7]='7'
reponse[8]='8'
reponse[9]='9'
reponse[10]='10'


print('l\'exercice de l\'élève est le suivant:')


total_des_questions = 0
note = 0
reponse2='O'

while reponse2 == 'O':
    total_des_questions = total_des_questions + 1
    question_aléatoire = randrange(10)
    print('Quelle est la valeur en chiffre de: ', question[question_aléatoire])
    reponse_de_lélève = input('entrez une reponse: ')

    if reponse_de_lélève == reponse[question_aléatoire ]:
        print('Bonne reponse')
        note = note + 2
        print(note,'points')
    else:
        print('Mauvaise reponse')
        

    reponse2 = input('Voulez vous continuer: ')
print('nombre de questions repondues: ',total_des_questions)
print('note/20: ',note)



"""
Ecrire un programme qui prend un nombre entier n au clavier et affiche une
liste des puissances comme suit : [n, n2, n4, n8, n16, …]. La taille de la
liste à afficher est de 5.
"""

# J'ai commante la suite 
"""
reponse3 = int(input('entrez un NOMBRE: '))
puissance = 1
compter = 1
resultat1 = 0

while compter <= 5 :
    compter = compter + 1
    
    resultat1=reponse3**puissance
    print('puissance = ', puissance, 'resultat = ', resultat1)
    puissance = puissance*2
"""
    
        
    
      
        

   
'''
from random import*

evaluationDELEleve = {}
evaluationDELEleve['Comment tu t appelles?'] = 'Stephanie'
evaluationDELEleve['Quelle age avez vous?'] = '18 ans'
evaluationDELEleve['Quelle est votre nationalite?'] = 'Camerounaise'
print('l evaluation de l eleve est :' ,evaluationDELEleve)
for i in range (3):
    maCleListe = random.sample(evaluationDELEleve.keys(), 1)
    maCle = maCleListe[0]
    print(maCle)  
    reponse = input('entrer la reponse : ')
    print(reponse) 
    if reponse == evaluationDELEleve[maCle]:
        print('Bonne reponse')
    else:
        print('Mauvaise reponse')
    instruction = 'Voulez vous continuer de repondre aux questions?'
    print(instruction)
    recommandation = input('tapez o pour oui ou n pour non : ')
    print( recommandation)
    if recommandation == 'o':
        continue
    else:  
        break  
'''
os.system ("pause")
 
