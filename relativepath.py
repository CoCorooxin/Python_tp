""""
Supposer pour cet exercice l’existence d’un type file permettant de représenter les élements d’un système
de fichiers. Si e est de type file,
— e.name est une valeur de type str, le nom de e ;
— e.parent est une valeur de type file, le parent de e si e n’est pas la racine et e sinon.
Définir une fonction relative_path prenant en argument un chemin relatif sous forme d’une liste path et
trois str sep (pour le séparateur), curdir (pour le dossier de départ) et pardir (pour le passage à un dossier
parent), et retournant la chaîne de caractères représentant ce chemin
"""
def relative_path(path, sep, curdir, pardir):  # path de files
    rel_path = [curdir]
    for i in range(1, len(path)):
        if path[i] == path[i-1].parent:
            rel_path.append(pardir)
        else:
            rel_path.append(path[i].name)
    return sep.join(rel_path)


"""
The Operators:
x << y
Returns x with the bits shifted to the left by y places (and new bits on the right-hand-side are zeros). This is the same as multiplying x by 2**y.
x >> y
Returns x with the bits shifted to the right by y places. This is the same as //'ing x by 2**y.
x & y
Does a "bitwise and". Each bit of the output is 1 if the corresponding bit of x AND of y is 1, otherwise it's 0.
x | y
Does a "bitwise or". Each bit of the output is 0 if the corresponding bit of x AND of y is 0, otherwise it's 1.
~ x
Returns the complement of x - the number you get by switching each 1 for a 0 and each 0 for a 1. This is the same as -x - 1.
x ^ y
"""

import os

"""
print(os.path.join(os.sep, "home", "guest"))
print(os.curdir)
print(os.pardir)
print(os.sep)
"""

path = os.curdir
path = os.path.join(path, "doc", os.pardir, "videos", "films")
#print(path)

"""
print(os.getcwd())
for e_name in os.listdir(os.getcwd()): print(e_name)

for e_na in os.listdir(os.curdir): print(e_na)
"""

path = os.path.join(os.sep, "home", "guest")
#print(path)

#print(os.path.exists(path))

"""ex3
afficher les fichier
"""
#for e_na in os.listdir(os.curdir):
    #if os.path.isfile(e_na):
     #   print(e_na)

"""4
afficher les dossier
"""
#for e_name in os.listdir(os.curdir):
    #if os.path.isdir(e_name):
        #print(e_name)

"""ex5 
"""
f = open("wordCount.txt", "r")
#print(f.read())
#print(f.read())
"""
Biographie courte d'Emile Zola 
- Fils d'un ingÃ©nieur d'origine vÃ©nitienne et d'une femme originaire de la Beauce, 
Emile Zola naÃ®t le 2 avril 1840 Ã  Paris mais passe sa jeunesse Ã  Aix-en-Provence. 
A sept ans, il est orphelin de pÃ¨re, ce qui pose des difficultÃ©s financiÃ¨res Ã  sa mÃ¨re. 
Il va tout de mÃªme au collÃ¨ge oÃ¹ il cÃ´toie Paul CÃ©zanne, mais les problÃ¨mes d'argent lui interdisent bientÃ´t les Ã©tudes. 
Revenu Ã  Paris en 1858, il Ã©choue deux fois au baccalaurÃ©at Ã  cause du franÃ§ais. 
Puis, renonÃ§ant Ã  peser plus longtemps sur le budget de sa mÃ¨re, il dÃ©cide de chercher du travail. 
AprÃ¨s quelques petits postes ingrats, il entre en 1862 Ã  la librairie Hachette en tant que commis.  
C'est en 1864 qu'il fait la connaissance de celle qui deviendra sa femme, Alexandrine Meley. 
Cependant, Emile Zola ne lui sera pas fidÃ¨le et entretiendra Ã  l'Ã¢ge de 50 ans et jusqu'Ã  sa mort une double vie avec Jeanne Rozerot qui lui donne ses deux enfants, Denise (1889) et Jacques (1891). Les deux femmes acceptent cette situation, mais Emile Zola dira souvent qu'en voulant faire le bonheur de tous, il a fait le malheur de chacun. A la mort de l'Ã©crivain, Alexandrine accepte que Denise et Jacques portent le nom de leur pÃ¨re.

"""
#print(f.readline()) # read the first line
#print(f.readline()) #read the second line in the first line with an aditionnal empty line
#print(f.readline())
"""
Biographie courte d'Emile Zola 

- Fils d'un ingÃ©nieur d'origine vÃ©nitienne et d'une femme originaire de la Beauce, 

Emile Zola naÃ®t le 2 avril 1840 Ã  Paris mais passe sa jeunesse Ã  Aix-en-Provence. 

"""
#print(f.readlines()) # read the file as a list separated by \n,

f.close()

with open("wordCount.txt", "r") as f:
    print(f.readline())
    print(f.readlines())
    print(f.read())
"""
— Bonjour, comment allez-vous ?
— Très bien, et vous ?



[]
"""

"""
-Bonjour, comment allez-vous?

["— Bonjour, comment allez-vous ?\n", "— Très bien, et vous ?"]
— Bonjour, comment allez-vous ?
— Très bien, et vous ?

"""

"""
Ex6
prenre en parametre, un fichier et un gestionnaire dentree et sortie obtenu a l'ouverture dun fichier
"""
def f(f):
    l = []

    while True:
        ligne = f.readline()
        l.append(ligne())
        if ligne == "":  # f.readline() == ""  la fin de la ligne , f.readline == "\n" une ligne vide dans le texte
            break
    return l
"""
ex7
prendre en argument une chaine de caractere representant un chemin 
"""
def f(filename):
    if os.path.isfile(filename):
        with open(filename, "r"):
            e_line = f.readline()
            while(e_line != ""):
                if e_line[0] != "#":
                   print(e_line)

"""
ex8
"""
def split_name(name):  # prendre en arguments une chaine de caracteres
    dict = {}
    l_name = name.split()
    if len(l_name) == 2 :
        dict["prenom"] = l_name[0]
        dict["nom"] = l_name[1]
        return dict
    else:
        return None
#print(split_name("George Sand"))

def word_set(filename): # prendre en argument un chemin en string
    with open(filename, "r") as f:
        return f.read().split(" ")

#print(word_set("wordCount.txt"))

with open("wordCount.txt", "w") as f:
    f.write("coucou")









