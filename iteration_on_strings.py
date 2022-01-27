#Exercice 19 (Itération par la fin, ??)
#Écrire une fonction attendant une chaîne s de caractères comme argument et qui affiche chaque caractère de
#s sur une ligne (par caractère), du dernier au premier.
def iter_par_fin(s):
    n=len(s)
    for i in range(n-1,0,-1):
        print(s[i],end="")
    return

s = "Cela implique notamment que tout ce que l’on peut faire avec une chaîne de caractères peut être fait avec un caractère"
#print(iter_par_fin(s))



# tran_vi: the tranch between space
# Exercice 21 (Toutes les tranches, ? ? ?)
# 1. Considérant une chaîne s de caractères. Quelle est, en fonction de len(s), la longueur de la plus
# longue tranche de s commençant à l’indice i (tel que 0 ≤ i < len(s))

# 2. Écrire une fonction attendant une chaîne s de caractères comme argument et affichant à l’écran toutes
# les tranches non-vides de s (sans se soucier des potentiels doublons). La fonction doit être construite
# autour d’une boucle for (sur des indices dans s et sur les longueurs des tranches).

def f(s):
    list_length = []
    list_words=[]
    for i in range(len(s)):
        if s[i]== " ":
            n = sum(list_length)
            list_length.append((i-n))
            list_words.append(s[n:i])
    return list_words

s = "Cela implique notamment que tout ce que l’on peut faire avec une chaîne de caractères peut être fait avec un caractère"


maxi = max(f(s), key = len)

#print(f(s))
#print(maxi)

#Exercice 26 (Concaténation)
def test(x):
    if 2<=x<=8:
        return True
    else:
        return False
#print(test(25))

#Exercice 30 (Ordinaux anglais)
def cardinal(number):
    if number == 1:
        return "1st"
    elif number == 2:
        return "2nd"
    elif number == 3:
        return "3rd"
    else:
        return str(number)+"th"

#print(cardinal(4))

#ex31
def f(x,y):
    if x != y:
        if x<y and x<0:
            return -x
        else:
            return x

    elif y<0:
        return -y
    return y

#ex33 . 2
def affiche(n):
    for i in range(n):
        if i%2==0 :
            print("*",end="")
        else:
            print(" ",end="")



#affiche(7)

def divisors(n):
    for i in range(1,n):
        if n%i == 0:
            yield i

#divisors(60)


def is_perfect(n):
    m=0
    for i in divisors(n):
        m+=int(i)
    if m==n:
        return f'{n} est parfait.'

#print(is_perfect(28))

def enum_perfect(m):
    for i in range(1,m+1):
        if is_perfect(i) is not None:
            print(f"{i} est parfait")

#enum_perfect(1000)
