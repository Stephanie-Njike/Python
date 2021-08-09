### 14.01.2021


### Les Fonctions Predefinies : Ce sont des fonctions integrees(builtin) a python


## abs(x) : Retourne la valeur absolu.
a = abs(-1)
print(a)


## all(iterable) : Retourne True si tous les éléments d'un élément itérable sont True
liste = [True,1,True, 2, 3]
print(all(liste))                   ###?????? oui c est vrai, mais comment on fait pour savoir que c est vrai


## any(iterable): Retourne True si au moins un élément d'un élément itérable est True 
liste = [True,False, True]
print(any(liste))                   ##????? oui la liste a ses elts qu elle contient. ca signifit que tt ces elts lui
                                          # appartient. MAIS comment pouvont ns savoir ici kelle contient au moins un elt
                                          #vrai ou faux ?
                           
def hello():
    return 'hello  World!'

## callable(object): Determine si un objet est callable .
print(callable("A"))
 #ici A n est pas callable          ###????? estce pour voir si un objet est en fait dejas un builtin a python ?
print(callable(int))
print(callable(all))
print(callable(bin))
print(callable(any))
print(callable(hello))
 #ici int est callable


##  str.capitalize(): La méthode capitalize permet de mettre une chaine de caractères au format Xxxxx
b = "oLIviER".capitalize()
print(b)
 # ca executera : 'Olivier'

##  str.islower() : Retoune True si tous les caractères sont en minuscule.
print("olivier".islower())
 # retournera True
print("Olivier".islower())
 # retournera False


## str.isupper(): Retourne True si tous les caractères sont en majucule et qu'il y a au moins un caractère.
print("OLIVIER".isupper())
 # retournera True
print("Olivier".isupper())
 # retournera False
print("OlivieR".isupper())
 # retournera False
 

##  str.lower(): La méthode lower permet de mettre en minuscule une chaine de caractères.

print("OLIVIER".lower())
 # le resultat c est 'olivier'
 

##  upper()La méthode upper permet de mettre en majuscule une chaine de caractères.

print("olivier".upper())
 # le resultat c est'OLIVIER'

 
##  str.isspace(): Retoune True si il n'y a que des espaces.
print(" ".isspace())
 # retourne True
print("jean louis".isspace())         ####???? entre jean louis il ya un espace et au moins un caractere 
 # retourne False                            # pourquoi retourne t il false donc?
print("    ".isspace())
 # retourne True

##  str.title(): Transforme la chaine dans un format title.

print("Ceci est un titre".title())
 # 'Ceci Est Un Titre' s affichera



## str.istitle(): Retourne True si la chaine a un format titre.

print("Titre".istitle())
 # retourne True
print("TitrE".istitle())
 # retourne False
print("Titre de mon site".istitle())
 # retourne False
print("Titre De Mon Site".istitle())
 # retourne True


##  str.isalnum():Retoune True si tous les caractères sont alphanumériques et qu'il y a au moins
                 #un caractère. Sinon False.
         
print("25".isalnum())
 # retournera True
print("25b".isalnum())
 # retournera True
print("25bé".isalnum())
 # retournera True
print("25bé@".isalnum())     ####???? c est quoi un caractere alphanumerique?
 # retournera False
print("-".isalnum())
 # retournera False
print("_".isalnum())
 # retournera False
print("".isalnum())
 # retournera False

##  str.isalpha(): Retourne True si tous les caractères sont des lettres et qu'il y a au moins
                 # un caractère. Sinon False

print("x".isalpha())
 # retournera True
print("-".isalpha())
 # retournera False
print("12".isalpha())
 # retournera False
print("jean-claude".isalpha())          ####????? est ce parce que c est un mot que ns avons false?
 # retournera False                             # ce mot est pourtant constitue de lettres!?
print("jean claude".isalpha())
 # retournera False
print("élise".isalpha())
 # retournera True

##  str.isdigit() : Retourne True si tous les caractères sont numériques et
                  # qu'il y a au moins un caractère. Sinon False.

print("1".isdigit())
 # retournera True
print("1.5".isdigit())
 # retournera False
print("1,5".isdigit())
 # retournera False
print("3b".isdigit())                  ####???? pourquoi print("3b".isdigit()) retourne false? 
 # retournera False                           # pourtant il contient au moins un caractere numerique , 3.
print(" ".isdigit())
 # retournera False


##  str.replace(string, string):La méthode replace remplace un segment d'une chaine de caractères par une autre.

print("olivier".replace("i", "a"))
 #'olavaer' s affiche



##  str.count(string) : La méthode count compte le nombre d'occurences de la recherche demandée.
print("olivier".count("i"))


##  str.endswith(str) : La méthode endswith teste si une chaine de caractères se termine
                       #par la chaine demandée
a = "olivier"
print(a.endswith("r"))
 # ca va executer True
print( a.endswith("er"))
 # ca va executer True
print(a.endswith("é"))
 # ca va executer False



##  str.startswith(prefix[, start[, end]]):Retourne True si la chaine commence par le préfix indiqué.
                                          #Ce préfix peut être un tuple. Les paramètres start et end (optionnel)

                                          #teste la chaine à la position indiquée. Le test est sensible à la case.

print("olivier".startswith("ol"))
 # Reponse : True
print("olivier".startswith(("ol", "eng")))
 # Reponse : True
print("olivier".startswith(("xxx", "ol")))         ####????? d abord je voudrais comprendre la presentation generale de la fonction meme 
 # Reponse : False                                          #et savoir de meme plus ce que sont les paramatres que contiennent cette fonction
print("olivier".startswith("OL"))                           # c est quoi le "eng" ou que represente le eng dans les exples appliques a gauches?
 # Reponse : False
print("olivier".startswith("ol"))
 # Reponse : True



##  str.find(string): La méthode find trouve la première occurence de la recherche demandée.
print(a.find("i"))
    # ou
print("olivier".find("i"))


##  str.split(séparateur) : La méthode split transforme une chaine de caractères en liste.


print("olivier:engel".split(":"))        ### ????? cette chaine de caractere doit elle  tjrs etre un  
 #['olivier', 'engel'] s affiche                 # elt dun dictionnairen pr quelle  se transforme en liste?
                                                 #doit il tjrs y avoir qqc a l interieur de la fction plit() ?                                                  



## str.splitlines([keepends]):Retourne une liste des lignes de la chaine.
                             #Cette méthode utilise le saut à la ligne universel,
                             #le retour à la ligne n'est pas inclu, à moins de
                             #renseigner le paramètre keepends à True.



print("olivier\n\n\engel\n\ndéveloppeur".splitlines())
 # ['olivier', '', '\\engel', '', 'développeur']
print("olivier\nengel\ndéveloppeur".splitlines())
 # ['olivier', 'engel', 'développeur']
print("olivier\n\rengel\n\rdéveloppeur".splitlines())      #####???  c est quoi keepends?
 # ['olivier', '', 'engel', '', 'développeur']
print("olivier\r\nengel\r\ndéveloppeur".splitlines())
 # ['olivier', 'engel', 'développeur']
print("olivier\r\nengel\r\n\r\ndéveloppeur".splitlines())
 # ['olivier', 'engel', '', 'développeur']
print("olivier\r\nengel\r\n\r\ndéveloppeur".splitlines(True))
 # ['olivier\r\n', 'engel\r\n', '\r\n', 'développeur']




## str.join(liste): La méthode join transforme une liste en chaine de caractères.
print( ":".join(["olivier", "engel"]))
 #'olivier:engel' s affichera.         ######???? je remerque pr que cette methode s execute il faut a tt pris mettre qqc devant join().
                                                # en plus ns donne un elt dun dictionnaire


##  len(s): Retourne le nombre d'items ou elt d'un objet.
print(len([1,2,3]))
 # le nbre d element ici c est 3
print(len("olivier"))
 # le nbre d element ici c est 7


##  reverse(): La méthode reverse inverse l'ordre d'une liste.

x = [1,4,7]
x.reverse()
print(x)
 #[7, 4, 1] s affiche

## reversed([]): Retourne un itérateur inversé.

print(list(reversed([1,2,3,4])))
# [4, 3, 2, 1] s affiche


## list.sort(): La méthode sort permet de trier une liste.

l = [5,1,4,2,10]
l.sort()
print(l)
 # [1, 2, 4, 5, 10] nous obtenons une liste trie de facon ordonnee

## sorted(iterable)Tri un élément itérable.

print(sorted([3,2,12,1]))
 # [1, 2, 3, 12] la liste est triee de facon ordonnee


##  max() / min(): Retourne la valeur la plus élévée pour max() et la plus basse pour min()
print(max([1,3,2,6,99,1]))
 # ici 99 s affiche
print(max(1,4,6,12,1))
 # ici 12 s affiche

 

##  zip(*iterables): Permet de regrouper sous la forme d'un tuple les items de listes.
"""
a = ["olivier", "bruce", "john"]      ####????? comment faire pour afficher le resultat ?
b = ["engel", "wayne", "Wayne"]                # avec print ca ne marche pas
zip(a,b)
 # resultat : [('olivier', 'engel'), ('bruce', 'wayne'), ('john', 'Wayne')]
"""

##  locals(): Retoune un dictionnaire avec les valeurs des variables en cours.
"""
print(locals()
 #{'a': 12, '__builtins__': , '__package__': None, 'i': 20, 'v': 101,
 #'liste': [True, False, True], '__name__': '__main__', '__doc__': None})
"""                                ####????? je ne comprend pas ce que fait exactement cette fction. priere d executer ensemble





##  choice([]): Retourne une valeur d'une liste aléatoirement.
import random
print( random.choice([1,2,3,4,5]))


##  randint() : Retourne un int aléatoire.
import random
print(random.randint(1,11))


## random(): Retourne une valeur aléatoire.
import random
random.random()                     ####???? retourne t elle cette valeur d une liste, dictionnaire, tuple?


##  shuffle([]): Mélange aléatoirement une liste.
import random
x = [1,2,3,4,5]
random.shuffle(x)
print(x)
 #[2, 5, 4, 1, 3]pourrait aussi s afficher


##  map(function, []): Execute une fonction sur chaque item d'un élément itérable.

"""
def add_one(x):               ###???? pouvez vous svp bien m expliquer ce qu on veut dans cette defintition ?
     return x + 1                   #je souhaiterai que nous l executons ensemble. je ne trouve pas 
                                    # cmt bien ecrire le programme
map(add_one, [1,2,3])

 # [2, 3, 4] s affiche
"""



## round(number): Arrondi un nombre.

print(round(1))
 # reponse c est 1.0
print(round(1.2))
 # reponse c est 1.0
print(round(1.5))
 # reponse c est 2.0
print(round(1.7))
 # reponse c est 2.0
print(round(-1.7))
 # reponse c est -2.0
print(round(-1.2))
 # reponse c est -1.0


##  sum(iterable [,start]):Additionne les valeurs d'un élément itérable.

print(sum([1,2,3]))        ###?????? c est quoi iterable dans sum(iterable [,start])
 # reponse 6                       # de meme pourquoi la viegule devant strart et que represente start ici


##  hex: Convertit un nombre en valeur hexadécimale.

print(hex(16))
 # Reponse : '0x10'    ####??? que signifit cette reponse ecrite '0x10'?



##  bin(x) : Convertit un integer en chaine de caractères binaires.

print(bin(101))
 # Reponse :'0b1100101'  ####???? c est quoi un caractere binaire? a quoi sert ceci?



##  dir(object) : Indique les noms de la structure de l'objet.

print(dir(int))
['__abs__', '__add__', '__and__', '__class__', '__cmp__', '__coerce__',
 '__delattr__', '__div__', '__divmod__', '__doc__', '__float___',
 '__floordiv__', '__format__', '__getattribute__', '__getnewargs__',
 '__hash__', '__hex__', '__index__', '__init__', '__int__',
 '__invert__', '__long__', '__lshift__', '__mod__', '__mul__',
 '__neg__', '__new__', '__nonzero__', '__oct__', '__or__', '__pos__',
 '__pow__', '__radd__', '__rand__', '__rdiv__', '__rdivmod__',
 '__reduce__', '__reduce_ex__', '__repr__', '__rfloordiv__',
 '__rlshift__', '__rmod__', '__rmul__', '__ror__', '__rpow__',       ####?????je ne comprend pas ce que fait cette fonction
 '__rrshift__', '__rshift__', '__rsub__', '__rtruediv__',
 '__rxor__', '__setattr__', '__sizeof__', '__str__', '__sub__',
 '__subclasshook__', '__truediv__', '__trunc__', '__xor__',
 'bit_length', 'conjugate', 'denominator', 'imag', 'numerator', 'real']



## eval(expression,globals=None,locals=None) = Execute une chaine de caractères.

v = 101                                             ####????? que signifit ce qui est dans la parenthense devant de aval?
print(eval('v+1'))                                          # v devient t elle une chaine de caractere et s additionne avec 1 ?
 #ca va executer 102                                        # pourquoi ne se concatene t elle pas?





##  help(element): Cette fonction vous retourne des informations
                 # sur l'utilisation de l'élément qui vous intéresse.
"""
>>> help(int)

Help on class int in module __builtin__:

class int(object)
 |  int(x=0) -> int or long
 |  int(x, base=10) -> int or long
 |  
 |  Convert a number or string to an integer, or return 0 if no arguments
 |  are given.  If x is floating point, the conversion truncates towards zero.
 |  If x is outside the integer range, the function returns a long instead.
 |  
 |  If x is not a number or if base is given, then x must be a string or
 |  Unicode object representing an integer literal in the given base.  The
 |  literal can be preceded by '+' or '-' and be surrounded by whitespace.
 |  The base defaults to 10.  Valid bases are 0 and 2-36.  Base 0 means to
 |  interpret the base from the string as an integer literal.
 |  >>> int('0b100', base=0)
 |  4
"""
                                                #####????? je voudrais que vous m expliquer mieux cet exple
                                
 

