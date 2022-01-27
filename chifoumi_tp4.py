import random

# Pierre > Ciseaux
# Ciseaux > Feuille
# Feuille > Pierre

feuille = 1
ciseaux = 2
pierre = 3

coup = ["Pierre", "Ciseaux", "Feuille"]

def tirage():
    coup_ordi = random.randint(1,3)
    if coup_ordi == 1:
        return "Pierre"
    elif coup_ordi == 2:
        return "Feuille"
    else:
        return "Ciseaux"

def coup_Joueur():
    joueur = input("Votre choix(Pierre, Feuille, Ciseaux): ")
    coup = ["Pierre", "Ciseaux", "Feuille"]
    if joueur in coup:
        return joueur
    else:
        print("Pas un coup valid!")
        coup_Joueur()

#coup_Joueur()

def uneManche():
    pair_result = pair()
    if pair_result in [("Pierre", "Ciseaux"), 
                          ("Feuille", "Pierre"), 
                          ("Ciseaux", "Feuille")]:
        return "J"
    elif pair_result[1] == pair_result[0]:
        return "E"
    else:
        return "O"
#print("result : " + uneManche())

def pair():
    ordi = tirage()
    hum = coup_Joueur()
    print("ordinateur: " + ordi)
    return hum,ordi
#print("result : " + uneManche())

def chifoumi(n):
    st_result = ""
    for i in range(n):
        partie = uneManche()
        print("result : " + partie)
        st_result = st_result + partie
    return st_result

def result():
    n=int(input("\ncombien de parties vous voulez jouer?\n" ))
    st_result = chifoumi(n)
    print("\nFinal: " + st_result)
    j = st_result.count("J")
    o = st_result.count("O")
    e = st_result.count("E")
    if j==o:
        print("partie nulle!")
    elif j>0:
        print("victoire du joueur!")
    else:
        print("victoire de l'ordinateur!")
    new_value()



def new_value():
    new = input(f"\n\nVoulez vous jouez une autre partie?(oui ou non)\n")
    if new == "oui":
        return result()
    elif new == "non":
        print("jeux terminé")
    else:
        print("veuillez entrez une bonne réponse")


result()

#print(chifoumi(int(input("combien de parties vous voulez jouer?\n" ))))

