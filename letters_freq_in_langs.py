"""EX1"""
def get_letter_frequence(text): # prendre en argu un string
    dicto_result = {}
    strin = text.lower().replace(" ", "")
    N = len(strin)
    for cr in strin:
        if cr == " ":
            continue
        dicto_result[cr] = strin.count(cr)/N*100
    return dicto_result

#print(get_letter_frequence("Hey bob"))


"""Ex2"""
import os
def get_files_in_corpus(corpus):
    result = []
    for fichier in os.listdir(corpus):
        if fichier.endswith(".txt"):
            result.append(os.path.join(corpus, fichier))
    return result

#print(get_files_in_corpus("corpus"))
"""['corpus\\ada-lovelace-de.txt', 'corpus\\ada-lovelace-en.txt', 'corpus\\ada-lovelace-es.txt', 'corpus\\ada-lovelace-fr.txt', 'corpus\\ada-lovelace-it.txt', 'corpus\\doc-de.txt', 'corpus\\doc-en.txt', 'corpus\\doc-es.txt', 'corpus\\doc-fr.txt', 'corpus\\doc-it.txt']
"""
"""
Ex3
"""

def get_frequence(corpus):
    dict_frq = {}
    for fichier in get_files_in_corpus(corpus):
            with open(fichier, "r", encoding= "utf-8") as f:
                data = f.read()
                dict_frequence = get_letter_frequence(data)
                dict_frq[fichier.strip("corpus\\")] = {"a": dict_frequence["a"]}   # add a value as subdict for the first layer key
                dict_frq[fichier.strip("corpus\\")]["e"] = dict_frequence["e"]   # items in subdict
                dict_frq[fichier.strip("corpus\\")]["i"] = dict_frequence["i"]
                dict_frq[fichier.strip("corpus\\")]["o"] = dict_frequence["o"]
                dict_frq[fichier.strip("corpus\\")]["u"] = dict_frequence["u"]
            """I finally understand why there is always an error if I try to add all 5 as sub dict or as new items in dic
            I just doesn't work like that.... you need to add the value of the first items as a subdict, and all others as items in subdict
            like this we can get a dict with a sub dict......"""
    return dict_frq
#print(get_frequence("corpus"))
"""
{'ada-lovelace-de.txt': {'a': 6.881933796338053, 'e': 15.53170379724001, 'i': 7.75683232614774, 'o': 2.633715161901326, 'u': 3.3552809596825113}, 'ada-lovelace-en.txt': {'a': 8.656777077829709, 'e': 11.542369437106279, 'i': 6.599268441373704, 'o': 6.502743344848608, 'u': 2.3013615118878277}, 'ada-lovelace-es.txt': {'a': 12.353332632832476, 'e': 12.04861475955308, 'i': 6.118874995621869, 'o': 7.2887114286715, 'u': 4.020874925571784}, 'ada-lovelace-fr.txt': {'a': 8.974498100922409, 'e': 13.814432989690722, 'i': 5.935973955507325, 'o': 5.013564839934888, 'u': 4.612045577862181}, 'ada-lovelace-it.txt': {'a': 12.021194392317033, 'e': 10.564079920521028, 'i': 9.658902748647753, 'o': 6.722596313058836, 'u': 3.2453913235456455}, 'doc-de.txt': {'a': 5.4602341542188135, 'e': 13.625353249899073, 'i': 8.155026241421073, 'o': 3.0783205490512717, 'u': 4.178441663302382}, 'doc-en.txt': {'a': 8.346286701208982, 'e': 10.004317789291882, 'i': 8.095854922279793, 'o': 7.085492227979275, 'u': 3.402417962003454}, 'doc-es.txt': {'a': 10.994962216624685, 'e': 11.309823677581864, 'i': 6.801007556675064, 'o': 7.8085642317380355, 'u': 3.6397984886649875}, 'doc-fr.txt': {'a': 6.52237118397674, 'e': 13.558391213051205, 'i': 6.616055564529155, 'o': 5.579066386690357, 'u': 5.443385559683412}, 'doc-it.txt': {'a': 9.26391215335939, 'e': 11.408896333519449, 'i': 11.222780569514237, 'o': 8.384515168434767, 'u': 2.8243067187790807}}
 """


def somme_frequence(text):
    dict = get_letter_frequence(text)
    return sum(list(dict.values()))
#print(somme_frequence("Hey bob"))
# Pourquoi n’est-elle pas forcement égale à 100% ?


"""
ex3
"""
import csv

def read_frequencies(freq_file):
    result = {}
    with open(freq_file, 'r', encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            lang = row["letter"]
            result[lang] = {}
            row.pop("letter")
            for key, val in row.items():
                result[lang][key] = float(val)
    return result

#print(read_frequencies("./corpus/frequences-transposee.csv"))
"""
{'en': {'a': 8.167, 'b': 1.492, 'c': 2.782, 'd': 4.253, 'e': 12.702, 'f': 2.228, 'g': 2.015, 'h': 6.094, 'i': 6.966, 'j': 0.153, 'k': 0.772, 'l': 4.025, 'm': 2.406, 'n': 6.749, 'o': 7.507, 'p': 1.929, 'q': 0.095, 'r': 5.987, 's': 6.327, 't': 9.056, 'u': 2.758, 'v': 0.978, 'w': 2.36, 'x': 0.15, 'y': 1.974, 'z': 0.074, 'à': 0.0, 'â': 0.0, 'á': 0.0, 'å': 0.0, 'ä': 0.0, 'ã': 0.0, 'ą': 0.0, 'æ': 0.0, 'œ': 0.0, 'ç': 0.0, 'ĉ': 0.0, 'ć': 0.0, 'č': 0.0, 'ď': 0.0, 'ð': 0.0, 'è': 0.0, 'é': 0.0, 'ê': 0.0, 'ë': 0.0, 'ę': 0.0, 'ě': 0.0, 'ĝ': 0.0, 'ğ': 0.0, 'ĥ': 0.0, 'î': 0.0, 'ì': 0.0, 'í': 0.0, 'ï': 0.0, 'ı': 0.0, 'ĵ': 0.0, 'ł': 0.0, 'ñ': 0.0, 'ń': 0.0, 'ň': 0.0, 'ò': 0.0, 'ö': 0.0, 'ô': 0.0, 'ó': 0.0, 'õ': 0.0, 'ø': 0.0, 'ř': 0.0, 'ŝ': 0.0, 'ş': 0.0, 'ś': 0.0, 'š': 0.0, 'ß': 0.0, 'ť': 0.0, 'þ': 0.0, 'ù': 0.0, 'ú': 0.0, 'û': 0.0, 'ŭ': 0.0, 'ü': 0.0, 'ů': 0.0, 'ý': 0.0, 'ź': 0.0, 'ż': 0.0, 'ž': 0.0}, 'fr': {'a': 7.636, 'b': 0.901, 'c': 3.26, 'd': 3.669, 'e': 14.715, 'f': 1.066, 'g': 0.866, 'h': 0.737, 'i': 7.529, 'j': 0.613, 'k': 0.074, 'l': 5.456, 'm': 2.968, 'n': 7.095, 'o': 5.796, 'p': 2.521, 'q': 1.362, 'r': 6.693, 's': 7.948, 't': 7.244, 'u': 6.311, 'v': 1.838, 'w': 0.049, 'x': 0.427, 'y': 0.128, 'z': 0.326, 'à': 0.486, 'â': 0.051, 'á': 0.0, 'å': 0.0, 'ä': 0.0, 'ã': 0.0, 'ą': 0.0, 'æ': 0.0, 'œ': 0.018, 'ç': 0.085, 'ĉ': 0.0, 'ć': 0.0, 'č': 0.0, 'ď': 0.0, 'ð': 0.0, 'è': 0.271, 'é': 1.504, 'ê': 0.218, 'ë': 0.008, 'ę': 0.0, 'ě': 0.0, 'ĝ': 0.0, 'ğ': 0.0, 'ĥ': 0.0, 'î': 0.045, 'ì': 0.0, 'í': 0.0, 'ï': 0.005, 'ı': 0.0, 'ĵ': 0.0, 'ł': 0.0, 'ñ': 0.0, 'ń': 0.0, 'ň': 0.0, 'ò': 0.0, 'ö': 0.0, 'ô': 0.023, 'ó': 0.0, 'õ': 0.0, 'ø': 0.0, 'ř': 0.0, 'ŝ': 0.0, 'ş': 0.0, 'ś': 0.0, 'š': 0.0, 'ß': 0.0, 'ť': 0.0, 'þ': 0.0, 'ù': 0.058, 'ú': 0.0, 'û': 0.06, 'ŭ': 0.0, 'ü': 0.0, 'ů': 0.0, 'ý': 0.0, 'ź': 0.0, 'ż': 0.0, 'ž': 0.0}, 'de': {'a': 6.516, 'b': 1.886, 'c': 2.732, 'd': 5.076, 'e': 16.396, 'f': 1.656, 'g': 3.009, 'h': 4.577, 'i': 6.55, 'j': 0.268, 'k': 1.417, 'l': 3.437, 'm': 2.534, 'n': 9.776, 'o': 2.594, 'p': 0.67, 'q': 0.018, 'r': 7.003, 's': 7.27, 't': 6.154, 'u': 4.166, 'v': 0.846, 'w': 1.921, 'x': 0.034, 'y': 0.039, 'z': 1.134, 'à': 0.0, 'â': 0.0, 'á': 0.0, 'å': 0.0, 'ä': 0.578, 'ã': 0.0, 'ą': 0.0, 'æ': 0.0, 'œ': 0.0, 'ç': 0.0, 'ĉ': 0.0, 'ć': 0.0, 'č': 0.0, 'ď': 0.0, 'ð': 0.0, 'è': 0.0, 'é': 0.0, 'ê': 0.0, 'ë': 0.0, 'ę': 0.0, 'ě': 0.0, 'ĝ': 0.0, 'ğ': 0.0, 'ĥ': 0.0, 'î': 0.0, 'ì': 0.0, 'í': 0.0, 'ï': 0.0, 'ı': 0.0, 'ĵ': 0.0, 'ł': 0.0, 'ñ': 0.0, 'ń': 0.0, 'ň': 0.0, 'ò': 0.0, 'ö': 0.443, 'ô': 0.0, 'ó': 0.0, 'õ': 0.0, 'ø': 0.0, 'ř': 0.0, 'ŝ': 0.0, 'ş': 0.0, 'ś': 0.0, 'š': 0.0, 'ß': 0.307, 'ť': 0.0, 'þ': 0.0, 'ù': 0.0, 'ú': 0.0, 'û': 0.0, 'ŭ': 0.0, 'ü': 0.995, 'ů': 0.0, 'ý': 0.0, 'ź': 0.0, 'ż': 0.0, 'ž': 0.0}, 'es': {'a': 11.525, 'b': 2.215, 'c': 4.019, 'd': 5.01, 'e': 12.181, 'f': 0.692, 'g': 1.768, 'h': 0.703, 'i': 6.247, 'j': 0.493, 'k': 0.011, 'l': 4.967, 'm': 3.157, 'n': 6.712, 'o': 8.683, 'p': 2.51, 'q': 0.877, 'r': 6.871, 's': 7.977, 't': 4.632, 'u': 2.927, 'v': 1.138, 'w': 0.017, 'x': 0.215, 'y': 1.008, 'z': 0.467, 'à': 0.0, 'â': 0.0, 'á': 0.502, 'å': 0.0, 'ä': 0.0, 'ã': 0.0, 'ą': 0.0, 'æ': 0.0, 'œ': 0.0, 'ç': 0.0, 'ĉ': 0.0, 'ć': 0.0, 'č': 0.0, 'ď': 0.0, 'ð': 0.0, 'è': 0.0, 'é': 0.433, 'ê': 0.0, 'ë': 0.0, 'ę': 0.0, 'ě': 0.0, 'ĝ': 0.0, 'ğ': 0.0, 'ĥ': 0.0, 'î': 0.0, 'ì': 0.0, 'í': 0.725, 'ï': 0.0, 'ı': 0.0, 'ĵ': 0.0, 'ł': 0.0, 'ñ': 0.311, 'ń': 0.0, 'ň': 0.0, 'ò': 0.0, 'ö': 0.0, 'ô': 0.0, 'ó': 0.827, 'õ': 0.0, 'ø': 0.0, 'ř': 0.0, 'ŝ': 0.0, 'ş': 0.0, 'ś': 0.0, 'š': 0.0, 'ß': 0.0, 'ť': 0.0, 'þ': 0.0, 'ù': 0.0, 'ú': 0.168, 'û': 0.0, 'ŭ': 0.0, 'ü': 0.012, 'ů': 0.0, 'ý': 0.0, 'ź': 0.0, 'ż': 0.0, 'ž': 0.0}, 'it': {'a': 11.745, 'b': 0.927, 'c': 4.501, 'd': 3.736, 'e': 11.792, 'f': 1.153, 'g': 1.644, 'h': 0.636, 'i': 10.143, 'j': 0.011, 'k': 0.009, 'l': 6.51, 'm': 2.512, 'n': 6.883, 'o': 9.832, 'p': 3.056, 'q': 0.505, 'r': 6.367, 's': 4.981, 't': 5.623, 'u': 3.011, 'v': 2.097, 'w': 0.033, 'x': 0.003, 'y': 0.02, 'z': 1.181, 'à': 0.635, 'â': 0.0, 'á': 0.0, 'å': 0.0, 'ä': 0.0, 'ã': 0.0, 'ą': 0.0, 'æ': 0.0, 'œ': 0.0, 'ç': 0.0, 'ĉ': 0.0, 'ć': 0.0, 'č': 0.0, 'ď': 0.0, 'ð': 0.0, 'è': 0.263, 'é': 0.0, 'ê': 0.0, 'ë': 0.0, 'ę': 0.0, 'ě': 0.0, 'ĝ': 0.0, 'ğ': 0.0, 'ĥ': 0.0, 'î': 0.0, 'ì': -0.03, 'í': 0.03, 'ï': 0.0, 'ı': 0.0, 'ĵ': 0.0, 'ł': 0.0, 'ñ': 0.0, 'ń': 0.0, 'ň': 0.0, 'ò': 0.002, 'ö': 0.0, 'ô': 0.0, 'ó': 0.0, 'õ': 0.0, 'ø': 0.0, 'ř': 0.0, 'ŝ': 0.0, 'ş': 0.0, 'ś': 0.0, 'š': 0.0, 'ß': 0.0, 'ť': 0.0, 'þ': 0.0, 'ù': -0.166, 'ú': 0.166, 'û': 0.0, 'ŭ': 0.0, 'ü': 0.0, 'ů': 0.0, 'ý': 0.0, 'ź': 0.0, 'ż': 0.0, 'ž': 0.0}}
"""

"""
ex4
"""
import math
def dist_2d(p1,p2):
    dist = math.sqrt(math.pow(p1[0]-p2[0],2) + (p1[1]-p2[1])**2)
    """ dist = ((p1[0]-p2[0])**2 + (p1[1]-p2[1])**2)**0.5"""
    return dist
#print(dist_2d([4,0],[0,3]))
"""
utilise le lib math
math.pow(x, n = power)
 math.sqrt() non rounded
 math.isqrt() rounded
 """

def dist_nd(p1,p2):
    somme_pw = 0
    for i in range(len(p1)):
        somme_pw += math.pow(p1[i] - p2[i], 2)
    return(somme_pw**0.5)
#print(dist_nd([4,0,3,6,1], [0,3,0,5,0]))


"""
EX5
"""
def frequencies_to_vector(lang_dict):
    dict = {}
    for key in lang_dict:
        if key != 'a' and key != 'u' and key!= 'e' and key!= 'i' and key!= 'o':
            continue
        dict[key] = lang_dict[key]
    result = list(dict.values())
    return result
freq = read_frequencies("./corpus/frequences-transposee.csv")
#print(frequencies_to_vector(freq["en"]))
"""[8.167, 12.702, 6.966, 7.507, 2.758]"""


def guess_language_in_corpus(corpus):
    l_file = get_files_in_corpus(corpus)
    l_frq = get_frequence(corpus)
    dict_dist = {}
    for file in l_file:
        print(file.strip("corpus\\"))
        print(l_frq[file.strip("corpus\\")])
        l_frq_file = list(l_frq[file.strip("corpus\\")].values())
        for lang in read_frequencies("./corpus/frequences-transposee.csv"):
            l_frq_lang = frequencies_to_vector(freq[lang])
            dict_dist[lang] = dist_nd(l_frq_file, l_frq_lang)
        print(dict_dist)
        print(f"the closest language: {min(dict_dist, key = dict_dist.get)} | the distance : {min(list(dict_dist.values()))}")
guess_language_in_corpus("corpus")

import itertools
from functools import reduce
def dist_oneline(p1,p2):
    return math.sqrt(reduce(lambda a, b: a+b, map(lambda a: math.pow(a[0] - a[1], 2), itertools.zip_longest(p1,p2))))

"""
lambda
fonction classique:
def sum_classic( a , b ):
  return a + b
Avec les lambda on aura le code suivant:
sum_lambda = lambda a,b : a+b
map :
map(function, iterable, ...)
The map() function applies a given function to each item of an iterable (list, tuple etc.) and returns an iterator.
itertools.zip_longest
Make an iterator that aggregates elements from each of the iterables.
If the iterables are of uneven length, missing values are filled-in with fillvalue.
Iteration continues until the longest iterable is exhausted.
"""