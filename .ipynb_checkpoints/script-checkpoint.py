from itertools import islice
import numpy as np
import string

lang = {}

def take(n, iterable):
    return list(islice(iterable, n))

def getList(dict): 
    list = [] 
    for key in dict.keys(): 
        list.append(key) 
          
    return list

def get_trigrams_freqs(text):
    len(text)
    freqs = {}

    first = [char.lower() for char in text if char not in (string.punctuation + ' ')]
    first = ''.join(first)

    for i in range(0, len(first) - 2):
        key = first[i:i+3]
        freqs[key] = 0

    for tri in freqs:
        occurence = 0
        for j in range(0, len(first) - 2):
            key = first[j:j+3]
            if (tri == key):
                occurence += 1
        freq = float(occurence / ( len(first)/3 ) )
        freqs[tri] = freq

    freqs = {k: v for k, v in sorted(freqs.items(), key=lambda item: item[1], reverse=True)}

    return take(15, freqs.items())

eng = "This May 26th Quantum League will be available on Steam! Do you like a good fight and healthy competition? Try out this 2v2 arena, king of the hill, three clone time rewind mechanic, barrels, and all type of game. Put your skills and tactics into overdrive and wishlist for Early Access now!"
fr = """Vous recherchez une histoire en français. Que ce soit pour un nouveau né ou de jeunes enfants, le moment de la lecture est souvent un moment privilégié entre parents et enfants. Quel plaisir pour une petite fille ou un petit garçon quand son papa ou sa maman lui lit une histoire.
Lire une histoire à un enfant avant de dormir contribue à un endormissement serein. Celà lui permet de s’évader dans un monde fabuleux ou a contrario d’aborder des sujets qui l’ont touché durant sa journée. Lui raconter une histoire chaque soir, c’est aussi prendre du temps pour son enfant. Ca peut être une nouvelle histoire ou une histoire qu’il connait déjà et qu’il aime beaucoup."""
lang['English'] = get_trigrams_freqs(eng)
lang['Francais'] = get_trigrams_freqs(fr)

print(lang['Francais'])