print('Gestion des erreurs')

try:
    resultat = 15/0
    print('le resultat', resultat)
except:
    print('il y a erreur a ce niveau')



try:
    resultat = 15/0
    print('le resultat', resultat)
    
except NameError:
    print('Le nom de la variable n\'est pas defini')

except ZeroDivisionError:
    print('Impossible de diviser un nombre par zero')

except TypeError:
    pass

finally:
    print('les instructions vont toujours s\'executees')



