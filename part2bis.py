from math import *

def scalaire(a,b):
    assert type(a) is list and type(b) is list, "a et b  ne respecte pas les conditions"
    if len(a) != len(b):
        return None
    else:
        return sum((i * j for(i , j ) in zip(a,b)))
               
a = [5,8,6,8,7,9]
b = [8,9,2,3,4,5]

def norme(a):
    assert type(a) is list , "a ne respecte pas les conditions"
    somme = 0
    for e in a:
        somme+= e**2
    return sqrt(somme)


def simi(a,b):
    scal =  scalaire(a,b)
    nor = norme(a) * norme(b)
    return scal/nor


print(simi(a,b))