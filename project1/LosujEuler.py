#!/usr/bin/python
# -*- coding: utf-8 -*-

from Gnl import *
from konwersje import *


def LosujEuler(n,p):
   np = []
   puste = []

   if n < 3:
      return None

   # weź losowy
   li = matrixToList(H(n,p))

   # zbierz wierzchołki o stopniach nieparzystych

   np = [i for i,elem in enumerate(li) if len(elem) % 2 == 1]

   # liczba wierzchołków ze stopniem nieparzystym musi być parzysta, stąd skok o 2
   for i in range(0,len(np),2):
      # jeśli dana para sąsiaduje ze sobą...
      ind = next((j for j,elem in enumerate(li[np[i]]) if elem == np[i+1]), None)

      if ind != None:  # to usuń połączenie
         li[np[i]].remove(np[i+1])
         li[np[i+1]].remove(np[i])
      else:            # a jeśli nie, to je dodaj
         li[np[i]].append(np[i+1])
         li[np[i+1]].append(np[i])
   return li


if __name__=='__main__':
    import sys

    n = 4   if len(sys.argv) < 2 else int(sys.argv[1])
    p = 0.5 if len(sys.argv) < 2 else float(sys.argv[2])

    l = LosujEuler(n,p)
    from GraphDigital import *
    wyswietl(l)