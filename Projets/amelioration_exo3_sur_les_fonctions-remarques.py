# Exercice 3:

  #  Qu'affiche le programme suivant ?

def f(x):
    return 100*x-4*x**2+2

print(f(2))

     # Elle affichera la valeur de la fonction f(x) quand x = 2 ( 100*2-(4*2^2)+2 )
     # 186

  #  Écrire un programme qui affiche les valeurs f(x) pour tous les nombres entiers x entre 0 et 20 (utiliser une boucle for ...).

def affiche_f_de_x():
    for x in range (0,21):
        print(f(x))
affiche_f_de_x()

  #  Modifier le programme précédent pour qu'il trouve et affiche le maximum de la fonction f, et la valeur de x correspondante.

def affiche_f_de_x():
    # retirer x=0
    x = 0
    # retirer print(f(x))
    print(f(x))

    xmaximum = 0
    fmax = 0
    
    for x in range (0,20):
        # retirer x=x+1
        x = x + 1               
        print(f(x))
        if f(x) > fmax:
            fmax = f(x)
            xmaximum = x
    return(fmax,xmaximum)
print(affiche_f_de_x())


          ### Ou

def affiche_f_de_x():
    # retirer x=0
    x = 0
    # retirer print(f(x))
    print(f(x))
    
    lf = []
    # retirer lf.append(f(x))
    lf.append(f(x))
    # fmax = 0, c'est simple comme ceci
    fmax = lf[0]
    xmaximum = 0
    
    for x in range (0,20):
        # retirer x=x+1
        x = x + 1
        print(f(x))
        if f(x) > fmax:
            fmax = f(x)
            xmaximum = x
        lf.append(f(x))
    return(fmax,lf.index(fmax))
print(affiche_f_de_x())
