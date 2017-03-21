#!/usr/bin/env python
# -*- coding: utf-8 -*-

def Kruskal(A):
    '''tworzy minimalne drzewo rozpinające'''
    N = len(A)
    drzewo = []
    krawedzie = [(x,i,j) for i,row in enumerate(A)
                         for j,x in enumerate(row)
                  if x != float('inf') and i < j]
    ktory_las = list(range(N))
    lasy  = [[i] for i in range(N)]

    # podwójne odwrócenie pozwala usuwać z końca listy, wydajniej
    krawedzie.sort(reverse = True)

    for waga,i,j in reversed(krawedzie):
        l1 = ktory_las[i]
        l2 = ktory_las[j]
        if l1 != l2:  # są z różnych lasów
            drzewo.append( (waga,i,j) )
            mini = l1 if len(lasy[l1]) < len(lasy[l2]) else l2
            maxi = l1 if mini == l2 else l2
            for w in lasy[mini]:
                ktory_las[w] = maxi
            lasy[maxi].extend(lasy[mini])
            lasy[mini] = []
        krawedzie.pop()

    D = [[float('inf') if i != j else 0 for j in range(N)]
                                        for i in range(N)]
    for waga,i,j in drzewo:
        D[i][j] = waga
        D[j][i] = waga
    return D

if __name__=='__main__':
    import sys
    n = 7   if len(sys.argv) < 3 else   int(sys.argv[1])
    p = 0.7 if len(sys.argv) < 3 else float(sys.argv[2])

    from Gnl import H
    from DIdecorate import zerosToInfs
    l = zerosToInfs(H(n, p))
    '''
    l = [[0,3,3,float('inf'),float('inf')],
         [3,0,1,float('inf'),float('inf')],
         [3,1,0,2,1],
         [float('inf'),float('inf'),2,0,2],
         [float('inf'),float('inf'),1,2,0]]
    '''

    from GraphDigital2 import *
    d = Kruskal(l)
    wyswietl(l)
    wyswietl(d)