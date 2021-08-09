import os
# EXERCICE 1

def table_multiplication(mul,borninf,bornsup):
    i = borninf
    for i in range (borninf,bornsup+1):
        reponse = mul * i
        
        print(mul, "* ",i, "= ", reponse)



def table_multiplication(mul,borninf,bornsup):
    i = borninf
    for i in range (borninf,bornsup + 1):
        print(i," * ",mul, " = ", i*mul)
        


# OU

def table_multiplication(mul, bornInf, bornSup):
    i = bornInf
    while (i <= bornSup):
        print(i, ' * ', mul, ' = ', i*mul)
        i = i + 1



#ou

def table_multiplication(mul,borninf,bornsup):
    while borninf <= bornsup:
        print(mul, "* ",borninf, "= ", mul*borninf)
        borninf+=1


# EXERCICE 2
"""
- Ecrire une fonction cube qui retourne le cube de son argument"""

def cube(nbre):
    return nbre**3



"""
- Tester la fonction volumeSphere par un appel dans le programme principal"""

def volumeSphere(r):
    return (4/3)*3.14*cube(r)
v = volumeSphere(3)
#print(v)




# EXERCICE 3
"""
- Ecrire une fonction triangle en langage Python qui prend en paramètre une
entier (n) et permet d'afficher un triangle isocèle formé d'étoile(*).
"""



def triangle1(n):
    nombre_espace_gauche = n
    nombre_chiffre_milieu = 1
    nombre_espace_droit = n
    for i in range(1,n):
        for j in range (nombre_espace_gauche):
            print(' ', end ='')
        for k in range (nombre_chiffre_milieu):
            print(i, end ='')
        for l in range (nombre_espace_droit):
            print(' ', end ='')
            
        print(' => ',i)
        nombre_espace_gauche = nombre_espace_gauche - 1
        nombre_chiffre_milieu = nombre_chiffre_milieu + 2
        nombre_espace_droit = nombre_espace_droit - 1
    return " "





# EXERCICE 4


def maximum(nb1,nb2,nb3):
    max1 = nb1
    if nb1 > nb2 and nb1 > nb3:
        max1 = nb1
    if nb3 > nb1 and nb3 > nb2:
        max1 = nb3
    else:
        max1 = nb2
    return max1


# EXERCICE 5

def triangle2(n):
    for i in range(n):
        print(str(' ')*(n-i), end='')
        print(str(i) * (i*2))
    return " "


# OU

def triangleNewMethod(n):
    espace = n
    etoile = 2
    valeur = 1
    for i in range(n):
        if valeur < n:            
            print(' '*espace, str(valeur)*etoile, ' '*espace)
            espace = espace - 1
            etoile = etoile + 2
            valeur = valeur + 1


# OU

def triangleNewMethod(n):
    espace = n
    etoile = 2
    valeur = 1
    for i in range(1,n):
        print(' '*espace, str(valeur)*etoile, ' '*espace)
        espace = espace - 1
        etoile = etoile + 2
        valeur = valeur + 1


# OU

def triangle(n):
    nombre_espace_gauche = n
    nombre_etoiles_milieu = 2
    nombre_espace_droit = n
    for i in range(1,n):
        for j in range (nombre_espace_gauche):
            print(' ', end ='')
        for k in range (nombre_etoiles_milieu):
            print(i, end ='')
        for l in range (nombre_espace_droit):
            print(' ', end ='')
    
        print(" ")
        nombre_espace_gauche = nombre_espace_gauche - 1
        nombre_etoiles_milieu = nombre_etoiles_milieu + 2
        nombre_espace_droit = nombre_espace_droit - 1
    return " "
       




# EXERCICE 6

def chiffre_porte_bonheur (nb):

    resultat = nb
    print("Nombre de depart:", nb)

    while resultat > 10:
        str_result = str(resultat)
        somme = 0
        for i in range(len(str_result)):
            elt1 = int(str_result[i])
            
            print(elt1, "^2 =", elt1**2) 
            somme = somme + elt1**2
                      
        resultat = somme
        print("Nouveau:", resultat)    
                 
    if resultat == 1:
        print("le chiffre ", nb, " est un porte bonheur")
    else:
        print ("le chiffre ", nb, " n'est pas un porte bonheur")
            

# OU

def chiffre_porte_bonheur (nb):
    nouveau = nb
    while nouveau >= 10:
        resultat = str(nouveau)
        somme = 0
        for i in range(len(resultat)):
            chiffre = int(resultat[i])
            
            print(chiffre,"**2 = ",chiffre**2)
            somme = somme + chiffre**2

            nouveau = somme
            print(somme)
    if nouveau == 1:
        print("le chiffre ", nb, " est un chiffre porte bonheur")
    else:
        print ("le chiffre ", nb, " n'est pas un chiffre porte bonheur")




# EXERCICE 7

def compte_mot(phrase):
     
    for mots in phrase:
        liste_mot = phrase.split(' ')
        nombre_mot = len(liste_mot)
    return nombre_mot


# EXERCICE 9


def update_score(current,value):
    current +=value
    return current

# EXERCICE 10


def get_name(): pass

def calc_calories(a,b): pass
    

# EXERCICE 11

def mot_de_passe(char):
    return len(char)


# OU

def mot_de_passe(char):
    nb_total_caractere = char
    for i in  char :
        nb_total_caractere = len(char)
    return nb_total_caractere



def NbCMin(passe):
    return sum([int(i.islower()) for i in passe])


def NbCMaj(passe):
    return sum([int(i.isupper()) for i in passe])


def NbcAlpha(passe):
    return len(passe)-NbCMaj(passe)-NbCMin(passe)


# ou


def mot_de_passe(char):
    nb_total_caractere = char
    for i in  char :
        nb_total_caractere = len(char)
    return nb_total_caractere
print(mot_de_passe('aztrAzENEka@.202101/a'))

def NbCMin(passe):
    nb = 0
    for i in passe:
        if 'a' <= i <= "z":
            nb +=1
    return nb
print(NbCMin('aztrAzENEka@.202101/a'))

def NbCMaj(passe):
    nb = 0
    for i in passe:
        if 'A' <= i <= "Z":
            nb +=1
    return nb
print(NbCMaj('aztrAzENEka@.202101/a'))

def NbcAlpha(passe):
    return len(passe)-NbCMaj(passe)-NbCMin(passe)
print(NbcAlpha('aztrAzENEka@.202101/a'))

def LongMaj(passe):
    d = 0
    s = 0
    i = 0
    while i < len(passe):
        if 'A' < passe[i] < 'Z':
            s +=1
        else:
            if s > d:
                d = s
                s = 0
        i +=1
    return d

                 
        

def LongMin(passe):
    d = 0
    s = 0
    i = 0
    while i < len(passe):
        if 'a' < passe[i] < 'z':
            s +=1
        else:
            if s > d:
                d = s
                s = 0
        i +=1
    return d


def Score(passe):
    
    b1 = len(passe)*4
    b2 = (len(passe) - NbCMaj(passe))*2
    b3 = (len(passe) - NbCMin(passe))*3
    b4 = NbcAlpha(passe)*5
    somme_bonus = b1 + b2 + b3 + b4
    p1 = LongMin(passe)*2
    p2 = LongMaj(passe)*3
    somme_penalite = p1 + p2
    score_final = somme_bonus - somme_penalite
    return score_final









table_multiplication(4,5,20)
table_multiplication(4,5,20)
table_multiplication(7, 10, 25)
table_multiplication(mul=int(input("saisir le nombre multiplicateur : ")),
borninf = int(input("saisir la borne inferieure : ")),
bornsup = int(input("saisir la borne superieure : ")))
print(cube(5))
print(volumeSphere((4/3)*3.14*cube(3)))
print(triangle1(n = int(input("saisir la hauteur du triangle : "))))
print(maximum(nb1 = int(input("saisir le premier nombre : ")),
nb2 = int(input("saisir le deuxieme nombre : ")),
nb3 = int(input("saisir le troisieme nombre : "))))
print(triangle2(10))
triangleNewMethod(n = int(input("saisir la hauteur du triangle : ")))
triangleNewMethod(n = int(input("saisir la hauteur du triangle : ")))
print(triangle(n = int(input("saisir la hauteur du triangle : "))))
chiffre_porte_bonheur(912)
print(chiffre_porte_bonheur (nb = int(input("saisir le nombre : "))))
print(compte_mot(phrase = str(input("saisir la phrase: "))))
print(mot_de_passe('aztrAzENEka@.202101/a'))
print(mot_de_passe(char = str(input("saisir le mot de passe: "))))
print(NbCMin('aztrAzENEka@.202101/a'))
print(NbCMaj('aztrAzENEka@.202101/a'))
print(NbcAlpha('aztrAzENEka@.202101/a'))
print(LongMaj('aztrAzENEka@.202101/a'))
print(LongMin('aztrAzENEka@.202101/a'))
print(Score('aztrAzENEka@.202101/a'))



os.system("pause")
