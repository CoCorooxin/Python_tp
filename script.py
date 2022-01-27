
def clean_list(liste):
    for elem in liste:
        if elem == "":
            liste.remove(elem)

def wc(nomFichier):
    z = 0
    with open(nomFichier, encoding="utf-8",mode="r") as f:
        list_mots = []
        mot = ""
        text = f.read()
        for elem in nomFichier:
            if elem.isalnum() is True:
                mot += elem
            else:
                list_mots.append(mot)
                mot = ""
        clean_list(list_mots)
        m = len(list_mots)

        if "\n" in nomFichier:
            n = (len(nomFichier) - 2*nomFichier.index("\n"))
            z += nomFichier.index("\n")
        else:
            n = len(nomFichier)

        my_tuple = n, m, z

        return my_tuple
#print(wc(Users\Chaumi\Desktop\XinXin_BIG_projet\script.py))


def my_function():
    print("I am inside function")
# We can test function by calling it.


print("before import")
import math

print("before functionA")
def functionA():
    print("Function A")

print("before functionB")
def functionB():
    print("Function B {}".format(math.sqrt(100)))

print("before __name__ guard")

if __name__ == '__main__':
    functionA()
    functionB()

print("after __name__ guard")







