#using itertools to create pairs
from itertools import combinations

def combos(itemlist, n=2):
    #takes in list, uses combinations from itertools
    #n is the size of the combination; how many to draw from the list at a time
    #n defaults to 2
    #combinations would create duplicates because it takes order into account
    #so uses a set to ignore them
    return list(combinations(itemlist, n))