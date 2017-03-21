#!/usr/bin/python
# -*- coding: utf-8 -*-

from Gnl import *
from spojne import *
from randomizeWeights import *


def losowyZWagami(n,l):
    if l < 1 or l > n*(n-1)/2:
       print "Wprowadź inne dane (błędna liczba krawędzi)."

    czujnik = 0
    while 1:
       A = G(n, l)
       s = najwiekszaSpojna(A)

       if s[0] != 0:
          break

       czujnik += 1
       if czujnik == 100000:
          print "Wprowadź inne dane (za długi czas losowania)."
          sys.exit()

    # weź tylko wiersze i kolumny, których indeksy są w najdłuższej spójnej składowej
    from GraphSlice import GraphSlice
    A = GraphSlice(A, s[1])

    from DIdecorate import zerosToInfs
    A = zerosToInfs(A)
    randomizeWeights(A)
    return A


if __name__=='__main__':
    import sys

    # UWAGA! n,l to wartości STARTOWE, nie docelowe!
    n = 5 if len(sys.argv) < 3 else int(sys.argv[1])
    l = 5 if len(sys.argv) < 3 else int(sys.argv[2])

    A = losowyZWagami(n,l)

    from GraphDigital import *

    wyswietl(A)
