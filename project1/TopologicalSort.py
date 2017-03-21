#!/usr/bin/python
# -*- coding: utf-8 -*-

from Acykliczny import *
from konwersje import *
from GraphDigital import *



def CheckNode(v, vlist, visited, sorteds):
  ''' funkcja pomocnicza w sprawdzaniu wierzchołków '''

  visited[v] = True

  # jeśli wierzchołek wskazuje na inne wierzchołki, musi je sprawdzić
  if len(vlist[v]) > 0:
    for i in vlist[v]:
      if visited[i] == False:
        CheckNode(i, vlist, visited, sorteds)

  # sprawdzony wierzchołek "zamalowuje na czarno", czyli dodaje do listy posortowanych
  sorteds.append(v)


def TopologicalSort(Matrix):
  '''sortowanie topologiczne za pomocą przeszukiwania w głąb
  funkcja pobiera macierz sąsiedztwa z funkcji DAG(n) '''

  Vlista = matrixToList(Matrix)
  N = len(Matrix)

  # wizytowane
  visited = [False for i in range(N)]
  # posortowane
  sorteds = []

  for i in range(N):
    if visited[i] == False:
      CheckNode(i, Vlista, visited, sorteds)

  if len(sorteds) < len(Matrix):
    print "CYKL!"

  # odwrócona lista posortowanych - pseudopostać drzewa
  sorteds.reverse()
  return sorteds



if __name__=='__main__':
  import sys

  # UWAGA! n,l to wartości STARTOWE, nie docelowe!
  n =   5 if len(sys.argv) < 3 else   int(sys.argv[1])
  p = 0.7 if len(sys.argv) < 3 else float(sys.argv[2])
  print n, p

  A = DAG(n, p)

  from GraphDigital import *

  print "Lista sąsiedztwa:"
  print matrixToList(A)
  S = TopologicalSort(A)
  print "SORTOWANIE TOPOLOGICZNE:"
  print S
  
  #print A
  wyswietl(A)
