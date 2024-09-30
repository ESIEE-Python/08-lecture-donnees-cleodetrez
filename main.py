#### Imports et définition des variables globales
"""
Le module random est importé
"""
FILENAME = "listes.csv"
#### Fonctions secondaires
def read_data(filename) :
    """Retourne le contenu du fichier <filename>
    Args :
        filename (str): nom du fichier à lire
    Returns :
        list : le contenu du fichier (1 liste par ligne)
    """
    l = []
    with open(filename, mode='r', encoding='utf8') as f :
        s = f.readlines()
        for ligne in s :
            elements = ligne.strip().split(";")
            l.append([int(x) for x in elements])
    return l

def get_list_k(data, k):
    """
    Retourne la kème liste de data
    """
    return data[k]

def get_first(l):
    """
    Retourne le premier élément de la liste
    """
    return l[0]

def get_last(l):
    """
    Retourne le dernier élément de la liste
    """
    return l[-1]

def get_max(l):
    """
    Retourne le max de la liste
    """
    return max(l)

def get_min(l):
    """
    Retourne le min de la liste
    """
    return min(l)

def get_sum(liste):
    """Retourne la somme des éléments dans une liste de nombres sous forme de chaînes."""
    return sum(liste)


#### Fonction principale


def main():
    """
    Test si la fonction data fonctionne
    """
    data = read_data(FILENAME)
    print(len(data))
    for i, l in enumerate(data):
        print(i, l)
    k = 37
    print(k, get_list_k(data, 37))


if __name__ == "__main__":
    main()
