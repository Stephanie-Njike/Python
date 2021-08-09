##### 04.02.2021


### Exo :

"""
Prendre 5 modules de python. Pour chaque module, trouver 5 fonctions,
ensuite donner un exple d utilisation de chaque module.
"""
        #   https://docs.python.org/fr/3/library/datetime.html
        #   https://www.pierre-giraud.com/python-apprendre-programmer-cours/module-datetime-time-calendar/
import os  
user = os.getlogin()    # os.getlogin() : renvoie le nom d'utilisateur courant
print(user)             # imprime le nom d'utilisateur

#import os
#os.mkdir("c:/fichier")  # crée un dossier nommé myFolder sur le disque C:\

import os
rep_actuel = os.getcwd()# os.getcwd() : renvoie le répertoire actuel sous forme de chaîne de caractères.
print(rep_actuel)       # renvoie le répertoire actuel


## - La méthode os.path:
"""
Afin de pouvoir utiliser la méthode os.path, il faut préalablement importer
le module pathlib. Le module pathlib est un module doté d'une interface
orientée objet inclus dans python depuis la version 3.4 doté de méthodes très
intuitives permettant d'interagir avec le système de fichiers d'une façon simple
et conviviale.
"""

# La méthode os.path.exist() permet de tester si un répertoire existe ou non

import os  
from pathlib import Path
print(os.path.exists("c:/users/"))     #affiche True

#---------------------------
# On peut aussi utiliser
print(not os.path.exists("c:/users/")) #affiche False


# Pour tester la nature d'un chemin s'il s'agit d'un répertoire ou un fichier on utilise les méthodes is_dir() et is_file():

import os 
from pathlib import Path 
myDirectory = "C:/Users" 
p = Path(myDirectory) 
print(p.is_dir())                      # affiche True
print(p.is_file())                     # affiche False





import datetime
# classe date

d = datetime.date(2020,2,3)            # cree un objet date avec la date specifiee
print(d)

y = d.year                             # renvoie l annee de l objet d
print(y)

dT = datetime.date.today()             # renvoie un objet date avec la date d aujourd hui
print(dT)

# classe time

t = datetime.time(17,28,5)            # cree un objet time avec le temps specifie
print(t)

h = t.hour                            # renvoie l heure de l objet t
print (h)

mi = t.minute                         # renvoie les minutes de l objet t
print(mi)

# classe datetime

dTime = datetime.datetime(2020,2,3,17,28,5)
print(dTime)                         # cree un objet datetime avec la date specifiee

dTimeToday = datetime.datetime.today()
print(dTimeToday)                    # renvoie un objet datetime avec la date d aujourd hui
   # ou
dTimeToday = datetime.datetime.now() # renvoie un objet datetime avec la date d aujourd hui




import calendar

# creer un calendrier texte 
c = calendar.TextCalendar(calendar.MONDAY)
cm = c.formatmonth(2030,2)
print(cm)

# creer un calendrier HTML
hc = calendar.HTMLCalendar(calendar.MONDAY)
cm = hc.formatmonth(2030,2)
print(cm)



from Les_fonctions_natives_ou_integrees import *
# import Les_fonctions_natives_ou_integrees

print(random.randint(1,11))

x = [1,2,3,4,5]
random.shuffle(x)                  ####?????? pourquoi excute t il toute le code du fi
print(x)                           # chier

print( random.choice([1,2,3,4,5]))


