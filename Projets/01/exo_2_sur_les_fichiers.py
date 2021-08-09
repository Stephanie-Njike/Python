#### 28.01.2021

### Exo du livre Apprendre a programmer avec Python 3 page 114


## Exo 1 :
"""
Écrivez un script qui permette de créer et de relire aisément un fichier texte. Votre
programme demandera d’abord à l’utilisateur d’entrer le nom du fichier. Ensuite il lui
proposera le choix, soit d’enregistrer de nouvelles lignes de texte, soit d’afficher le contenu du
fichier.
L’utilisateur devra pouvoir entrer ses lignes de texte successives en utilisant simplement la
touche <Enter> pour les séparer les unes des autres. Pour terminer les entrées, il lui suffira
d’entrer une ligne vide (c’est-à-dire utiliser la touche <Enter> seule).
L’affichage du contenu devra montrer les lignes du fichier séparées les unes des autres de la
manière la plus naturelle (les codes de fin de ligne ne doivent pas apparaître)
"""
"""
nom_fichier = input( 'entrer le nom du fichier texte : ')
print ( ' le nom du fichier texte est : ', nom_fichier)

mode_douverture = input('veuillez choisir w ou r comme mode d ouverture : ')
print( 'votre mode d ouverture est : ', mode_douverture)

if (mode_douverture == 'w') or (mode_douverture == 'W'):
    ofi1 = open(nom_fichier, mode_douverture)
    while 1:
        ligne = input('Entrer une ligne de texte')
        if ligne == '':
            break
        else :
            ofi1.write(ligne + '\n')
    ofi1.close()
elif (mode_douverture == 'r') or (mode_douverture =='R'):
    ofi2 = open(nom_fichier, mode_douverture)
    while 1 :
        ligne = ofi2.readline()
        print(ligne)
        if ligne == '':
            print('soit ce fichier est vide, soit il est a sa fin')
            break
    ofi2.close()
    
    
else:
    print( 'veuillez choisir a, w ou r comme mode d ouverture : ')
"""


### exercice ameliore
"""
nom_fichier = input( 'entrer le nom du fichier texte : ')
print ( ' le nom du fichier texte est : ', nom_fichier)

mode_douverture = input('veuillez choisir a,w ou r comme mode d ouverture : ')
print( 'votre mode d ouverture est : ', mode_douverture)

option_ouverture_Ecriture = ['a', 'A', 'w', 'W']

if mode_douverture in option_ouverture_Ecriture:
    ofi1 = open(nom_fichier, mode_douverture)
    while 1:
        ligne = input('Entrer une ligne de texte')
        if ligne == '':
            break
        else :
            ofi1.write(ligne + '\n')
    ofi1.close()

elif (mode_douverture == 'r') or (mode_douverture == 'R'):
    ofi2 = open(nom_fichier, mode_douverture)
    fichierVide = True
    while 1 :
        ligne = ofi2.readline()
        print(ligne)
        if ligne != '':
            fichierVide = False
         if ligne == '':
             break
    if fichierVide:
        print('Le fichier est vide')
    else:
        print('La lecture du fichier est termine')
    ofi2.close()

else:
    print( 'veuillez choisir a, w ou r comme mode d ouverture : ')
"""

# Exo 2:
"""
Prendre  un fichier qui contient dejas un texte et rechercher certains
mots dans ce fichier
"""

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
while 2 :
        phrase = nouveaufichier.readline()
        numeroLigne = numeroLigne + 1
        liste_de_mots = phrase.split(' ')
        if 'de' in liste_de_mots:
            print('ligne = ', numeroLigne, ' position dans la ligne = ', liste_de_mots.index('de'))
            print(phrase)
        if phrase == '':
            break
nouveaufichier.close()
"""


# Exo 2 Correction:
"""
Prendre  un fichier qui contient deja un texte et recherche un mot pris au clavier dans ce fichier. 
Le programme retourne toutes les positions du mot.
"""

def allPosition(numeroLigne, liste, elt):
    for i in range(len(liste)):
        if liste[i] == elt:
            print('(',numeroLigne, ', ', i+1, ')')
"""
numeroLigne = 0
myfile = open('myfile.txt','w')
while 1 :
    # Entrer une ligne du fichier
    ligne = input ('veuiller entrer vos textes svp : ')
    if ligne == '':
        break
    else :
    	# Ajouter cette ligne dans le fichier
        myfile.write(ligne + ' \n')
myfile.close()
# On invite l'utilisateur a entrer le mot que nous souhaitons retouner les positions
mot_a_chercher = input('veuiller entrer le mot a chercher : ')
# Cette variable indique si on a trouver le mot dans le fichier ou pas
trouverMot = False 
# Ouverture du fichier
myfile = open('myfile.txt','r')
while 2 :
    ligne = myfile.readline()
    numeroLigne = numeroLigne + 1
    # Convertir une ligne du fichier en tableau avec la methode split()
    liste_a_partir_de_la_ligne = ligne.split(' ')
    # Verifier si le mot est dans une ligne du fichier
    if mot_a_chercher in liste_a_partir_de_la_ligne:
    	# Affichage des positions du mot dans le fichier
        allPosition(numeroLigne, liste_a_partir_de_la_ligne, mot_a_chercher)
        print(ligne)
        trouverMot = True
    if ligne == '':
        break
if trouverMot == False:
    print('Le mot rechercher n\'est pas dans le fichier')
# Fermeture du fichier
myfile.close()

"""
        
        
    




