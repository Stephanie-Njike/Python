# print('ecrire le resultat de l\'execution du programme dans un fichier')

"""
fichier = open('monFichier.txt', 'a')
nbre1 = input('entrer le premier nombre\n ')
nbre2 = input('entrer le deuxieme nombre\n ')
fichier.write('\nLe premier nombre est : ' + nbre1)
fichier.write('\nLe deuxieme nombre est : ' + nbre2)
somme = int(nbre1) + int(nbre2)
print('La somme des deux nombres est : ', somme)
fichier.write('\nLa somme des deux nombres est : ' + str(somme))
fichier.close()
"""

"""
fichier = open('fichiers/monfichier.txt', 'r')
print(fichier.readline())
print(fichier.readline())
print(fichier.readline())
print(fichier.readline())
print(fichier.readline())
print(fichier.readlines()[2])
fichier.close()
"""
"""
fichier = open('monFichier.txt', 'w')
fichier.write('Mon premier fichier\n')
fichier.write('Mon premier fichier deuxieme ligne\n')
nombre = 25
fichier.write('Ma variable = ' + str(nombre)+ '\n')
fichier.close()
"""
"""
fichier = open('monFichier.txt', 'r')
print(fichier.readline())
print(fichier.readline())
fichier.close()
"""

with open("monFichier.txt")as fichier:
    data = fichier.readlines()[8]
    print(data.split(' ')[-1])
       

