
monagenda = [ "" for i in range(366)]
n = 0  # variable pour compter le nombre d'évenements
for i in range(366):
    if i == 1:
        monagenda[i] = "Jour de l’An"
        n += 1
    elif i == 121:
        monagenda[i] = "Fête du Travail"
        n += 1
    elif i == 128:
        monagenda[i] = "Victoire 45"
        n += 1
    elif i == 195:
        monagenda[i] = "Fête Nationale"
        n += 1
    elif i == 315 :
        monagenda[i] = "Armistice 18"
        n += 1
    elif i == 67 :
        monagenda[i] = "Mon anniversaire!"
        n += 1
    for q in range(11): #ex5 il y a 11 seances de judo:
        if i == 3 + q*7:
            monagenda[i] = f"Cours de Judo numéro {q+1}"
            n += 1


#ex2
def affiche(a): # prendre une liste en parametre; print str
    for (i,x) in enumerate(a):
        print(f"jour {i} {x}")

#affiche(monagenda)

def affiche_partiel(a): # prendre une liste en parametre; print str
    n = 0
    for (i,x) in enumerate(a):
        if x != "":
            print(f"jour {i} {x}")
            n += 1
    return n
#affiche_partiel(monagenda)


#ex4
month_name = [" Janvier ", "Février ", "Mars", "Avril", "Mai", "Juin", "Juillet", "Août", "Septembre", "Octobre", "Novembre" , "Décembre"]
month_length = [31,28,31,30,31,30,31,31,30,31,30,31]
def month_of_day(j):  #parametre j est un entier return un str
    for i in range(len(month_length)):
        if j <= month_length[i]:
            return(month_name[i])
        else:
            j-= month_length[i]
#print(month_of_day(32))

def day_in_month(jour):
    for i in range(len(month_length)):
        if jour <= month_length[i]:
            return jour
        else:
            jour-= month_length[i]
#print(day_in_month(67))

def affiche_semaine(agenda, reverse): # parametre agenda : liste parametre reverse: valeur booleen
    m = 3
    week_days = ["Lun", "Mar", "Mer", "Jeu", " Ven", " Sam", "Dim"]
    print(f"Il y a {n} événements dans l’agenda.")
    if reverse:
        for (i, x) in enumerate(agenda):
            week = week_days[m % 7]
            m += 1
            if x != "":
                print(f"{week} {day_in_month(i)} {month_of_day(i)} {x}")
    elif reverse is False:
        reweek = []
        for (i, x) in enumerate(agenda):
            week = week_days[m % 7]
            m += 1
            if x != "":
                reweek.append(f"{week} {day_in_month(i)} {month_of_day(i)} {x}")
        ls = reweek[::-1]
        print("\n".join(ls))

affiche_semaine(monagenda, True)

#ex 5

#def








