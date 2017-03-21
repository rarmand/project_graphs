#!/usr/bin/env python
# -*- coding: utf-8 -*-

import random
from DIrandomizeWeights import randomizeWeights
from printCosts import printCosts

def prostaSiecPrzeplywowa(n):
    '''tworzy losową sieć przepływową'''
    war = [1 for x in xrange(n+2)]    # po warstwie na źródło i ujście
    # war przechowuje liczbę wierzchołków w warstwie
    
    w = 2    # źródło ujście
    for i in xrange(1, n+1):
        war[i] = random.randint(2, n)
    w = sum(war)

    A = [[float('inf') for j in xrange(w)] for i in xrange(w)]

    ne = 1
    for k in xrange(1, n+1):
        for j in xrange(war[k]):
            i = random.randint(ne - war[k-1], ne-1)
            A[i][ne+j] = 1    # łącz w tył
            i = random.randint(ne + war[k], ne + war[k] + war[k+1] - 1)
            A[ne+j][i] = 1    # łącz w przód
        ne += war[k]
    return A

def dodajLukow(ile, A):
    w = len(A)
    for i in xrange(ile):
        a = b = 0
        while    a == b    or    A[a][b] == 1:
            a = random.randint(1, w-2)
            b = random.randint(1, w-2)
        A[a][b] = 1
    return A

def siecPrzeplywowa(n, nn=-1, minWeight=1, maxWeight=10):
    nn = nn if nn >= 0 else 2*n

    A = prostaSiecPrzeplywowa(n)
    A = dodajLukow(nn, A)
    A = randomizeWeights(A, minWeight, maxWeight)
    return A


if __name__=='__main__':
    import sys

    # 2 <= N <= 4
    n =    4 if len(sys.argv) < 2 else     int(sys.argv[1])


    A = siecPrzeplywowa(3)

    printCosts(A)
