
front = []
back = []
def init(n):
    """initialisant front et back en des listes
de taille n"""
    global front
    global back
    front = [0]*n
    back = [0]*n
    front[n//2] = 1


def swap():
    """initialisant front et back en des listes
de taille n"""
    global front
    global back
    front, back = back, front

def print_automate():
    """initialisant front et back en des listes
de taille n"""
    global front
    dict = {0: " ", 1: "█"}
    for elem in front:
        print(dict[elem], end="")
    print()


rule = [0,1,1,0,0,1,1,0]
rule_corre= [7, 6, 5, 4, 3, 2, 1, 0]

def computIndex(bl1,bl2,bl3):
    """crire une fonction computeIndex prenant en argument trois booléens,
et retournant l’entier de l’écriture binaire constituée
de ces trois booléens.
"""
    val_bina=[4,2,1]
    result = bl1*val_bina[0] + bl2*val_bina[1] + bl3*val_bina[2]
    return rule_corre.index(result)


def step(rule, front):
    """
prenant en argument une règle, sous la forme d’une liste de 8 booléens.
Étant donné l’état courant de la grille dans front, step calcule le nouvel état de la grille et l’écrit
dans back.
"""
    i = 1
    n = len(front)
    global back
    while 0 < i < n-1:
        back[i] = rule[computIndex(front[i-1],front[i],front[i+1])]
        i+=1

def run(n_step, s_grid, rule):
    """prenant en argument une règle, sous la forme d’une liste de 8 booléens.
Étant donné l’état courant de la grille dans front, step calcule le nouvel état de la grille et l’écrit
dans back. """
    global front
    init(s_grid)
    n = 0
    while n < n_step:
        print_automate()
        step(rule, front)
        swap()
        n+=1

#run(32,64,rule)

def my_split(s, c):
    strin = ""  # creer un string vide
    result = []
    for carac in s:
        if carac != c:
            strin = strin + carac
        else:
            result.append(strin)
            strin = ""

    return result  # result est une liste
#print(my_split("bonjour tout le monde", " "))

def merge(intervals):
    todo = set()
    for n_list in intervals:
        todo.add(tuple(n_list))
    result = []
    for tup in todo:
        result.append(list(tup))
    for lis in result:
        for lis1 in result:
            if lis != lis1:
                if lis[0] <= lis1[1] <= lis[1]:
                    test = lis1.extend(lis)
                    result.add(min(test), max(test))
                    result.remove(lis1)
                    result.remove(lis)
        return result

print(merge([[1,4],[1,4]]))

def existsZ(lis):
    for elem in lis:
        if "Z" not in elem:
            return False
    return True

