#!/usr/bin/env python
# -*- coding: utf-8 -*-

from Gnl import G
from spojne import najwiekszaSpojna
from DIdecorate import *

def losowyDigraf(n,l):
    A = G(n,l)
    A = zerosToInfs(A)
    s = najwiekszaSpojna(A)
    A = [[elem for j,elem in enumerate(wiersz) if j in s[1]] for i,wiersz in enumerate(A) if i in s[1]]
    A = toDI(A)
    return A


if __name__=='__main__':
    import sys

    # UWAGA! n,l to wartości STARTOWE, nie docelowe!
    n = 5 if len(sys.argv) < 2 else int(sys.argv[1])
    l = 5 if len(sys.argv) < 2 else int(sys.argv[2])

    A = losowyDigraf(n,l)
    from GraphDigital2 import *
    wyswietl(A, showWeights=False)
