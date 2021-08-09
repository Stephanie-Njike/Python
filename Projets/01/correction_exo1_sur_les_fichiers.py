#### 30.01.2021

# Exo 1 :

"""
Prendre  un fichier qui contient deja un texte et recherche un mot pris au clavier dans ce fichier. 
Le programme retourne toutes les positions du mot.
"""

print( 'Puisque je n ai pas encore de fichier contenant un texte,')
print('je prefere me creer d abord un fichier et y introduire des textes')
numeroLigne = 0
nouveaufichier = open('monDeuxiemeFichier.txt','w')
while 2 :
    ligne = input ('veuiller entrer vos textes svp : ')

    if ligne == '':
        break
    else :
        nouveaufichier.write(ligne + '\n')

nouveaufichier.close()

print('Maintenant que le fichier texte (mondeuxiemeFichier)contient des ')
print('sequences de chaines de caracteres, je peux faire mes recherches')
nouveaufichier = open('monDeuxiemeFichier.txt','r')
mot_a_chercher = input('veuillez entrer le mot a chercher : ')
while 2 :
        phrase = nouveaufichier.readline()
        numeroLigne = numeroLigne + 1
        liste_de_mots = phrase.split(' ')
        #if mot_a_chercher in liste_de_mots:
        r = ( (numeroLigne, i) for i,m in enumerate(liste_de_mots) if m == mot_a_chercher)
        """
        for i,m in enumerate(liste_de_mots):
            if m == mot_a_chercher:
            
        """
        #print('ligne = ', numeroLigne, ' position dans la ligne = ', liste_de_mots.index(mot_a_chercher))
        print(list(r))
        print(phrase)
        if phrase == '':
            break
if trouverMot == False:
    print('Le mot rechercher n\'est pas dans le fichier')
    
nouveaufichier.close()

