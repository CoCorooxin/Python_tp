import random

# Pierre > Ciseaux
# Ciseaux > Feuille
# Feuille > Pierre

feuille = 1
ciseaux = 2
pierre = 3
Lézard = 4
Spock = 5

coup = ["Pierre", "Ciseaux", "Feuille","Lézard", "Spock"]

def tirage():
    coup_ordi = random.randint(1,5)
    if coup_ordi == 1:
        return "Pierre"
    elif coup_ordi == 2:
        return "Feuille"
    elif coup_ordi == 3:
        return "Ciseaux"
    elif coup_ordi == 4:
        return "Lézard"
    else:
        return "Spock"


def coup_Joueur():
    joueur = input("Votre choix(Pierre, Feuille, Ciseaux, Lézard , Spock): ")
    coup = ["Pierre", "Ciseaux", "Feuille","Lézard", "Spock"]
    if joueur in coup:
        return joueur
    else:
        print("Pas un coup valid!")
        coup_Joueur()

#coup_Joueur()
combi_possible =[(x,y) for x in coup for y in coup]
def rules():
    pair_result = uneManche()
    if pair_result in [("Pierre", "Ciseaux"), ("Pierre","Lézard"),
                          ("Feuille", "Pierre"), ("Feuille", "Spock"),
                          ("Ciseaux", "Feuille"),("Ciseaux", "Lézard"),
                        ("Lézard", "Feuille" ), ("Lézard", "Spock"),
                       ("Spock", "Pierre" ), ("Spock", "Ciseaux")]:
        return "J"
    elif pair_result[1] == pair_result[0]:
        return "E"
    else:
        return "O"


def uneManche():
    ordi = tirage()
    hum = coup_Joueur()
    print("ordinateur: " + ordi)
    return hum,ordi
#print("result : " + uneManche())


def chifoumi(n):
    st_result = ""
    for i in range(n):
        partie = rules()
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

